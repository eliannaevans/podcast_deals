import scrapy
from scrapy.crawler import CrawlerProcess

class PodcastSpider(scrapy.Spider):
    name = 'podcast_spider'
    
    def start_requests(self):
        urls=['placeholder.com'] # while a real site, this is a paceholder for podcast site(s)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_main)
            
    def parse_main(self, response):
        pass
