

![Proje Logo](https://cdn-images-1.medium.com/max/1200/1*qa1QXLhPeFNexxwIoz9Sgg.jpeg)
# Veri İşleme ve Modelleme

Bu proje, çeşitli kaynaklardan elde edilen verileri işleyerek ve BERT modelini kullanarak startup bilgileri ile CV verileri arasındaki uyumu belirlemek için tasarlanmıştır.

## 1. Araştırma Süreci

### 1.1 Veri Toplama Yöntemleri

Proje kapsamında kullanılan veriler, iki ana kaynaktan elde edilmiştir: startup bilgileri ve CV verileri.

#### 1.1.1 Startup Verilerinin Toplanması

Startup verileri, [EU-Startups]([link](https://www.eu-startups.com/directory/)) sitesinden elde edilmiştir. Scrapy adlı web kazıma kütüphanesi kullanılarak belirlenen URL'lerden veriler çekilmiş ve JSON formatında kaydedilmiştir. Starups.py file ile toplanan veriler startup.json da saklanmıştır.

#### 1.1.2 CV Verilerinin Toplanması

CV verileri, belirli bir formatta düzenlenmiş ve JSON dosyalarına dönüştürülmüştür. Bu veriler, çeşitli kaynaklardan manuel veya otomatik olarak toplanmış ve belirli bir formata dönüştürülmüştür.cv.json dosyasında saklanmıştır.

### 1.2 Veri Temizleme ve Düzenleme

Elde edilen veriler, gereksiz bilgilerden arındırılarak ve doğru formatta düzenlenerek temizlenmiştir.

### 1.3 Veri Analizi ve Görselleştirme

Veri toplama sürecinin ardından elde edilen veriler analiz edilmiş ve model geliştirme aşamasına geçilmiştir.

## 2. Model Eğitimi ve Değerlendirme Yöntemleri
![Proje Logo](https://cdn-images-1.medium.com/max/1200/1*mKmre9aQoAOdsTzbHnXCRA.jpeg)

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



![Project Logo](https://cdn-images-1.medium.com/max/1200/1*qa1QXLhPeFNexxwIoz9Sgg.jpeg)
# Data Processing and Modeling

This project is designed to determine the compatibility between startup data and CV data by processing data obtained from various sources and using the BERT model.

## 1. Research Process

### 1.1 Data Collection Methods

The data used in the project was obtained from two main sources: startup data and CV data.

#### 1.1.1 Collection of Startup Data

Startup data was obtained from [EU-Startups](https://www.eu-startups.com/directory/) website. Data was extracted from the specified URLs using the Scrapy web scraping library and saved in JSON format. The data collected using the startups.py file is stored in the startup.json file.

#### 1.1.2 Collection of CV Data

CV data was formatted and converted to JSON files. These data were collected manually or automatically from various sources and converted to a specific format. The collected data is stored in the cv.json file.

### 1.2 Data Cleaning and Editing

The obtained data was cleaned by removing unnecessary information and edited to the correct format.

### 1.3 Data Analysis and Visualization

After the data collection process, the obtained data was analyzed, and the model development stage was initiated.

## 2. Model Training and Evaluation Methods
![Project Logo](https://cdn-images-1.medium.com/max/1200/1*mKmre9aQoAOdsTzbHnXCRA.jpeg)

### 2.1 Use of BERT Model

The BERT model was used to determine the compatibility between startups and mentor CVs. The BERT model and tokenizer were used to convert text data into feature vectors.

#### Model 1: outputs.last_hidden_state

This model extracts from BERT's last layer. The last layer can represent the overall meaning of the text best and encode the most advanced features learned during the model's learning process.

#### Model 2: outputs.hidden_states[layer_num]

In this model, inference is made from a specified layer. Using intermediate layers may help capture more specific or detailed features.

### 2.2 Processing Feature Vectors

The output of the BERT model is converted into feature vectors representing the meaning of the texts. These vectors are compared using cosine similarity to find the most suitable CV.

## 3. Usage

1. Run the `process_json_with_bert.py` file to process JSON data.
2. Specify the JSON data to be processed.
3. View the outputs on the console or in a file.
4. Open the relevant file in GOOGLE COLAB, create and edit your data in the appropriate format, and present this data to the model to view the outputs.

## 4. Contribution

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Create a pull request!

## 5. License

This project is licensed under the MIT License.

---

This README file explains the purpose, methods, usage, contribution process, and license information of the project.

