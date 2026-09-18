# EMD 在睡眠研究中的應用

互動演算法網站，展示**經驗模態分解（Empirical Mode Decomposition, EMD）**在睡眠 EEG 訊號分析上的應用。

## 主題背景

由黃鍔院士（Norden E. Huang）於 1998 年提出的 EMD／希爾伯特–黃轉換（HHT），是分析非線性、非穩態生理訊號的革命性工具。本網站以互動示範的方式，說明 EMD 如何從睡眠腦電圖（EEG）中分解出 δ、θ、α、σ 等各頻帶的固有模態函數（IMF）。

## 功能特色

- **互動式 EMD 示範**：選擇不同睡眠期（Wake / N1 / N2 / N3 / REM），即時觀察訊號分解過程
- **可調雜訊強度**：模擬真實生理訊號的量測雜訊
- **IMF 視覺化**：原始訊號與各層 IMF 疊加展示
- **理論說明**：涵蓋 EMD 篩選算法、HHT 頻譜、各睡眠期特徵
- **學術引用**：列出 8 篇核心參考論文

## 技術架構

- **純前端靜態網站**（Single-page HTML）
- 自行實作 EMD 演算法（含自然三次樣條插值）
- 無外部 JS 框架相依，部署簡易

## 本地執行

```bash
# 直接用瀏覽器開啟
open index.html

# 或啟動本地伺服器
python3 -m http.server 8080
```

## 部署

本站已部署於：
- **Zeabur**：見 `zeabur.json`
- **GitHub Pages**：推送至 `main` 分支即可

## 參考論文

1. Huang et al. (1998) — EMD 原始論文，*Proc. R. Soc. Lond. A*, 454(1971), 903–995. [doi:10.1098/rspa.1998.0193](https://doi.org/10.1098/rspa.1998.0193)
2. Wu & Huang (2009) — EEMD，*Advances in Adaptive Data Analysis*, 1(1), 1–41. [doi:10.1142/S1793536909000047](https://doi.org/10.1142/S1793536909000047)
3. Hassan & Bhuiyan (2016) — CEEMDAN 睡眠自動分期，*Biomedical Signal Processing and Control*, 24, 1–10. [doi:10.1016/j.bspc.2015.09.002](https://doi.org/10.1016/j.bspc.2015.09.002)
4. Liang et al. (2005) — EMD 神經訊號分析，*Neurocomputing*, 65–66, 801–807. [doi:10.1016/j.neucom.2004.10.077](https://doi.org/10.1016/j.neucom.2004.10.077)
5. Flandrin et al. (2004) — EMD as a filter bank，*IEEE Signal Processing Letters*, 11(2), 112–114. [doi:10.1109/LSP.2003.821662](https://doi.org/10.1109/LSP.2003.821662)
6. Pachori & Bajaj (2011) — EEG 異常偵測，*Computer Methods and Programs in Biomedicine*, 104(3), 373–381. [doi:10.1016/j.cmpb.2011.03.009](https://doi.org/10.1016/j.cmpb.2011.03.009)
7. Yeh et al. (2010) — 心跳時間序列固有模態分析，*Annals of Biomedical Engineering*, 38(4), 1337–1344. [doi:10.1007/s10439-010-9939-z](https://doi.org/10.1007/s10439-010-9939-z)
8. Hsu et al. (2013) — EEG 能量特徵睡眠分期，*Neurocomputing*, 104, 105–114. [doi:10.1016/j.neucom.2012.11.003](https://doi.org/10.1016/j.neucom.2012.11.003)
