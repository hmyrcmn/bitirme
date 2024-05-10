import scrapy

class StartupsSpider(scrapy.Spider):
    name = "startups"
    allowed_domains = ["eu-startups.com"]
    start_urls = ["https://www.eu-startups.com/directory/"]

    def parse(self, response):
        # Kategori listesini hedefle
        categories = response.xpath("//div[@id='wpbdp-categories']/ul/li")
        
        # Her kategori için link ve başlığı al
        for category in categories:
            link = category.xpath("./a/@href").get()
            title = category.xpath("./a/text()").get()
            
            # Kategorinin sayfasına giderek içeriği çek
            yield scrapy.Request(url=link, callback=self.parse_category, meta={'title': title})

    def parse_category(self, response):
        # Kategorinin sayfasındaki listeleme öğelerini hedefle
        listings = response.xpath("//div[@id='wpbdp-listings-list']//div[contains(@class, 'wpbdp-listing')]")
        
        # Her bir listeleme öğesi için değerleri al
        for listing in listings:
            yield {
                "title": response.meta['title'],
                "business_name": listing.xpath(".//div[contains(@class, 'wpbdp-field-business_name')]//div[@class='value']/a/text()").get(),
                "category": listing.xpath(".//div[contains(@class, 'wpbdp-field-category')]//div[@class='value']/a/text()").get(),
                "based_in": listing.xpath(".//div[contains(@class, 'wpbdp-field-based_in')]//div[@class='value']/text()").get(),
                "tags": listing.xpath(".//div[contains(@class, 'wpbdp-field-tags')]//div[@class='value']/text()").get(),
                "founded": listing.xpath(".//div[contains(@class, 'wpbdp-field-founded')]//div[@class='value']/text()").get()
            }
