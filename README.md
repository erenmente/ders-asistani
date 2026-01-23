# 🎓 Fırat Asistan (AI Ders Mentoru)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey)
![Groq AI](https://img.shields.io/badge/Groq-API-orange)
![Deploy](https://img.shields.io/badge/Deploy-Render-success)

**Fırat Asistan**, Yazılım Mühendisliği öğrencileri için tasarlanmış web tabanlı, özelleşmiş bir Yapay Zeka mentorudur. Sıradan sohbet botlarının aksine, **Bağlam Değiştirme (Context Switching)** yeteneklerine sahiptir; bu sayede programlama görevleri için **Kıdemli Java Mentoru** veya Bilgisayar Bilimleri temelleri için **Teorik Akademisyen** gibi davranabilir.

🔗 [Canlı Demoyu İncele](https://www.erenmente.com/firatasistan)

---

## 🚀 Temel Özellikler

### 🧠 Çift Modlu AI Kişiliği

* **☕ Algoritma Modu:** Kıdemli bir Java Geliştiricisi gibi davranır. Temiz Kod (Clean Code), algoritmalar ve pratik uygulamalara odaklanır. Doğrudan cevap vermek yerine öğrenciyi *Sokratik Yöntem* ile yönlendirir.
* **💾 Bilgisayar Bilimleri Modu:** Akademik bir Profesör gibi davranır. Teorik konulara (İkili sistemler, CPU mimarisi, bellek yönetimi vb.) mühendislik analojileriyle odaklanır.

### 🎨 Modern Arayüz Deneyimi

* **ChatGPT Benzeri Arayüz:** Sohbet geçmişi kenar çubuğu ile temiz ve duyarlı tasarım.
* **Yerel Geçmiş:** Sohbet oturumlarını tarayıcının **LocalStorage** alanında güvenli bir şekilde saklar (Harici veritabanı gerektirmez).
* **Sözdizimi Vurgulama:** `highlight.js` kullanarak kod bloklarını (Java, Python vb.) otomatik olarak biçimlendirir ve renklendirir.
* **Markdown Desteği:** `marked.js` kullanarak zengin metni (kalın, listeler, başlıklar) işler.

---

## 🛠️ Teknoloji Yığını

* **Backend:** Python, Flask
* **AI Motoru:** groq API
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
* **Kütüphaneler:** `python-dotenv`, `marked.js`, `highlight.js`
* **Dağıtım (Deployment):** Render (Bulut Barındırma)

---

## 📂 Proje Yapısı

```bash
Firat-Asistan/
│
├── static/              # CSS ve Görsel dosyaları
├── templates/
│   └── index.html       # Ana uygulama arayüzü
├── app.py               # Flask backend & AI mantığı
├── requirements.txt     # Python bağımlılıkları
├── .env                 # API Anahtarları (Depoya dahil edilmez)
└── README.md            # Proje dokümantasyonu
```

## ⚙️ Kurulum (Yerel Çalıştırma)

Bu projeyi kendi bilgisayarınızda çalıştırmak isterseniz:

### Depoyu Klonlayın

```bash
git clone https://github.com/erenmente/ders-asistan.git
cd ders-asistan
```

## 🤝 Katkıda Bulunma

Bu proje eğitim amaçlıdır. Fork'layıp geliştirmekten çekinmeyin!

1. Projeyi Fork'layın
2. Özellik Dalınızı (Feature Branch) Oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi Commit Edin (`git commit -m 'YeniOzellik Eklendi'`)
4. Dalınıza Push Edin (`git push origin feature/YeniOzellik`)
5. Bir Pull Request Açın

## 👤 Yazar

Eren Mente

Fırat Üniversitesi - Yazılım Mühendisliği Öğrencisi

GitHub: @erenmente
