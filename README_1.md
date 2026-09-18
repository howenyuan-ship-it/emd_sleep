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

1. Huang et al. (1998) — EMD 原始論文，Proc. R. Soc. London A
2. Wu & Huang (2009) — EEMD，Advances in Adaptive Data Analysis
3. Hassan & Bhuiyan (2016) — 睡眠自動分期，Journal of Neuroscience Methods
4. Liang et al. (2005) — EMD 神經訊號分析，Neurocomputing
5. Flandrin et al. (2004) — EMD as filter bank，IEEE Signal Processing Letters
6. Pachori & Bajaj (2011) — EEG 異常偵測，Computer Methods and Programs in Biomedicine
7. Yeh et al. (2010) — 睡眠 HRV 分析，Applied Physics Letters
8. Hsu et al. (2013) — EEG 睡眠分期，Neurocomputing
