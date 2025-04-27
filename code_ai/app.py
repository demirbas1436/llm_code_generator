from flask import Flask, request, render_template
import requests
import json
import re

app = Flask(__name__)

# Ollama API Endpoint
OLLAMA_API_URL = "http://host.docker.internal:11434/api/generate"


class Job:
    def __init__(self, prompt):
        self.prompt = prompt
        self.output = {
            "detail": "",
            "compact": "",
            "video": "",
            "title": ""
        }
        self.score = 0

    def generate_title(self):
        """Prompt’a dayalı bir başlık üretir."""
        prompt_lower = self.prompt.lower()
        title = "Python'da Akıllı Kod Üretimi"

        if "toplama" in prompt_lower or "iki sayıyı topla" in prompt_lower:
            title = "Basit Hesaplama Sistemi: Python’da Toplama"
        elif "döngü" in prompt_lower or "for" in prompt_lower or "while" in prompt_lower:
            title = "Döngülerle Akıllı Veri İşleme"
        elif "koşul" in prompt_lower or "if" in prompt_lower:
            title = "Karar Mekanizmaları: Python’da Koşullar"
        elif "dosya" in prompt_lower or "okuma" in prompt_lower or "write" in prompt_lower:
            title = "Veri Yönetimi: Python'da Dosya İşlemleri"
        elif "liste" in prompt_lower or "array" in prompt_lower:
            title = "Veri Yapıları: Python'da Liste Kullanımı"
        elif "fonksiyon" in prompt_lower or "def" in prompt_lower:
            title = "Modüler Programlama: Fonksiyonlarla Çalışma"
        else:
            title = f"{self.prompt} için Python Çözümü"

        self.output["title"] = title

    def run(self):
        """Yapay zekâ ile kod üretimini gerçekleştir."""
        data = {
            "model": "deepseek-r1:8b",
            "prompt": f"Python kodu üret. Açıklama ekleme. Sadece çalışabilir bir kod bloğu ver. Kod formatı: ```python ... ```\n{self.prompt}"
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(OLLAMA_API_URL, headers=headers, json=data, stream=True)

        if response.status_code == 200:
            complete_response = ""
            for line in response.iter_lines():
                if line:
                    json_line = json.loads(line.decode('utf-8'))
                    complete_response += json_line.get("response", "")

            self.output["detail"] = complete_response
            self.output["compact"] = self.extract_python(complete_response)
        else:
            self.output["detail"] = f"Hata: {response.status_code} - {response.text}"

    def extract_python(self, response_text):
        """Yanıttan yalnızca Python kod bloğunu çıkarır."""
        match = re.search(r"```python(.*?)```", response_text, re.DOTALL)
        return match.group(1).strip() if match else "Kod bloğu bulunamadı!"

    def calculate_score(self):
        """Kodun karmaşıklığına dayalı akıllı puanlama."""

        python_code = self.output["compact"]
        if "def " in python_code or "class " in python_code:
            self.score += 4  # Fonksiyon veya sınıf varsa ekstra puan

        if "for " in python_code or "while " in python_code:
            self.score += 3  # Döngü kullanımı varsa ekstra puan

        if "if " in python_code:
            self.score += 2  # Karar yapısı varsa ekstra puan

        if "import " in python_code:
            self.score += 1  # Harici modül kullanımı varsa ekstra puan

        if self.score == 0:
            self.score = 1  # Kod tamamen basitse en düşük puan

        # Skoru 10 ile sınırla
        self.score = min(self.score, 10)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form.get("prompt")
    if not prompt:
        return render_template("index.html", result="Lütfen bir kod türü girin!")

    job = Job(prompt)
    job.run()
    job.calculate_score()

    return render_template("index.html", result=f"<pre>{job.output['compact']}</pre>", score=job.score)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

