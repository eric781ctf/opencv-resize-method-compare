import matplotlib.pyplot as plt
import numpy as np
import os

def plot_rgb_bar_chart(rgb_dict, scale, save_path):
    methods = list(rgb_dict.keys())
    rgb_values = np.array([rgb_dict[m] for m in methods])  # shape: (N, 3)

    x = np.arange(len(methods))
    width = 0.25

    plt.figure(figsize=(10, 6))
    plt.bar(x - width, rgb_values[:, 0], width, label='R', color='#FFB7B2')
    plt.bar(x,         rgb_values[:, 1], width, label='G', color='#C7CEEA')
    plt.bar(x + width, rgb_values[:, 2], width, label='B', color='#B5EAD7')

    plt.xticks(x, methods, rotation=30)
    plt.ylabel("Mean RGB Value")
    plt.title(f"Mean RGB Comparison at {scale}")
    plt.legend()
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.4)

    # 儲存圖
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()
    print(f"[儲存圖] {save_path}")
