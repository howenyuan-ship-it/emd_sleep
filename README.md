# EMD 在睡眠研究中的應用

互動演算法網站，展示**經驗模態分解（Empirical Mode Decomposition, EMD）**在睡眠 EEG 訊號分析上的應用。

## 線上瀏覽

- **Cloudflare**：https://emd-sleep.howenyuan.workers.dev
- **GitHub Pages**：https://howenyuan-ship-it.github.io/emd_sleep/

## 主題背景

由黃鍔院士（Norden E. Huang）於 1998 年提出的 EMD／希爾伯特–黃轉換（HHT），是分析非線性、非穩態生理訊號的重要工具。本網站以互動示範的方式，說明 EMD 如何從睡眠腦電圖（EEG）中分解出 δ、θ、α、σ 等各頻帶的固有模態函數（IMF）。

## 功能特色

- **互動式 EMD 示範**：選擇不同睡眠期（Wake / N1 / N2 / N3 / REM），即時觀察訊號分解過程
- **可調雜訊強度**：模擬真實生理訊號的量測雜訊
- **IMF 視覺化**：原始訊號與各層 IMF 疊加展示
- **理論說明**：涵蓋 EMD 篩選算法、HHT 頻譜、各睡眠期特徵
- **學術引用**：15 篇參考文獻，分三組並附重點摘要與 DOI 連結

## 技術架構

- **純前端靜態網站**（Single-page HTML）
- 自行實作 EMD 演算法（含自然三次樣條插值、極值偵測、篩選迭代）
- 無外部 JS 框架相依，部署簡易

## 本地執行

```bash
# 直接用瀏覽器開啟
open index.html

# 或啟動本地伺服器
python3 -m http.server 8080
```

## 部署

- **Cloudflare Workers**：連動本 repo，push 至 `main` 自動重新部署
- **GitHub Pages**：Settings → Pages，Source 設為 `main` 分支根目錄
- `zeabur.json` 為早期規劃 Zeabur 部署所留，現已不使用（Zeabur 現行架構需自備伺服器）

---

# 參考文獻

共 15 篇，分為三組。所有書目資料（期刊、卷期、頁碼、作者）皆經 Crossref 逐筆核對。

## A ─ EMD／HHT 方法發展

**[1] Huang, N. E., Shen, Z., Long, S. R., et al. (1998).** "The empirical mode decomposition and the Hilbert spectrum for nonlinear and non-stationary time series analysis." *Proceedings of the Royal Society of London A*, 454(1971), 903–995. [doi:10.1098/rspa.1998.0193](https://doi.org/10.1098/rspa.1998.0193)

> EMD 的原始論文。核心主張是傅立葉分析預設訊號為線性、穩態、由固定頻率正弦波疊加，此前提對多數生理訊號不成立。EMD 改以訊號自身極值點建構上下包絡線，反覆「篩選」逐層萃取固有模態函數（IMF），為資料驅動、無需預設基底的分解方式；搭配希爾伯特轉換可得瞬時頻率，構成 HHT。
> **引用時機**：任何提及 EMD 或 HHT 的段落。

**[2] Wu, Z., & Huang, N. E. (2009).** "Ensemble empirical mode decomposition: a noise-assisted data analysis method." *Advances in Adaptive Data Analysis*, 1(1), 1–41. [doi:10.1142/S1793536909000047](https://doi.org/10.1142/S1793536909000047)

> 解決原始 EMD 最主要的缺陷「模態混疊」（同一 IMF 混入頻率差距甚大的成分）。作法為刻意加入多組白雜訊、各自做 EMD 後平均；雜訊提供均勻參考尺度，平均後互相抵消。
> **引用時機**：說明 EMD 限制，或採用 EEMD／CEEMDAN 時。分析真實 EEG 多用 EEMD 系列，此為源頭。

**[3] Flandrin, P., Rilling, G., & Gonçalvès, P. (2004).** "Empirical mode decomposition as a filter bank." *IEEE Signal Processing Letters*, 11(2), 112–114. [doi:10.1109/LSP.2003.821662](https://doi.org/10.1109/LSP.2003.821662)

> 以寬頻雜訊做數值實驗，發現 EMD 對雜訊的行為近似二進制濾波器組——每上升一階 IMF，中心頻率大致減半。
> **引用時機**：解釋「為何 IMF1 對應高頻、IMF4 對應 δ 波」。這是把 IMF 對應到 EEG 傳統頻帶的理論依據。

**[4] Liang, H., Bressler, S. L., Desimone, R., & Fries, P. (2005).** "Empirical mode decomposition: a method for analyzing neural data." *Neurocomputing*, 65–66, 801–807. [doi:10.1016/j.neucom.2004.10.077](https://doi.org/10.1016/j.neucom.2004.10.077)

> 較早系統性檢視 EMD 是否適用於神經電生理訊號，作者群包含 Bressler、Desimone、Fries。討論 EMD 處理非穩態神經振盪的優勢，也指出邊界效應與 IMF 物理意義詮釋的限制。
> **引用時機**：論證「EMD 適合用於腦波」時，比訊號處理領域論文更具神經科學說服力。

## B ─ EMD 應用於睡眠與腦波分析

**[5] Hassan, A. R., & Bhuiyan, M. I. H. (2016).** "Computer-aided sleep staging using Complete Ensemble Empirical Mode Decomposition with Adaptive Noise and bootstrap aggregating." *Biomedical Signal Processing and Control*, 24, 1–10. [doi:10.1016/j.bspc.2015.09.002](https://doi.org/10.1016/j.bspc.2015.09.002)

> 以 CEEMDAN（逐階加入自適應雜訊的 EEMD 改良版）分解單通道 EEG，從各 IMF 萃取統計特徵，再以 bagging 集成分類器自動分期。「EMD 特徵工程 + 傳統機器學習」路線的代表作。
> **引用時機**：說明 EMD 用於自動睡眠分期的完整流程。

**[6] Hassan, A. R., & Bhuiyan, M. I. H. (2016).** "Automatic sleep scoring using statistical features in the EMD domain and ensemble methods." *Biocybernetics and Biomedical Engineering*, 36(1), 248–255. [doi:10.1016/j.bbe.2015.11.001](https://doi.org/10.1016/j.bbe.2015.11.001)

> 同團隊姊妹作，改用原始 EMD 而非 CEEMDAN，並系統性比較多種集成分類器。
> **引用時機**：需比較 EMD 與 EEMD／CEEMDAN 在同一任務上的表現差異時，與 [5] 並讀。

**[7] Liu, C., Tan, B., Fu, M., Li, J., Wang, J., Hou, F., & Yang, A. (2021).** "Automatic sleep staging with a single-channel EEG based on ensemble empirical mode decomposition." *Physica A: Statistical Mechanics and its Applications*, 567, 125685. [doi:10.1016/j.physa.2020.125685](https://doi.org/10.1016/j.physa.2020.125685)

> 以 EEMD 分解單通道 EEG 後萃取 IMF 特徵進行五分期分類。單通道設定對應穿戴式與居家監測的實際條件。
> **引用時機**：討論 EMD 在居家／穿戴式睡眠監測的應用潛力。

**[8] Saifutdinova, E., Gerla, V., Lhotska, L., Koprivova, J., & Sos, P. (2015).** "Sleep spindles detection using Empirical Mode Decomposition." *2015 International Workshop on Computational Intelligence for Multimedia Understanding (IWCIM)*, 1–5. [doi:10.1109/IWCIM.2015.7347063](https://doi.org/10.1109/IWCIM.2015.7347063)

> 針對 N2 期紡錘波（σ 頻帶約 11–15 Hz 的短暫爆發）偵測。紡錘波短暫、非穩態的特性正是 EMD 強項——在固定窗長的傅立葉分析中易被背景稀釋，EMD 則可自然分離至對應 IMF。
> **引用時機**：說明 N2 期特徵，或論證 EMD 對瞬態事件的優勢。注意為研討會論文，引用時宜與期刊文獻並列。

**[9] Pittman-Polletta, B., Hsieh, W.-H., Kaur, S., Lo, M.-T., & Hu, K. (2014).** "Detecting phase-amplitude coupling with high frequency resolution using adaptive decompositions." *Journal of Neuroscience Methods*, 226, 15–32. [doi:10.1016/j.jneumeth.2014.01.006](https://doi.org/10.1016/j.jneumeth.2014.01.006)

> 以 EMD 類自適應分解取代傳統帶通濾波計算相位–振幅耦合（PAC）。對睡眠研究關鍵：慢波振盪（<1 Hz）相位調控紡錘波振幅被認為是記憶固化的神經機制，而固定頻帶濾波分析此類耦合易生假性結果。
> **引用時機**：討論 SWS 的慢波–紡錘波耦合，或需方法學更嚴謹的 PAC 計算時。

**[10] Pachori, R. B., & Bajaj, V. (2011).** "Analysis of normal and epileptic seizure EEG signals using empirical mode decomposition." *Computer Methods and Programs in Biomedicine*, 104(3), 373–381. [doi:10.1016/j.cmpb.2011.03.009](https://doi.org/10.1016/j.cmpb.2011.03.009)

> 以 EMD 分解 EEG 後，利用 IMF 在解析訊號平面上的橢圓面積特徵區辨正常與癲癇發作腦波。非睡眠研究，但示範 EMD 在 EEG 異常事件偵測上的判別力。
> **引用時機**：論證 EMD 在臨床 EEG 判讀上的普遍適用性。

**[11] Yeh, J.-R., Sun, W.-Z., Shieh, J.-S., & Huang, N. E. (2010).** "Intrinsic mode analysis of human heartbeat time series." *Annals of Biomedical Engineering*, 38(4), 1337–1344. [doi:10.1007/s10439-010-9939-z](https://doi.org/10.1007/s10439-010-9939-z)

> 以 EMD 拆解心跳時間序列的固有模態，出自黃鍔院士主持的中央大學資料分析方法研究中心（他為資深作者）。HRV 高低頻成分反映交感／副交感消長，各睡眠期自律神經狀態差異顯著。
> **引用時機**：將分析從 EEG 延伸到 ECG／HRV 等其他 PSG 導程時。

**[12] Anupama, B., Deshpande, R., Anil Kumar, B., Devika, S. V., & Sidhapuram, A. (2026).** "Empirical Mode Decomposition-Based Classification of Presleep/Sleep/Postsleep Stages." *ICT for Intelligent Systems* (Lecture Notes in Networks and Systems), 69–85. Springer Nature Singapore. [doi:10.1007/978-981-96-9191-3_7](https://doi.org/10.1007/978-981-96-9191-3_7)

> 主題直接針對「入睡前／睡眠／睡後」三段狀態的 EMD 分類，是本清單中唯一觸及睡前與睡後清醒差異的 EMD 研究。
> **使用前請注意**：2026 年 Springer 研討會論文集章節（ICTIS 2025），Crossref 上查無摘要，方法細節、資料來源與結果品質**均未經查證**。列此僅為標示研究方向存在，引用前務必自行取得全文評估。

## C ─ 睡眠生理背景：兩種「清醒」的差異

以下三篇**並非 EMD 研究**，而是傳統頻譜分析，但回答了一個 EMD 文獻尚未處理的問題：入睡前的清醒與起床前後的清醒，在生理上是否相同？

**[13] Cajochen, C., Brunner, D. P., Kräuchi, K., Graw, P., & Wirz-Justice, A. (1995).** "Power density in theta/alpha frequencies of the waking EEG progressively increases during sustained wakefulness." *Sleep*, 18(10), 890–894. [doi:10.1093/sleep/18.10.890](https://doi.org/10.1093/sleep/18.10.890)

> 持續清醒條件下，清醒腦波 θ／α 頻帶功率隨清醒時數單調上升，使 waking theta 成為恆定性睡眠壓力（Borbély 雙歷程模型的 Process S）的可觀測指標。
> **對本主題的意義**：晚上入睡前累積十幾小時清醒，Wake 期腦波 θ 功率處於一日高點。

**[14] Finelli, L. A., Baumann, H., Borbély, A. A., & Achermann, P. (2000).** "Dual electroencephalogram markers of human sleep homeostasis: correlation between theta activity in waking and slow-wave activity in sleep." *Neuroscience*, 101(3), 523–529. [doi:10.1016/S0306-4522(00)00409-7](https://doi.org/10.1016/S0306-4522(00)00409-7)

> 證明睡前清醒腦波的 θ 活動與隨後睡眠中慢波活動（SWA）正相關——兩者是同一恆定性歷程在清醒與睡眠兩側的表現。
> **對本主題的意義**：睡眠壓力在夜間耗散，早晨 Wake 期 θ 功率應顯著低於前一晚入睡前。

**[15] Marzano, C., Ferrara, M., Moroni, F., & De Gennaro, L. (2011).** "Electroencephalographic sleep inertia of the awakening brain." *Neuroscience*, 176, 308–317. [doi:10.1016/j.neuroscience.2010.12.014](https://doi.org/10.1016/j.neuroscience.2010.12.014)

> 剛醒來的腦波雖已判為 Wake，仍帶明顯升高的 δ／θ 與偏低的 β，需數十分鐘才消退，即「睡眠慣性」。
> **對本主題的意義**：起床前後的 Wake 期並非完全清醒，而是帶睡眠成分殘留的狀態。

---

## 綜合觀點與研究缺口

*（整理自上述文獻，非任何單一論文的結論）*

**兩種 Wake 的對比。** 結合 [13]–[15]：**入睡前的清醒**處於高睡眠壓力、低睡眠慣性，θ 功率因長時間清醒累積至高點；**起床前後的清醒**相反，睡眠壓力已耗散，卻帶有尚未消退的睡眠慣性。兩者晝夜節律相位亦不同——前者落在褪黑激素分泌前的清醒維持區，後者剛越過核心體溫最低點。兩種狀態的清醒腦波都可能出現偏慢成分，但**成因完全相反**：一個是睡眠壓力累積，一個是睡眠狀態殘留。在 AASM 判讀標準下兩者同樣標記為單一個「W」，此差異在 hypnogram 上完全不可見。

**EMD 的潛在切入點。** 傳統頻譜以固定頻帶取功率，對上述兩種狀態只能觀察到「都有慢波成分」。EMD 分解出的 IMF 帶有瞬時頻率與瞬時振幅，理論上可區辨「持續性低頻節律」與「間歇性慢波侵入」這兩種不同時間結構——這正是目前文獻尚未填補的空隙。

**已確認的文獻缺口（截至 2026 年 9 月的檢索結果）。** 以 REM 期為主題的 EMD 研究未能檢索到穩固成果，相關查詢回傳多為癲癇、紡錘波或泛用五分期分類論文。入睡初期（sleep onset）方面，檢索到的嗜睡偵測研究多採用 VMD（變分模態分解）或經驗傅立葉分解，屬 EMD 的相近方法而非 EMD 本身，嚴格而言不應混用。此二方向若確為研究稀缺，對後續研究而言即是機會。
