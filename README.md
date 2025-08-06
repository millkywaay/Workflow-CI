# Workflow-CI

Repositori ini berisi proyek machine learning untuk prediksi penyakit jantung, dilengkapi dengan workflow Continuous Integration (CI) untuk memastikan kualitas dan konsistensi kode.

## Daftar Isi

- [Deskripsi Proyek](#deskripsi-proyek)
- [Struktur Direktori](#struktur-direktori)
- [Persiapan Lingkungan](#persiapan-lingkungan)
- [Menjalankan Proyek](#menjalankan-proyek)
- [Testing](#testing)
- [Continuous Integration (CI)](#continuous-integration-ci)


---

## Deskripsi Proyek

Proyek ini bertujuan untuk membangun sistem machine learning yang dapat memprediksi penyakit jantung berdasarkan data yang telah diproses. Proses preprocessing dan modelling dilakukan menggunakan Python, dengan dependensi yang dikelola melalui Conda dan pip.

## Struktur Direktori

```
MLProject/
├── conda.yaml
├── heart_disease_preprocessing/
│   ├── test_processed.csv
│   └── train_processed.csv
├── MLproject
├── modelling.py
└── requirements.txt
```

- `conda.yaml` : Spesifikasi environment Conda.
- `heart_disease_preprocessing/` : Folder berisi data hasil preprocessing.
- `MLproject` : File konfigurasi MLflow Project.
- `modelling.py` : Script utama untuk training dan evaluasi model.
- `requirements.txt` : Daftar dependensi Python.

## Persiapan Lingkungan

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/username/Workflow-CI.git
   cd Workflow-CI/MLProject
   ```

2. **Buat environment Conda:**
   ```bash
   conda env create -f conda.yaml
   conda activate workflow-ci
   ```

3. **Install dependensi tambahan (jika ada):**
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Proyek

Jalankan script modelling:
```bash
python modelling.py
```

Atau, jika menggunakan MLflow:
```bash
mlflow run .
```

## Testing

Pastikan Anda sudah menyiapkan data di folder `heart_disease_preprocessing/`. Untuk pengujian, Anda bisa menambahkan script test sesuai kebutuhan.

## Continuous Integration (CI)

Repositori ini dirancang untuk mendukung workflow CI, misalnya dengan GitHub Actions. CI akan secara otomatis menjalankan linting, testing, dan build setiap kali ada perubahan kode, sehingga kualitas kode tetap terjaga.
