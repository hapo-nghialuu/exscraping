import scrapy

class NiftySpider(scrapy.Spider):
    name = 'nifty'
    start_urls = [
        'https://myhome.nifty.com/chuko-mansion/osaka/osakashimiyakojimaku_ct/?subtype=buc&pnum=40',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

    def parse(self, response):
        for div in response.css('div.card.is-bg-light.is-floating-shadow.is-radius-lg.is-overflow-hidden'):
            h2_text = div.css('h2 a::text').get()
            if h2_text:
                print(h2_text)
