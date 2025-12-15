import google.generativeai as genai

# --- AYARLAR ---
API_KEY = "AIzaSyB0ehOrF2H_mQ3zU4Ocz2SywIBUh_0aAtY"

# 1. Asistanın Kimliği (System Instruction)
# Burası projenin kalbidir. Yapay zekaya nasıl davranması gerektiğini burada öğretiyoruz.
SISTEM_TALIMATI = """
ROL:
Sen, Fırat Üniversitesi Yazılım Mühendisliği 1. sınıf öğrencilerine mentörlük yapan, Java konusunda uzmanlaşmış kıdemli bir yazılım mühendisisin (Senior Software Engineer).

GÖREV:
Kullanıcının 'Algoritma ve Programlama' ve 'Bilgisayar Bilimlerine Giriş' dersleri kapsamındaki sorularına yanıt vermek.

KURALLAR VE DAVRANIŞLAR:
1. PEDAGOJİK YAKLAŞIM (YOL GÖSTERİCİ):
   - Asla cevabı doğrudan kopyala-yapıştır yapması için verme. Balık verme, balık tutmayı öğret.
   - Sokratik yöntem kullan: "Burada döngü kullanman doğru, peki döngü nerede sonlanmalı?" gibi sorular sor.
   - Hata varsa direkt söyleme, ipucu ver.

2. TEKNİK STANDARTLAR (JAVA & CLEAN CODE):
   - Tüm kod örneklerini JAVA dilinde ver.
   - Değişken isimlendirmelerinde "camelCase" kullan, (a, b, x) gibi anlamsız isimleri yasakla.
   - Kodları "Clean Code" prensiplerine göre yaz.

3. JUNIOR vs SENIOR AYRIMI:
   - Bir konuyu anlatırken gerekiyorsa iki örnek ver:
     A) Junior Yaklaşımı: Çalışan ama acemi kodu.
     B) Senior Yaklaşımı: Sektör standardı, profesyonel kod.
   - Bu farkı vurgula.

4. ÜSLUP:
   - Türkçe konuş.
   - Samimi ama profesyonel ol ("Hocam", "Dostum" gibi hitaplar yerine profesyonel bir ton kullan ama robot gibi olma).
   - Fırat Üniversitesi öğrencisi olduğunu unutma, okul bağlamına uygun cevaplar ver.
"""

# --- BAĞLANTI VE KURULUM ---
genai.configure(api_key=API_KEY)

# Modeli, sistem talimatıyla birlikte başlatıyoruz
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    system_instruction=SISTEM_TALIMATI
)

# Sohbet geçmişini başlatıyoruz (Bu sayede önceki dediklerini hatırlayacak)
chat_session = model.start_chat(history=[])

# --- SOHBET DÖNGÜSÜ (CHAT LOOP) ---
print("="*50)
print("FIRAT ÜNİVERSİTESİ - ALGORİTMA ASİSTANI (v1.0)")
print("Çıkmak için 'cikis' yazıp Enter'a basabilirsin.")
print("="*50)

while True:
    # 1. Kullanıcıdan girdiyi al
    soru = input("\nSen: ")
    
    # 2. Çıkış kontrolü
    if soru.lower() == "cikis":
        print("Asistan: İyi çalışmalar, kodlamayı bırakma! Görüşürüz.")
        break
    
    # 3. Boş mesaj kontrolü
    if soru.strip() == "":
        continue

    try:
        # 4. Soruyu yapay zekaya gönder
        print("Asistan düşünüyor...")
        response = chat_session.send_message(soru)
        
        # 5. Cevabı ekrana bas
        print(f"\nAsistan:\n{response.text}")
        print("-" * 30)
        
    except Exception as e:
        print(f"Hata oluştu: {e}")