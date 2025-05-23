# 📸 OpenCV Resize Method Comparison

這是一個視覺化小專案，旨在比較 OpenCV 各種 `resize` 方法（如 `INTER_LINEAR`, `INTER_AREA`, `INTER_CUBIC`, `INTER_LANCZOS4`）在不同放大與縮小倍率下，對圖片畫質造成的影響。

不使用深度學習模型，僅透過圖像處理與統計特徵分析，評估不同方法在銳利度、資訊熵、色彩偏移與紋理變化上的表現。

---

## ⚙️ 功能與分析

### resize 倍率：
- 放大：`2x`, `5x`, `10x`
- 縮小：`0.5x`, `0.2x`, `0.1x`

### 支援的 resize 方法：
- `cv2.INTER_LINEAR`
- `cv2.INTER_AREA`
- `cv2.INTER_CUBIC`
- `cv2.INTER_LANCZOS4`
- `cv2.INTER_NEAREST`

### 非對齊比較指標：
| 指標名稱          | 說明                         |
|-------------------|------------------------------|
| Mean RGB/LAB      | 亮度、色彩偏移分析           |
| Sharpness         | Laplacian 銳利度             |
| Texture           | Sobel 邊緣強度               |
| Entropy           | 資訊熵，細節豐富程度         |
| RGB Histogram     | 色彩直方圖（可選）           |

---

## 📊 圖表

執行後會自動產生：
- 每個倍數 + 方法下的 **柱狀圖視覺化比較**

---

## 🚀 如何使用

1. 放入原始圖片於：
```bash
images/original/original.jpg
```

2. 執行 resize 與分析主腳本：
```bash
python generate_img.py
```

3. 執行分析與視覺化：
```bash
python compare.py
```

---

## 🙌 Special Thanks
本專案為個人實驗性質，無使用 AI 模型，僅純演算法分析，歡迎參考與擴充。
