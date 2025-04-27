# Resmi Python imajını kullan
FROM python:3.12.4

# Çalışma dizinini belirle
WORKDIR /app

# Bağımlılıkları yükle (Eğer "requirements.txt" varsa)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Uygulamanın çalıştırılma komutu
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]


