from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
import time
from dotenv import load_dotenv

# 1. AYARLARI YÜKLE
load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ HATA: API Anahtarı bulunamadı!")
else:
    genai.configure(api_key=API_KEY)

# --- SİSTEM TALİMATLARI ---
ALGO_PROMPT = """
ROL: Fırat Üniversitesi Yazılım Müh. Algoritma Mentorü (Java Uzmanı).
GÖREV: Asla direkt kod verme. Önce mantığı anlat. Clean Code kullan.
"""

BBG_PROMPT = """
ROL: Bilgisayar Bilimleri Akademisyeni.
GÖREV: Konuları mühendislik formasyonuyla, derinlemesine ve analojilerle anlat.
"""

# --- MODEL LİSTESİ (STRATEJİK SIRALAMA) ---
# 1. 'gemini-flash-latest': En güvenli liman. Google senin için en boş sunucuyu seçer.
# 2. 'gemini-2.0-flash': Standart sürüm.
# 3. 'gemini-2.0-flash-lite-preview...': Az önce kullandığımız (Yedek)
MODEL_LIST = [
    'gemini-flash-latest',       # <-- JOKER (En Yüksek Öncelik)
    'gemini-2.0-flash',          # <-- Standart
    'gemini-2.0-flash-exp',      # <-- Hızlı
    'gemini-2.0-flash-lite-preview-02-05' 
]

active_models = {}

def get_working_chat_session(mode):
    """Sırayla modelleri dener, çalışan ilkini döndürür."""
    global active_models
    
    if mode in active_models:
        return active_models[mode]

    print(f"🕵️‍♂️ '{mode}' için en uygun model aranıyor...")
    
    for model_name in MODEL_LIST:
        try:
            print(f"👉 Deneniyor: {model_name}...")
            instruction = ALGO_PROMPT if mode == 'algo' else BBG_PROMPT
            model = genai.GenerativeModel(model_name, system_instruction=instruction)
            
            # Test atışı
            chat = model.start_chat(history=[])
            
            active_models[mode] = chat
            print(f"✅ BAŞARILI! '{model_name}' devreye alındı.")
            return chat
            
        except Exception as e:
            print(f"❌ {model_name} pas geçildi: {e}")
            continue

    raise Exception("Tüm modeller meşgul veya kotası dolu.")

# --- ROTALAR ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sor', methods=['POST'])
def sor():
    try:
        data = request.json
        user_input = data.get('message')
        mode = data.get('mode') 

        if not user_input:
            return jsonify({'response': "Boş mesaj."})

        # --- RETRY (TEKRAR DENEME) MEKANİZMASI ---
        # Hata alırsak 5 saniye bekleyip tekrar deniyoruz (Toplam 3 hak)
        max_retries = 3
        
        for i in range(max_retries):
            try:
                # 1. Aktif sohbeti al (veya yenisini bul)
                active_chat = get_working_chat_session(mode)
                
                # 2. Mesajı gönder
                response = active_chat.send_message(user_input)
                return jsonify({'response': response.text})

            except Exception as e:
                error_msg = str(e)
                print(f"⚠️ Deneme {i+1}/{max_retries} Başarısız: {error_msg}")
                
                # Model hatası varsa hafızadan sil ki bir sonraki turda yenisini seçsin
                if mode in active_models:
                    del active_models[mode]
                
                # Son hak değilse bekle
                if i < max_retries - 1:
                    time.sleep(4) # Bekleme süresini 4 saniyeye çıkardım
                else:
                    return jsonify({'response': "⚠️ Sunucular şu an aşırı yoğun. Lütfen 30 saniye bekleyip tekrar dene."})

    except Exception as e:
        return jsonify({'response': f"Sistem hatası: {str(e)}"})

@app.route('/temizle', methods=['POST'])
def temizle():
    global active_models
    active_models = {}
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)