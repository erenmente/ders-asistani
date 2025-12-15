import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Ayarları Yükle
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ .env dosyasında API Key bulunamadı!")
    exit()

genai.configure(api_key=api_key)

print("="*50)
print("📡 HESABINA TANIMLI OLAN MODELLER (LİSTE)")
print("="*50)

try:
    bulunan_modeller = []
    for m in genai.list_models():
        # Sadece "metin üretme" yeteneği olan modelleri filtrele
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ {m.name}")
            bulunan_modeller.append(m.name)
            
    print("="*50)
    
    if not bulunan_modeller:
        print("❌ HİÇBİR MODEL BULUNAMADI! API Anahtarın hatalı veya erişimi yok.")
    else:
        print("👆 Yukarıdaki listeden başında 'models/' olan bir tanesini seçip app.py'ye yazacağız.")

except Exception as e:
    print(f"❌ BAĞLANTI HATASI: {e}")