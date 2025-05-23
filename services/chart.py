import os
import matplotlib.pyplot as plt
from matplotlib import cm
from analyze_metrics import analyze_all_metrics
import cv2

# ========== 圖表主函式：畫出每一種指標的柱狀圖 ==========
def plot_metric_bar_chart(metric_name, method_to_value, save_dir):
    methods = list(method_to_value.keys())
    values = list(method_to_value.values())

    # 馬卡龍色系（手動定義一些柔和色）
    pastel_colors = ['#FFB7B2', '#FFDAC1', '#E2F0CB', '#B5EAD7', '#C7CEEA', '#C9C9FF', '#F3C1C6']
    colors = pastel_colors[:len(methods)]

    plt.figure(figsize=(8, 5))
    plt.bar(methods, values, color=colors)
    plt.title(f"{metric_name} Comparison")
    plt.ylabel(metric_name)
    plt.grid(True, axis='y', linestyle='--', alpha=0.4)
    plt.tight_layout()

    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, f"{metric_name}_bar.png")
    plt.savefig(save_path)
    plt.close()
    print(f"儲存圖表：{save_path}")