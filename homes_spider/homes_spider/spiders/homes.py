import scrapy


class HomesSpider(scrapy.Spider):
    name = 'homes'
    start_urls = [
        'https://www.homes.co.jp/archive/list/tokyo/chiyoda-city/nrg7VExr9efKjuqghS1a9Q-addr/',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            })


    def parse(self, response):
        # Lặp qua tất cả các thẻ <div> có class `lg:mb-6 my-4`
        for index, div in enumerate(response.css('div.lg\\:mb-6.my-4')):
            # Lấy nội dung text của thẻ <h2> bên trong mỗi <div>
            h2_text = div.css('h2 > span::text').get()
            # Nối các dòng text và loại bỏ khoảng trắng thừa
            h2_text = " ".join(h2_text).strip()
            print(f"Index: {index}, H2 Content: {h2_text}")
