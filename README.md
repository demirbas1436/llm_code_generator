# llm_code_generator
Python ile LLM destekli kod üretme ve Kubernetes üzerinde deployment.

# 🚀 LLM Destekli Python Kod Üretici  

Bu proje, büyük dil modellerini (**LLM**) kullanarak verilen **prompt’a göre Python kodu ve başlık üretir**.  
Yerel çalıştırılabilir **Ollama modeli** kullanılarak yazıldı.

🚀 **Proje, Flask API ile entegre edilerek Docker ve Kubernetes üzerinde ölçeklenebilir hale getirilmiştir.**  

---

## **🛠 Gereksinimler**  
Bu projeyi çalıştırabilmek için aşağıdaki araçların sistemde yüklü olması gerekir:  

✅ **Python 3.9+** _(Proje, Python **3.12.4** sürümünde yazıldı.)_  
✅ **Flask** _(Web framework)_  
✅ **Docker** _(Container çalıştırmak için)_  
✅ **Kubernetes & Minikube** _(Projeyi Kubernetes ortamında çalıştırmak için)_  
✅ **Ollama** _(Yerel LLM modeli kullanmak için)_  

📌 Eğer bu araçlar sistemde yoksa, önce yüklenmelidir!  

---

## **📥 Kurulum**  
📌 **Projeyi GitHub’dan indirip çalıştırmak için:**  

```sh
git clone https://github.com/KULLANICI_ADIN/proje-adi.git
cd proje-adi
```

Bu komutlar, GitHub’daki kodu bilgisayara çeker ve proje klasörüne geçiş yapar.

✅ Python bağımlılıklarını yükle:
```sh
pip install -r requirements.txt

💡 Ollama Modelini Kurma ve Çalıştırma
📌 Yerel LLM modeli olan Ollama’yı yüklemek için:

```sh
curl -fsSL https://ollama.com/install.sh | sh
ollama pull mistral
ollama serve
✅ Bu komutlar Ollama’yı indirir ve çalıştırır.

📌 Eğer Ollama kurulu değilse, Flask uygulaması çalışmayacaktır!

🐳 Docker ile Çalıştırma
📌 Docker kullanarak projeyi çalıştırmak için:

```sh
docker build -t myapp .
docker run -p 5000:5000 myapp
✅ Bu komutlar, Docker imajını oluşturur ve Flask API’yi başlatır.
🚀 Şimdi tarayıcıda şu adresi açıp test edilebilir:
```sh
http://127.0.0.1:5000

☸️ Kubernetes Üzerinde Çalıştırma
📌 Kubernetes ortamında çalıştırmak için Minikube başlat:
```sh
minikube start
✅ Bu, Kubernetes’i yerel ortamda başlatır.

📌 Deployment ve servis dosyalarını çalıştır:
```sh
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

✅ Bu komutlar, Kubernetes podlarını ve servisini oluşturur.
📌 Çalışan podları kontrol et:
```sh
kubectl get pods

📌 Servis durumunu kontrol et:
```sh
kubectl get services

🌐 Minikube Servisini Açma ve Test Etme

📌 Minikube üzerinde servisin çalıştığını kontrol etmek için:
```sh
kubectl get services

✅ Eğer servisin EXTERNAL-IP kısmı <pending> görünüyorsa, Minikube tunnel başlatmalısın:
```sh
minikube tunnel
✅ Servise erişmek için Minikube’den URL al:(diğer terminalden çalıştırılır.)
```sh
minikube service flask-service --url

🚀 Çıkan URL’yi tarayıcıya yaz
