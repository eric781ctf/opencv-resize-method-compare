import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

# === 指標 1：MSE ===
def compute_mse(img1, img2):
    return np.mean((img1.astype("float") - img2.astype("float")) ** 2)

# === 指標 2：MAE ===
def compute_mae(img1, img2):
    return np.mean(np.abs(img1.astype("float") - img2.astype("float")))

# === 指標 3：SSIM ===
def compute_ssim(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    return ssim(gray1, gray2)

# === 指標 4：PSNR ===
def compute_psnr(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    return psnr(gray1, gray2)

# === 指標 5：色差 ΔE（使用 LAB 色彩空間） ===
def compute_delta_e(img1, img2):
    lab1 = cv2.cvtColor(img1, cv2.COLOR_BGR2LAB).astype("float32")
    lab2 = cv2.cvtColor(img2, cv2.COLOR_BGR2LAB).astype("float32")
    delta = np.linalg.norm(lab1 - lab2, axis=2)
    return np.mean(delta)

# === 指標 6：邊緣圖 MSE ===
def compute_gradient_mse(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    grad1 = cv2.Sobel(gray1, cv2.CV_64F, 1, 1, ksize=3)
    grad2 = cv2.Sobel(gray2, cv2.CV_64F, 1, 1, ksize=3)
    return np.mean((grad1 - grad2) ** 2)

# === 主分析函式 ===
def analyze_all_metrics(img1, img2):
    results = {
        "MSE": compute_mse(img1, img2),
        "MAE": compute_mae(img1, img2),
        "SSIM": compute_ssim(img1, img2),
        "PSNR": compute_psnr(img1, img2),
        "DeltaE (LAB)": compute_delta_e(img1, img2),
        "Edge MSE": compute_gradient_mse(img1, img2)
    }
    return results
