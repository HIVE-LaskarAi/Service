# API Klasifikasi Hama Tanaman Padi

API ini digunakan untuk mengklasifikasi jenis hama atau penyakit pada tanaman padi berdasarkan input gambar. Model deep learning yang digunakan telah dilatih untuk mengenali berbagai jenis hama/penyakit.

## Fitur

- Endpoint RESTful /api/predict untuk klasifikasi gambar.
- Dokumentasi Swagger tersedia di /apidocs.
- Model klasifikasi berbasis CNN/MobileNet (TensorFlow).

## Struktur Direktori

```
Service/
│
├── app.py
├── Dockerfile
├── controllers/
│   └── rice_controller.py
├── routes/
│   └── rice_route.py
├── models/
│   └── hive_disease_model.h5
└── requirements.txt
```

## Cara Menjalankan API

### 1. Jalankan di Localhost (Tanpa Docker)

Langkah-langkah:

- Buat virtual environment (opsional):
  ```
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate     # Windows
  ```
- Install dependencies:
  ```
  pip install -r requirements.txt
  ```
- Jalankan aplikasi:
  ```
  python app.py
  ```

### 2. Jalankan Menggunakan Docker (di Local atau VPS)

Langkah-langkah:

- Build image Docker:
  ```
  docker build -t rice-pest-api .
  ```
- Jalankan container:
  ```
  docker run -d -p 5000:5000 --name rice-api rice-pest-api
  ```

### 3. Akses

- Local
  ```
  API: http://localhost:5000/api/predict
  Swagger Docs: http://localhost:5000/apidocs
  ```
- VPS
  ```
  API: http://<ip-vps>:5000/api/predict
  Swagger Docs: http://<ip-vps>:5000/apidocs
  ```

## Cara Menggunakan Endpoint

- Method: POST
- URL: /api/predict
- Content-Type: multipart/form-data
- Parameter:
  - file: File gambar (.png/.jpg/.jpeg)
- Contoh Curl Request:
  ```
  curl -X POST http://localhost:5000/api/predict \
    -F "file=@contoh_gambar.jpg"
  ```
- Response Sukses:
  ```
  {
  "predicted_class": "blast",
  "confidence": 94.58
  }
  ```

## Catatan Tambahan

- Pastikan file model hive_disease_model.h5 berada di folder models/.
- Ekstensi file yang didukung: .png, .jpg, .jpeg.
- API akan memberikan error 400 jika file tidak valid atau tidak ditemukan.
