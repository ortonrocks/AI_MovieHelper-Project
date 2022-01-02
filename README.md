# AI_MovieHelper-Project

詳細項目內容請看=>

https://github.com/ortonrocks/AI_MovieHelper-Project/blob/main/%E5%B0%88%E6%A1%88%E8%AA%AA%E6%98%8E.pptx

  這是我於2021.9-2021.12和團隊開發基於Line 平台的電影整合系統，用戶能在我們的Linebot上獲取
台灣已上映和即將上映的電影資訊。同時利用“電影推薦功能”，將根據用戶輸入喜歡的電影類型和喜歡
的電影推薦現正上映的電影,本推薦系統為動態混合推薦系統，在協同過濾長度基礎上加入NLP的模型，利用
動態權重降低協同過濾的冷啟動問題。

同時開發了基於人臉辨識的訂票檢票系統，用戶利用人臉進行身份註冊後可直接利用人臉掃碼入場，簡化
現有檢票流程的同時提高用戶的觀影體驗。

本專案使用的技術：

AIoT:利用Jetson nano 實現電影檢票功能。

OPENCV Face recognition(hog):檢票人臉偵測和識別

NLP：利用BERT對電影評論進行情感分析，利用TFIDF對用戶電影推薦

Collaborative filter(協同過濾)：利用KnnWithMeans

AIoT:利用Jetson nano 實現電影檢票功能。

docker:結合beautifulsoup ,request 自動化定時爬蟲 





技術架構圖![alt text](https://raw.githubusercontent.com/ortonrocks/AI_MovieHelper-Project/main/structure.jpg?raw=true))


