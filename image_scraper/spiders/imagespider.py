import scrapy
from ..items import ImageScraperItem

class ImagespiderSpider(scrapy.Spider):
    name = "imagespider"
    allowed_domains = ["caesaugu.com"]
    start_urls = ["https://caesaugu.com/hosthatch%e7%91%9e%e5%a3%ab%e8%8b%8f%e9%bb%8e%e4%b8%96vps%e6%b5%8b%e8%af%84"]

    def parse(self, response):
        item = ImageScraperItem()
        item['image_urls'] = response.css('img::attr(src)').getall()
        yield item
