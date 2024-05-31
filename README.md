# Proje Adı

Proje Açıklaması: Bu proje, startup'lar ile mentor CV'leri arasındaki uyumu belirlemek için BERT modelini kullanır.

## Kurulum

1. Python'u yükleyin: [Python](https://www.python.org/downloads/)
2. Gerekli kütüphaneleri yükleyin:


## Kullanım

1. `bert_similarity.py` dosyasını çalıştırarak benzerlik analizini yapabilirsiniz.
2. İlgili verileri ve ayarları dosyaya girdi olarak sağlayın.
3. Çıktıları konsolda veya dosyada görebilirsiniz.

## Örnek Kod:

```python
from bert_similarity import BERTSimilarity

# Verileri ve ayarları yükle
startup_data = "startup.json"
cv_data = "cv.json"
settings = {"model_type": "bert-base-uncased", "max_length": 128}

# Benzerlik analizini yap
similarity_analyzer = BERTSimilarity(startup_data, cv_data, settings)
similarity_scores = similarity_analyzer.calculate_similarity()

# Sonuçları görüntüle
for startup, score in similarity_scores.items():
    print(f"{startup}: {score}")
