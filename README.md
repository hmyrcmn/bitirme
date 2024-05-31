
![Proje Logo](https://www.bing.com/images/create/bunu-nlp-bert-modelinin-yaptc4b1c49fc4b1nc4b1-anlatarak-yap-re/1-6659ab9d731949da9c38027e953b6944?id=mKmre9aQoAOdsTzbHnXCRA%3d%3d&view=detailv2&idpp=genimg&thId=OIG3.8rHw03pW2DeWj8cCEIzj&FORM=GCRIDP&mode=overlay)

# Veri İşleme ve Modelleme

Bu proje, çeşitli kaynaklardan elde edilen verileri işleyerek ve BERT modelini kullanarak startup bilgileri ile CV verileri arasındaki uyumu belirlemek için tasarlanmıştır.

## 1. Araştırma Süreci

### 1.1 Veri Toplama Yöntemleri

Proje kapsamında kullanılan veriler, iki ana kaynaktan elde edilmiştir: startup bilgileri ve CV verileri.

#### 1.1.1 Startup Verilerinin Toplanması

Startup verileri, [EU-Startups]([link](https://www.eu-startups.com/directory/)) sitesinden elde edilmiştir. Scrapy adlı web kazıma kütüphanesi kullanılarak belirlenen URL'lerden veriler çekilmiş ve JSON formatında kaydedilmiştir.

#### 1.1.2 CV Verilerinin Toplanması

CV verileri, belirli bir formatta düzenlenmiş ve JSON dosyalarına dönüştürülmüştür. Bu veriler, çeşitli kaynaklardan manuel veya otomatik olarak toplanmış ve belirli bir formata dönüştürülmüştür.

### 1.2 Veri Temizleme ve Düzenleme

Elde edilen veriler, gereksiz bilgilerden arındırılarak ve doğru formatta düzenlenerek temizlenmiştir.

### 1.3 Veri Analizi ve Görselleştirme

Veri toplama sürecinin ardından elde edilen veriler analiz edilmiş ve model geliştirme aşamasına geçilmiştir.

## 2. Model Eğitimi ve Değerlendirme Yöntemleri

### 2.1 BERT Modeli Kullanımı

Startup'lar ve mentor CV'leri arasındaki uyumu belirlemek için BERT modeli kullanılmıştır. BERT modeli ve tokenizer'ı, metin verilerini özellik vektörlerine dönüştürmek için kullanılmıştır.

#### Model 1: outputs.last_hidden_state

Bu model, BERT'in son katmanından çıkarım yapar. Son katman, metnin genel anlamını en iyi şekilde temsil edebilir ve modelin öğrenme sürecinde edindiği en üst düzeydeki özellikleri kodlar.

#### Model 2: outputs.hidden_states[layer_num]

Bu modelde ise belirtilen bir katmandan çıkarım yapılır. Orta katmanlardan birinin kullanılması, daha spesifik veya ayrıntılı özelliklerin yakalanmasına yardımcı olabilir.

### 2.2 Özellik Vektörlerinin İşlenmesi

BERT modelinin çıktısı, metinlerin anlamını temsil eden özellik vektörlerine dönüştürülür. Bu vektörler, cosine similarity yöntemiyle karşılaştırılarak en uygun CV'nin bulunmasında kullanılır.

## 3. Kullanım

1. `process_json_with_bert.py` dosyasını çalıştırarak JSON verilerini işleyebilirsiniz.
2. İşlenecek JSON verilerini belirtin.
3. Çıktıları konsolda veya dosyada görebilirsiniz.
4. GOOGLE COLAB da ilgili dosyayı açın ve verilerinizi uygun formatta oluşturun ve düzenleyin ve modele bu verileri sunun çıktıları görütüleyin .
## 4. Katkıda Bulunma

1. Fork'layın.
2. Yeni bir branch oluşturun.
3. Değişikliklerinizi commit edin.
4. Branch'ı pushlayın.
5. Pull request oluşturun!

## 5. Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

---

Bu README dosyası, projenin amacını, yöntemlerini, kullanımını, katkıda bulunma sürecini ve lisans bilgisini açıklar.
