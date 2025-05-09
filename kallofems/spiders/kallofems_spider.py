import scrapy

class KalloFemSpider(scrapy.Spider):
    name = "kallofems" # Spider neve
    allowed_domains = ["kallofem.hu"]
    start_urls = ["https://kallofem.hu/shop/group/keriteselemek"]

    def start_requests(self):
        # Playwright használata a JavaScript által generált tartalomhoz
        for url in self.start_urls:
            # A Playwright-ot használó kérésekhez meta adatokat adunk meg
            # yield jelentése: a kérések generálása
            yield scrapy.Request(
                url,
                meta={"playwright": True},
                callback=self.parse
            )

    def parse(self, response):

        # 1. Debug a következő oldal URL-jéről
        next_page = response.xpath(
            '//ul[contains(@class,"pagination")]//a[text()="›"]/@href'
        ).get()
        self.logger.debug(f"Next page URL: {next_page!r}")

        # Termékek kinyerése
        for product in response.css('article.product-row'):
            name = product.css('h4::text').get()
            price = product.css('span.product-price::text').get()
            image = product.css('img::attr(src)').get()

            yield {
                'name': name.strip() if name else None,
                'price': price.strip() if price else None,
                'image_url': response.urljoin(image) if image else None,
            }

        # 3. Lapozás – explicit várakozással
        if next_page:
            yield response.follow(
                next_page,
                callback=self.parse,
                meta={
                    "playwright": True,
                    "playwright_page_methods": [
                        {
                            "method": "wait_for_selector",
                            "args": ["article.product-row"],
                            "kwargs": {"timeout": 10000},
                        }
                    ]
                }
            )

        """ Lapozás kezelése: a '›' gomb XPath-szelektorral
        next_page = response.xpath(
            '//ul[contains(@class,"pagination")]//a[text()="›"]/@href'
        ).get()
        if next_page:
            yield response.follow(
                next_page,
                callback=self.parse,
                meta={"playwright": True}
            )"""
