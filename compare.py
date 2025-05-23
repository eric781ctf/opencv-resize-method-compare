import os
import cv2

# ========== 主流程：讀取多個圖片進行分析 ==========
def main():
    # key = 方法名稱, value = resize 圖片路徑
    method_to_path = {
        'nearest': 'resize/upscale/nearest/nearest_5x.png',
        'linear': 'resize/upscale/linear/linear_5x.png',
        'cubic': 'resize/upscale/cubic/cubic_5x.png',
        'lanczos': 'resize/upscale/lanczos/lanczos_5x.png'
    }

    original_path = 'images/original/original.jpg'
    original_img = cv2.imread(original_path)
    if original_img is None:
        raise FileNotFoundError(f"找不到原始圖片：{original_path}")

    # 收集各個方法的分析結果
    all_results = {}
    for method, path in method_to_path.items():
        img = cv2.imread(path)
        if img is None:
            print(f"警告：找不到圖片 {path}，跳過。")
            continue
        metrics = analyze_all_metrics(original_img, img)
        all_results[method] = metrics

    # 根據每個指標分別畫圖
    save_dir = "results/metrics_charts"
    metric_names = list(next(iter(all_results.values())).keys())
    for metric in metric_names:
        data = {method: all_results[method][metric] for method in all_results}
        plot_metric_bar_chart(metric, data, save_dir)
