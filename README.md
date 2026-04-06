# Pengolahan Citra Digital - Tugas 4

Proyek ini mengimplementasikan beberapa operasi dasar pemrosesan citra menggunakan Python dan OpenCV.

## Isi Proyek

- `tugas4.py`: skrip Python yang melakukan:
  - konversi RGB ke grayscale
  - threshold binarisasi
  - reduksi ke m-bit grayscale
  - perubahan brightness dan kontras
  - histogram grayscale
  - histogram equalization
- `Kucing.jpg`: gambar input untuk diproses
- `tugas4_output.png`: hasil visualisasi yang disimpan dari skrip
- `.gitignore`: daftar file/folder yang tidak di-push ke Git
- `requirements.txt`: daftar dependensi Python

## Dependensi

Instal paket yang dibutuhkan dengan:

```bash
python -m pip install -r requirements.txt
```

Isi `requirements.txt`:

- `opencv-python`
- `matplotlib`
- `numpy`

## Menjalankan Skrip

Jalankan perintah berikut di folder proyek:

```bash
python tugas4.py
```

Skrip akan menghasilkan file `tugas4_output.png` di folder yang sama.

## Catatan GUI

Secara default skrip menggunakan backend Matplotlib non-interaktif untuk menghindari masalah `Tkinter` di lingkungan yang belum terpasang Tcl/Tk. Jika kamu ingin menampilkan plot langsung di jendela GUI, ubah skrip dengan:

- menghapus atau mengomentari baris `matplotlib.use('Agg')`
- mengganti `plt.savefig('tugas4_output.png')` dengan `plt.show()`

Pastikan Python terpasang dengan dukungan Tcl/Tk agar `plt.show()` bisa bekerja.
