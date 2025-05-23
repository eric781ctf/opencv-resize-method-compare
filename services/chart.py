import matplotlib.pyplot as plt
import numpy as np
import os

def plot_vector_metric_bar_chart(vector_dict, scale, labels, title_prefix, save_path):
    import matplotlib.pyplot as plt
    import numpy as np
    import os

    methods = list(vector_dict.keys())
    values = np.array([vector_dict[m] for m in methods])  # shape (N, 3)

    x = np.arange(len(methods))
    width = 0.25
    colors = ['#FFB7B2', '#C7CEEA', '#B5EAD7']

    plt.figure(figsize=(10, 6))
    for i in range(3):
        plt.bar(x + (i - 1) * width, values[:, i], width, label=labels[i], color=colors[i])

    plt.xticks(x, methods, rotation=30)
    plt.ylabel("Mean Value")
    plt.title(f"{title_prefix} Comparison at {scale}")
    plt.legend()
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.4)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()
    print(f"[儲存圖] {save_path}")


import matplotlib.pyplot as plt
import os

def plot_scalar_metric_bar_chart(vector_dict, scale, metric_name, save_path):
    methods = list(vector_dict.keys())
    values = [float(vector_dict[m]) for m in methods]

    colors = ['#FFB7B2', '#FFDAC1', '#E2F0CB', '#B5EAD7', '#C7CEEA', '#C9C9FF', '#F3C1C6']
    colors = colors[:len(methods)]

    plt.figure(figsize=(10, 6))
    plt.bar(methods, values, color=colors)
    plt.ylabel(metric_name)
    plt.title(f"{metric_name} Comparison at {scale}")
    plt.xticks(rotation=30)
    plt.grid(axis='y', linestyle='--', alpha=0.4)
    plt.tight_layout()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()
    print(f"[儲存圖] {save_path}")
