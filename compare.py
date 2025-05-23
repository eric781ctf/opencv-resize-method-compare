import os
import cv2
import re
from services.algorithm import analyze_unaligned
from services.chart import plot_rgb_bar_chart
import json

# ========== 主流程：讀取多個圖片進行分析 ==========
def main():
    img_path_data = {}
    for scale_type in os.listdir('./images/resize'):
        img_path_data[scale_type] = {}
        for method in os.listdir(f'./images/resize/{scale_type}'):
            img_path_data[scale_type][method] = []
            img_path_data[scale_type][method].extend(os.listdir(f'./images/resize/{scale_type}/{method}'))

    print('==============================================================')
    print(img_path_data)
    original_img_path = './images/original/original-1.jpg'
    original_img = cv2.imread(original_img_path)
    if original_img is None:
        raise FileNotFoundError(f"找不到原始圖片：{original_img_path}")

    # 收集各個方法的分析結果
    all_results = {}
    for scale_type in img_path_data:
        all_results[scale_type]={}
        for method in img_path_data[scale_type]:
            all_results[scale_type][method]={}
            for resized_img_name in img_path_data[scale_type][method]:
                resized_img_path = f'./images/resize/{scale_type}/{method}/{resized_img_name}'
                resized_img = cv2.imread(resized_img_path)
                if resized_img is None:
                    print(f"警告：找不到圖片 {resized_img_path}，跳過。")
                    continue

                metrics = analyze_unaligned(original_img, resized_img)
                if scale_type == 'upscale':
                    match = re.search(r'_(\d+x)\.png$', resized_img_name)
                else:
                    match = re.search(r'_([\d_]+x)\.png$', resized_img_name)
                if not match:
                    print(f"警告：無法從檔名解析 scale：{resized_img_name}，跳過。")
                    continue
                else:
                    scale = match.group(1)
                all_results[scale_type][method][scale] = {}
                all_results[scale_type][method][scale][resized_img_name] = metrics


    # 找出第一筆包含原圖指標的資料
    found = next(
        (data for scale_type in all_results
            for method in all_results[scale_type]
            for scale in all_results[scale_type][method]
            for data in all_results[scale_type][method][scale].values()),
        None
    )

    # 提取含 'orig' 的指標
    if found:
        origin_metrix = {k: v for k, v in found.items() if 'orig' in k}

    metric_mapping = {'Mean RGB':{}, 'Mean LAB':{}, 'Sharpness':{}, 'Texture':{}, 'Entropy':{}}
    scale_mapping = ['2x','5x','10x','0_5x','0_2x','0_1x']
    for scale in scale_mapping:
        metric_mapping['Mean RGB'][scale] = {}
        metric_mapping['Mean LAB'][scale] = {}
        metric_mapping['Sharpness'][scale] = {}
        metric_mapping['Texture'][scale] = {}
        metric_mapping['Entropy'][scale] = {}

    for scale_type in all_results:
        for method in all_results[scale_type]:
            for scale in all_results[scale_type][method]:
                for resized_img_name, metrics in all_results[scale_type][method][scale].items():
                    for metric_name, value in metrics.items():
                        if 'orig' in metric_name:
                            continue
                        for metric_key in metric_mapping:
                            if metric_key in metric_name:
                                print(f"scale_type: {scale_type},scale: {scale}, method: {method}, metric_name:{metric_name}")
                                print(value)
                                metric_mapping[metric_key][scale][method] = value

    for metric in metric_mapping:
        for scale in metric_mapping[metric]:
            for data, value in origin_metrix.items():
                if 'orig' in data:
                    if metric in data:
                        metric_mapping[metric][scale]['original'] = value
                        break
                        
    print('================== 單一檢查 ========================')
    print(metric_mapping['Mean RGB']['2x'])
    for metric in metric_mapping:
        if metric == 'Mean RGB':
            for scale in metric_mapping[metric]:
                plot_rgb_bar_chart(metric_mapping[metric][scale], scale, f'./analysis/{scale}_{metric}.png')

if __name__ == "__main__":
    main()