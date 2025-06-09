# Gunakan base image Python
FROM python:3.10-slim

# Buat working directory di dalam container
WORKDIR /app

# Salin file requirements dan install dependensi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh project ke dalam container
COPY . .

# Expose port Flask (5000)
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "app.py"]