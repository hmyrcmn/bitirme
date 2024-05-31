

![Proje Logo](https://cdn-images-1.medium.com/max/1200/1*qa1QXLhPeFNexxwIoz9Sgg.jpeg)
# 1.1 Veri Toplama Yöntemleri

Proje kapsamında kullanılan veriler, iki farklı kaynaktan elde edilmiştir bunlar startup bilgileri ve CV verileri, json fromatına dönüştürülüne bu veriler githubda startup.json dosyasına kaydedildi ve cv.json dosyalarına veri arttırma işlemi uygulanmış ve modele hazır hale getirildi .

#### 1.1.1 Startup Verilerinin Toplanması

Startup verileri, [EU-Startups]([link](https://www.eu-startups.com/directory/)) sitesinden elde edilmiştir. Scrapy adlı web kazıma kütüphanesi kullanılarak belirlenen URL'lerden veriler çekilmiş ve JSON formatında kaydedilmiştir. Starups.py file ile toplanan veriler startup.json da saklanmıştır.

#### 1.1.2 CV Verilerinin Toplanması

CV verileri, belirli bir formatta düzenlenmiş ve JSON dosyalarına dönüştürülmüştür. Bu veriler, çeşitli kaynaklardan manuel veya otomatik olarak toplanmış ve belirli bir formata dönüştürülmüştür.cv.json dosyasında saklanmıştır.

## 2. Model Eğitimi ve Değerlendirme Yöntemleri
![Proje Logo](https://cdn-images-1.medium.com/max/1200/1*mKmre9aQoAOdsTzbHnXCRA.jpeg)
Json formatına dönüştürülen veriler Bert (google nin ) dil modelinde verildi ve ilgili json verileri bert modeli ile vektörleştirildi ve bu vektörler sayısal vektörleşme uygulandı tüm verilere kosinus benzerliği uygulandı bu uygulama sonrasında elde edilen skor her firma için en uygun cv ye sahip kişinin adını ve yüzde üzerinden uygunluk değerine ait skor değerini çıktı olarak almaktayız. 
Eğitim sırasınd 2 farklı yöntem uygulanmıştır bunları model-1 ve model -2 olarak isimlendirdim.
# modelin diagramla gösterimi


![Proje Logo](https://cdn-images-1.medium.com/max/1200/1*8OJyM3xMxCalgwlpPzvxPQ.png)
#### Model 1:

BERT modelinin son katmanından (last_hidden_state) elde edilen çıktının ortalamasını kullanır.
Bu, BERT modelinin tüm çıktılarını tek bir vektörde toplamak anlamına gelir.
Kodda: outputs.last_hidden_state.mean(dim=1).detach().numpy()
#### Model 2:

BERT modelinin belirli bir katmanından (örneğin 11. katman) elde edilen çıktının ortalamasını kullanır.
Belirli bir katman seçerek, modelin farklı seviyelerdeki özelliklerini kullanabilirsiniz.
Kodda: outputs.hidden_states[layer_num].mean(dim=1).detach().numpy()
# modelde kulllanılan kosinus benzerliğinin detaylı gösterimi

![Proje Logo](https://cdn-images-1.medium.com/max/1200/1*8OJyM3xMxCalgwlpPzvxPQ.png)
## 3. Kullanım
1. GOOGLE COLAB da ilgili dosyayı açın ve verilerinizi uygun formatta oluşturun ve düzenleyin ve modele bu verileri sunun çıktıları görütüleyin .
## 4. Model 2 nin Sonuçları 
![Proje Logo](https://cdn-images-1.medium.com/max/1200/1*FLBnhkdkLluJmn8pTeWYkQ.png)
Bu tabloda selin öztürk cvsine firmaların uygunluklarını belirten skorlar yer almaktadır.
