import cv2
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Load gambar asli
img = cv2.imread('Kucing.jpg')
# OpenCV membaca gambar dalam format BGR, kita ubah ke RGB untuk visualisasi Matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

# --- TASK 1: Konversi RGB ke Grayscale ---
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# --- TASK 2: Konversi Grayscale ke Biner ---
# Menggunakan nilai threshold tengah (127)
_, biner = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# --- TASK 3: Konversi Grayscale ke m-bit ---
# Contoh: Mengubah ke 3-bit (hanya memiliki 2^3 = 8 derajat keabuan)
m = 3
mbit = (gray / (256 / (2**m))).astype(np.uint8)
# Dikembalikan ke rentang 0-255 hanya agar bisa dilihat secara visual
mbit_display = mbit * (255 / (2**m - 1)) 
mbit_display = mbit_display.astype(np.uint8)

# --- TASK 4: Image dengan Brightness ---
# Menambahkan intensitas cahaya (alpha=1 untuk kontras tetap, beta=50 untuk tambah cerah)
brightness = cv2.convertScaleAbs(img_rgb, alpha=1, beta=50)

# --- TASK 5: Image dengan Contrast ---
# Meningkatkan kontras (alpha=1.5 untuk kontras dinaikkan, beta=0 untuk brightness tetap)
contrast = cv2.convertScaleAbs(img_rgb, alpha=1.5, beta=0)

# --- TASK 6: Image Grayscale to Histogram ---
# Disiapkan langsung di plot Matplotlib pada bagian visualisasi (subplot 7)

# --- TASK 7: Image dengan Operasi Histogram Equalization ---
equalized = cv2.equalizeHist(gray)


# ====================================================================
# VISUALISASI HASIL KESELURUHAN (Akan muncul di satu jendela)
# ====================================================================
plt.figure(figsize=(15, 10))

plt.subplot(3, 3, 1)
plt.title('Original RGB')
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(3, 3, 2)
plt.title('1. Grayscale')
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 3)
plt.title('2. Biner (Threshold 127)')
plt.imshow(biner, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 4)
plt.title(f'3. {m}-bit Image')
plt.imshow(mbit_display, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 5)
plt.title('4. Brightness (+50)')
plt.imshow(brightness)
plt.axis('off')

plt.subplot(3, 3, 6)
plt.title('5. Contrast (x1.5)')
plt.imshow(contrast)
plt.axis('off')

plt.subplot(3, 3, 7)
plt.title('6. Histogram dari Grayscale')
plt.hist(gray.ravel(), 256, [0,256], color='black')
plt.xlim([0, 256])

plt.subplot(3, 3, 8)
plt.title('7. Histogram Equalization')
plt.imshow(equalized, cmap='gray')
plt.axis('off')

# Ekstra: Perbandingan histogram setelah di-equalize
plt.subplot(3, 3, 9)
plt.title('Histogram setelah Equalization')
plt.hist(equalized.ravel(), 256, [0,256], color='black')
plt.xlim([0, 256])

plt.tight_layout()
plt.savefig('tugas4_output.png')
print('Saved plot to tugas4_output.png')