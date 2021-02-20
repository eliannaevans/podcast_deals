import scrapy
from scrapy.crawler import CrawlerProcess

class PodcastSpider(scrapy.Spider):
    name = 'podcast_spider'
    
    def start_requests(self):
        urls=['https://podcasts.google.com/search/rich%20roll'] # start with podcast with known sponsors
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_main)
            
    def parse_main(self, response):
        website_body = response.xpath('/html/body/c-wiz[2]')
        episode_links = response.css('a.jJ8Epb::attr(href)').extract()
        
        for link in episode_links:
            yield response.follow(url=link, callback=self.parse_episodes)
            
    def parse_episodes(self, response):
        pass
