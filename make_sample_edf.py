#!/usr/bin/env python3
"""
Generate a synthetic 60-second EDF file containing ECG + tri-axial ACC.

This is SIMULATED data, not a recording from a human subject. It exists so the
website can demonstrate EDF parsing and EMD decomposition without distributing
anyone's physiological data.

Signal design (so the EMD demo shows something meaningful):
  ECG    256 Hz  - PQRST complexes, HR ~62 bpm, modulated by respiratory
                   sinus arrhythmia at 0.25 Hz (15 breaths/min)
  ACC_X   32 Hz  - small postural sway + noise
  ACC_Y   32 Hz  - small postural sway + noise
  ACC_Z   32 Hz  - ~1 g gravity + respiration-driven oscillation at 0.25 Hz
                   + two brief movement bursts
The 0.25 Hz respiratory component in ACC_Z is the payoff: EMD should pull it
out into its own IMF, which is the accelerometer-derived respiration signal
used in real sleep studies.
"""
import math
import random
import struct

random.seed(20260919)

DURATION = 60          # seconds
FS_ECG = 256
FS_ACC = 32
RESP_HZ = 0.25         # 15 breaths per minute
HR_BASE = 62.0         # bpm


def ascii_field(value, width):
    """EDF header fields: ASCII, left-justified, space padded, exact width."""
    s = str(value)
    if len(s) > width:
        s = s[:width]
    return s.ljust(width).encode("ascii")


def ecg_beat(t_rel):
    """One PQRST complex as a sum of Gaussians. t_rel in seconds from R peak."""
    def g(amp, centre, width):
        return amp * math.exp(-((t_rel - centre) ** 2) / (2 * width ** 2))
    return (
        g(120.0, -0.20, 0.025)    # P
        + g(-90.0, -0.035, 0.008)  # Q
        + g(1100.0, 0.0, 0.009)    # R
        + g(-220.0, 0.030, 0.011)  # S
        + g(260.0, 0.180, 0.040)   # T
    )


def build_ecg(n):
    """ECG with respiratory sinus arrhythmia: instantaneous HR varies with breathing."""
    sig = [0.0] * n
    # Place R peaks by integrating instantaneous heart rate.
    peaks = []
    t = 0.6
    while t < DURATION:
        peaks.append(t)
        hr = HR_BASE + 4.5 * math.sin(2 * math.pi * RESP_HZ * t)   # RSA
        t += 60.0 / hr
    for pk in peaks:
        centre = int(pk * FS_ECG)
        span = int(0.45 * FS_ECG)
        for i in range(max(0, centre - span), min(n, centre + span)):
            sig[i] += ecg_beat((i - centre) / FS_ECG)
    # Baseline wander (respiration on the chest electrodes) + mains-ish + noise
    for i in range(n):
        t = i / FS_ECG
        sig[i] += 45.0 * math.sin(2 * math.pi * RESP_HZ * t + 0.6)
        sig[i] += 6.0 * math.sin(2 * math.pi * 50.0 * t)
        sig[i] += random.gauss(0, 7.0)
    return sig


def build_acc(n):
    """Tri-axial accelerometer in g. Z carries gravity + respiration."""
    x = [0.0] * n
    y = [0.0] * n
    z = [0.0] * n
    # Two brief movement bursts (e.g. a postural shift)
    bursts = [(21.0, 1.1), (43.5, 0.8)]
    for i in range(n):
        t = i / FS_ACC
        sway = 0.012 * math.sin(2 * math.pi * 0.07 * t)
        x[i] = 0.02 + sway + 0.004 * math.sin(2 * math.pi * RESP_HZ * t + 1.1) + random.gauss(0, 0.0035)
        y[i] = -0.03 + 0.010 * math.sin(2 * math.pi * 0.05 * t + 2.0) + random.gauss(0, 0.0035)
        z[i] = (
            0.98                                                   # gravity
            + 0.030 * math.sin(2 * math.pi * RESP_HZ * t)          # respiration
            + 0.008 * math.sin(2 * math.pi * 1.05 * t)             # ballistocardiogram-ish
            + 0.006 * math.sin(2 * math.pi * 0.03 * t)             # slow drift
            + random.gauss(0, 0.0030)
        )
        for bt, amp in bursts:
            d = t - bt
            if abs(d) < 0.7:
                env = math.exp(-(d ** 2) / (2 * 0.16 ** 2))
                x[i] += amp * 0.45 * env * math.sin(2 * math.pi * 3.1 * d)
                y[i] += amp * 0.30 * env * math.sin(2 * math.pi * 2.4 * d + 1.0)
                z[i] += amp * 0.35 * env * math.sin(2 * math.pi * 2.8 * d + 0.5)
    return x, y, z


def to_digital(values, phys_min, phys_max):
    """EDF stores int16. Map physical range onto the full digital range."""
    dig_min, dig_max = -32768, 32767
    scale = (dig_max - dig_min) / (phys_max - phys_min)
    out = []
    for v in values:
        d = int(round((v - phys_min) * scale + dig_min))
        out.append(max(dig_min, min(dig_max, d)))
    return out


def main():
    n_ecg = DURATION * FS_ECG
    n_acc = DURATION * FS_ACC

    ecg = build_ecg(n_ecg)
    ax, ay, az = build_acc(n_acc)

    signals = [
        ("ECG",   "uV", -5000.0, 5000.0, FS_ECG, ecg, "HP:0.05Hz LP:100Hz"),
        ("ACC_X", "g",     -8.0,    8.0, FS_ACC, ax,  "LP:16Hz"),
        ("ACC_Y", "g",     -8.0,    8.0, FS_ACC, ay,  "LP:16Hz"),
        ("ACC_Z", "g",     -8.0,    8.0, FS_ACC, az,  "LP:16Hz"),
    ]
    ns = len(signals)
    header_bytes = 256 * (ns + 1)

    h = bytearray()
    h += ascii_field("0", 8)                                  # version
    h += ascii_field("X X X Simulated_subject", 80)           # patient id
    h += ascii_field("Startdate 19-SEP-2026 X X EMD_sleep_demo_synthetic", 80)
    h += ascii_field("19.09.26", 8)                           # start date
    h += ascii_field("22.30.00", 8)                           # start time
    h += ascii_field(header_bytes, 8)
    h += ascii_field("SIMULATED DATA - NOT A HUMAN RECORDING", 44)
    h += ascii_field(DURATION, 8)                             # number of data records
    h += ascii_field(1, 8)                                    # duration of a record (s)
    h += ascii_field(ns, 4)

    for label, *_ in signals:
        h += ascii_field(label, 16)
    for _ in signals:
        h += ascii_field("simulated", 80)
    for _, dim, *_ in signals:
        h += ascii_field(dim, 8)
    for _, _, pmin, *_ in signals:
        h += ascii_field(f"{pmin:g}", 8)
    for _, _, _, pmax, *_ in signals:
        h += ascii_field(f"{pmax:g}", 8)
    for _ in signals:
        h += ascii_field(-32768, 8)
    for _ in signals:
        h += ascii_field(32767, 8)
    for *_, prefilt in signals:
        h += ascii_field(prefilt, 80)
    for _, _, _, _, fs, *_ in signals:
        h += ascii_field(fs, 8)          # samples per data record
    for _ in signals:
        h += ascii_field("", 32)

    assert len(h) == header_bytes, (len(h), header_bytes)

    digital = []
    for label, dim, pmin, pmax, fs, vals, prefilt in signals:
        digital.append((fs, to_digital(vals, pmin, pmax)))

    body = bytearray()
    for rec in range(DURATION):
        for fs, dig in digital:
            chunk = dig[rec * fs:(rec + 1) * fs]
            body += struct.pack("<%dh" % len(chunk), *chunk)

    with open("sample_ecg_acc.edf", "wb") as f:
        f.write(bytes(h))
        f.write(bytes(body))

    print(f"header {header_bytes} B, body {len(body)} B, total {header_bytes + len(body)} B")
    print(f"signals: {[s[0] for s in signals]}")


if __name__ == "__main__":
    main()
