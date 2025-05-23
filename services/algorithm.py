import cv2
import numpy as np
from skimage.measure import shannon_entropy
import matplotlib.pyplot as plt
import os

# === 平均像素值 (RGB) ===
def mean_rgb(img):
    return np.mean(img, axis=(0, 1))

# === LAB 色彩空間平均值 ===
def mean_lab(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    return np.mean(lab, axis=(0, 1))

# === 銳利度（Laplacian 變異數） ===
def sharpness_laplacian(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    return lap.var()

# === 紋理強度（Sobel 邊緣總量） ===
def texture_sobel(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobel = cv2.Sobel(gray, cv2.CV_64F, 1, 1, ksize=3)
    return np.mean(np.abs(sobel))

# === 資訊熵（Shannon Entropy） ===
def image_entropy(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return shannon_entropy(gray)



# === 主函式 ===
def analyze_unaligned(original_img, resized_img):
    if original_img is None or resized_img is None:
        raise FileNotFoundError("無法讀取圖片")

    metrics = {
        "Mean RGB (orig)": mean_rgb(original_img),
        "Mean RGB (resized)": mean_rgb(resized_img),
        "Mean LAB (orig)": mean_lab(original_img),
        "Mean LAB (resized)": mean_lab(resized_img),
        "Sharpness (orig)": sharpness_laplacian(original_img),
        "Sharpness (resized)": sharpness_laplacian(resized_img),
        "Texture (orig)": texture_sobel(original_img),
        "Texture (resized)": texture_sobel(resized_img),
        "Entropy (orig)": image_entropy(original_img),
        "Entropy (resized)": image_entropy(resized_img),
    }

    return metrics

