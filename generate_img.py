import cv2
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
def get_output_path(scale_type, method_name):
    return os.path.join(BASE_DIR, "images", "resize", scale_type, method_name)


input_path = os.path.join(current_dir, "images", "original", "original-1.jpg")
image_path = os.path.normpath(input_path)

img = cv2.imread(input_path)

if img is None:
    raise FileNotFoundError(f"無法讀取圖片：{input_path}")

h, w = img.shape[:2]

# 插值方法與適用場景
resize_methods = {
    "cv2 INTER_NEAREST": {"flag": cv2.INTER_NEAREST, "scale": "both"},
    "cv2 INTER_LINEAR": {"flag": cv2.INTER_LINEAR, "scale": "both"},
    "cv2 INTER_CUBIC": {"flag": cv2.INTER_CUBIC, "scale": "up"},
    "cv2 INTER_LANCZOS4": {"flag": cv2.INTER_LANCZOS4, "scale": "up"},
    "cv2 INTER_AREA": {"flag": cv2.INTER_AREA, "scale": "down"},
}

# 縮放倍率設定
up_scales = [2, 5, 10]
down_scales = [0.5, 0.2, 0.1]  # 1/2, 1/5, 1/10

for method_name, method_info in resize_methods.items():
    flag = method_info["flag"]
    scale_type = method_info["scale"]

    # 建立對應資料夾
    if scale_type in ["up", "both"]:
        outdir = get_output_path("upscale", method_name)
        os.makedirs(outdir, exist_ok=True)
        for scale in up_scales:
            new_size = (int(w * scale), int(h * scale))
            resized = cv2.resize(img, new_size, interpolation=flag)
            filename = f"{method_name}_{scale}x.png"
            cv2.imwrite(os.path.join(outdir, filename), resized)

    if scale_type in ["down", "both"]:
        outdir = get_output_path("downscale", method_name)
        os.makedirs(outdir, exist_ok=True)
        for scale in down_scales:
            new_size = (int(w * scale), int(h * scale))
            resized = cv2.resize(img, new_size, interpolation=flag)
            scale_str = str(scale).replace(".", "_")
            filename = f"{method_name}_{scale_str}x.png"
            cv2.imwrite(os.path.join(outdir, filename), resized)


