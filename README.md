# Sleep Alarm Detection

Sistem deteksi kantuk dan menguap menggunakan computer vision untuk memantau tingkat kewaspadaan pengguna secara real-time.

## 📋 Deskripsi

Aplikasi ini menggunakan teknologi MediaPipe dan OpenCV untuk mendeteksi tanda-tanda kantuk dan menguap pada wajah pengguna melalui webcam. Sistem akan memberikan peringatan suara ketika mendeteksi bahwa pengguna sedang mengantuk atau menguap berlebihan.

## 🔧 Fitur Utama

- **Deteksi Kantuk**: Menggunakan Eye Aspect Ratio (EAR) untuk mendeteksi mata yang tertutup
- **Deteksi Menguap**: Menggunakan Mouth Aspect Ratio (MAR) untuk mendeteksi mulut terbuka
- **Alarm Suara**: Memberikan peringatan beep ketika kantuk atau menguap terdeteksi
- **Real-time Display**: Menampilkan nilai EAR dan MAR secara langsung
- **Visual Alert**: Menampilkan pesan peringatan di layar

## 📦 Dependencies

```bash
pip install opencv-python
pip install mediapipe
```

**Catatan**: `winsound` adalah modul bawaan Python untuk Windows, tidak perlu instalasi terpisah.

## 🚀 Cara Penggunaan

1. Pastikan webcam terhubung dengan komputer
2. Jalankan script:
   ```bash
   python sleepy_detector.py
   ```
3. Posisikan wajah di depan kamera
4. Sistem akan mulai memantau dan memberikan peringatan jika diperlukan
5. Tekan tombol `ESC` untuk keluar dari aplikasi

## ⚙️ Parameter Konfigurasi

| Parameter | Nilai Default | Deskripsi |
|-----------|---------------|-----------|
| `EAR_THRESHOLD` | 0.25 | Batas minimum EAR untuk deteksi mata tertutup |
| `MAR_THRESHOLD` | 0.6 | Batas minimum MAR untuk deteksi menguap |
| `SLEEP_FRAMES` | 30 | Jumlah frame mata tertutup sebelum alarm kantuk |
| `YAWN_FRAMES` | 15 | Jumlah frame menguap sebelum alarm menguap |

## 🧠 Cara Kerja

### Eye Aspect Ratio (EAR)
- Menghitung rasio antara jarak vertikal dan horizontal mata
- EAR menurun ketika mata tertutup
- Formula: `EAR = (|p2-p6| + |p3-p5|) / (2 * |p1-p4|)`

### Mouth Aspect Ratio (MAR)
- Menghitung rasio antara tinggi dan lebar mulut
- MAR meningkat ketika mulut terbuka (menguap)
- Formula: `MAR = |mouth_top - mouth_bottom| / |mouth_left - mouth_right|`

### Algoritma Deteksi
1. **Face Mesh Detection**: Menggunakan MediaPipe untuk mendeteksi 468 landmark wajah
2. **Feature Extraction**: Mengekstrak koordinat mata dan mulut
3. **Ratio Calculation**: Menghitung EAR dan MAR
4. **Threshold Comparison**: Membandingkan dengan nilai ambang batas
5. **Frame Counting**: Menghitung frame berturut-turut yang memenuhi kondisi
6. **Alert Triggering**: Memberikan peringatan jika melebihi batas frame

## 📊 Landmark Points

### Mata Kiri: `[362, 385, 387, 263, 373, 380]`
### Mata Kanan: `[33, 160, 158, 133, 153, 144]`
### Mulut:
- Atas: `13`
- Bawah: `14`  
- Kiri: `78`
- Kanan: `308`

## 🎯 Aplikasi

- **Driver Monitoring**: Memantau kantuk pengemudi
- **Study Assistant**: Membantu menjaga fokus saat belajar
- **Work Productivity**: Mencegah kantuk saat bekerja
- **Health Monitoring**: Memantau pola tidur dan kelelahan

## 🔊 Audio Alerts

- **Kantuk**: Beep 1000 Hz selama 500ms
- **Menguap**: Beep 800 Hz selama 500ms

## 🚫 Troubleshooting

- **Kamera tidak terdeteksi**: Pastikan webcam terhubung dan tidak digunakan aplikasi lain
- **Deteksi tidak akurat**: Pastikan pencahayaan cukup dan wajah terlihat jelas
- **Audio tidak berfungsi**: Pastikan speaker/headphone terhubung (Windows only untuk winsound)

## 📝 Lisensi

Proyek ini dibuat untuk keperluan riset dan pembelajaran.

## 👨‍💻 Kontribusi

Kontribusi dan saran perbaikan sangat diterima! Silakan buat issue atau pull request.
