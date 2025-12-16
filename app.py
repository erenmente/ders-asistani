from flask import Flask, render_template, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv

# 1. AYARLARI YÜKLE
load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("GROQ_API_KEY")

# Groq İstemcisini Başlat
if not API_KEY:
    print("⚠️ API Anahtarı bulunamadı!")
    client = None
else:
    client = Groq(api_key=API_KEY)

# --- SİSTEM TALİMATLARI ---
ALGO_PROMPT = """
Sen Fırat Üniversitesi Yazılım Mühendisliği bölümünde bir Algoritma Mentorüsün (Java Uzmanı).
Görevin: Öğrenciye asla direkt kodu kopyala-yapıştır yapabileceği şekilde verme.
Önce mantığı anlat, pseudocode (sözde kod) göster, ipuçları ver.
Clean Code prensiplerine sadık kal.
Cevaplarında bol bol emoji kullan ve samimi, motive edici bir dil kullan.
"""

BBG_PROMPT = """
Sen Bilgisayar Bilimleri dersi veren kıdemli bir Akademisyensin.
Görevin: Konuları (Binary sistemler, CPU mimarisi, Bellek yönetimi vb.) mühendislik formasyonuyla anlatmak.
Günlük hayattan analojiler ve metaforlar kullan.
Ciddi ama anlaşılır bir dil kullan.
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sor', methods=['POST'])
def sor():
    try:
        if not client:
            return jsonify({'response': "Sunucu Hatası: API Anahtarı eksik."})

        data = request.json
        user_input = data.get('message')
        mode = data.get('mode') 

        if not user_input:
            return jsonify({'response': "Boş mesaj."})

        system_content = ALGO_PROMPT if mode == 'algo' else BBG_PROMPT

        # --- GÜNCELLENMİŞ MODEL ---
        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_content
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            # GÜNCEL MODEL İSMİ BURADA:
            model="llama-3.3-70b-versatile", 
            temperature=0.7,
        )

        ai_response = completion.choices[0].message.content
        
        return jsonify({'response': ai_response})

    except Exception as e:
        error_msg = str(e)
        print(f"❌ Groq Hatası: {error_msg}")
        return jsonify({'response': f"Bağlantı Hatası: {error_msg}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)