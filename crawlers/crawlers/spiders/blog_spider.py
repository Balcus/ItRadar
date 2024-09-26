import scrapy #type: ignore
from urllib.parse import urlparse

class BaseSpider(scrapy.Spider):

    def parse(self, response) :
        article_links = response.css("a::attr(href)").getall()
        for link in article_links :
            if self.is_valid_article_link(link, response):
                yield response.follow(link, callback=self.parse_article)

    def parse_article(self, response):
        # This method should be overridden in each spider
        raise NotImplementedError("Subclasses must implement parse_article")

    def is_valid_article_link(self, link, response):
        bad_keywords = ["newsletter"]
        for keyword in bad_keywords:
            if keyword in link:
                return False
            
        if len(link) < 2 :
            return False
        
        domain = urlparse(response.url).netloc
        if domain in link or link.startswith("/") or not link.startswith("http"):
            return True
        
        return False
    

class DanLuuSpider(BaseSpider):
    name = "danluuspider"
    start_urls = [
        "https://danluu.com/"
    ]

    def parse_article(self, response):
        yield {
                "url": response.url,
                "title": response.css("strong::text").get(), 
                "content" : " ".join(response.css("main p::text, main h1::text, main h2::text, main h3::text, main h4::text,  main a::text").getall())

            }
        

class JvnsSpider(BaseSpider) :
    name = "jvnsspider"
    start_urls = [
        "https://jvns.ca/"
    ]

    def parse(self, response):
        article_links = response.css("tr.article-row a::attr(href)").getall()
        for link in article_links :
            if self.is_valid_article_link(link, response):
                yield response.follow(link, callback=self.parse_article)

    def parse_article(self, response):
        yield {
                "url": response.url,
                "title": response.css("h1.entry-title::text").get(),
                "content": " ".join(response.css("div.entry-content *::text").getall())
            }


class TwoalitySpider(BaseSpider):
    name = "2alityspider"
    start_urls = [
        "https://2ality.com/index.html"
    ]

    def parse(self, response):
        article_links = response.css("h3.post-item-title a::attr(href)").getall()
        for link in article_links:
            if self.is_valid_article_link(link, response):
                yield response.follow(link, callback=self.parse_article)

        pagination_links = response.css("a.page-nav-span")
        yield from response.follow_all(pagination_links, self.parse)

    def parse_article(self, response):
        yield {
            "url": response.url,
            "title": " ".join(response.css("div#page-core-content h1 ::text").getall()),
            "content": " ".join(response.css("div#page-core-content h1::text, div#page-core-content h2::text, div#page-core-content h3::text, div#page-core-content p::text, div#page-core-content ul::text, div#page-core-content a::text, div#page-core-content li::text").getall())
        }


class CleanCoderSpider(BaseSpider):
    name = "cleancoderspider"
    start_urls = [
        "https://blog.cleancoder.com/"
    ]

    def parse_article(self, response):
        yield {
            "url" : response.url,
            "title" : response.css("div.blog-post h1::text, div.blog-post h1 i::text").get(),
            "content" : " ".join(response.css("div.blog-post article *::text").getall())
        }


class PragmaticEngineerSpider(BaseSpider):
    name = "pragmaticengineerspider"
    start_urls = [
        "https://blog.pragmaticengineer.com/"
    ]

    def parse(self, response):
        article_links = response.css("main#content a::attr(href)").getall()
        for link in article_links:
            if self.is_valid_article_link(link, response):
                yield response.follow(link, callback=self.parse_article)


    def parse_article(self, response):
        yield {
            "url" : response.url,
            "title" : response.css("h1.post-title::text").get(),
            "content" : " ".join(response.css("section.post-content *::text").getall())
        }


class TechRadarSpider(BaseSpider):
    name = "techradarspider"
    start_urls = [
        "https://www.techradar.com/audio/news",
        "https://www.techradar.com/computing/news",
        "https://www.techradar.com/audio/headphones/earbuds-airpods/news",
        "https://www.techradar.com/health-fitness/news",
        "https://www.techradar.com/cameras/news",
        "https://www.techradar.com/health-fitness/fitness-trackers/news",
        "https://www.techradar.com/audio/headphones/news",
        "https://www.techradar.com/computing/laptops/news",
        "https://www.techradar.com/phones/news",
        "https://www.techradar.com/home/small-appliances/news",
        "https://www.techradar.com/health-fitness/smartwatches/news",
        "https://www.techradar.com/tablets/news",
        "https://www.techradar.com/home/news",
        "https://www.techradar.com/tablets/ipad/news",
        "https://www.techradar.com/home/smart-home/news",
        "https://www.techradar.com/televisions/news"
    ]

    def parse(self, response):
        article_links = response.css('a.article-link::attr(href)').getall()

        for link in article_links:
            if self.is_valid_article_link(link, response):
                yield response.follow(link, callback=self.parse_article)

        pagination_links = response.css('div.flexi-pagination a::attr(href)').getall()
        yield from response.follow_all(pagination_links, self.parse)

    def parse_article(self, response):
        yield {
            "url" : response.url,
            "title" : response.css("div.news-article h1::text").get(),
            "content" : " ".join(response.css("div#content p::text, div#content h1::text, div#content h2::text, div#content h3::text, div#content h4::text, div#content h5::text, div#content h6::text").getall())
        }

class ArsTehnnicaSpider(BaseSpider):
    name = "arsspider"
    start_urls = [
        "https://arstechnica.com/gadgets/"
    ]

    def parse(self, response):
        article_links = response.css('div.listing.listing-latest a.overlay::attr(href)').getall()

        for link in article_links:
            if self.is_valid_article_link(link, response):  
                yield response.follow(link, callback=self.parse_article)

        load_more_link = response.css("a.load-more::attr(href)").get()
        right_pagination_link = response.css("div.prev-next-links a.left::attr(href)").get()

        if load_more_link:
            yield response.follow(load_more_link, callback=self.parse)
        elif right_pagination_link:
            yield response.follow(right_pagination_link, callback=self.parse)

    def parse_article(self, response):
        yield {
            "url" : response.url,
            "title" : response.css("header.article-header h1::text").get(),
            "content" : " ".join(response.css("section.article-guts p::text").getall())
        }

class AlistApartSpider(BaseSpider):
    name = "a_list_apart_spider"
    start_urls = [
        "https://alistapart.com/articles/"
    ]

    def parse(self, response):
        article_links = response.css("h2.entry-title a::attr(href)").getall()

        for link in article_links:
            if self.is_valid_article_link(link, response):
                yield response.follow(link, callback=self.parse_article)

        prev_articles = response.css("div.nav-previous a::attr(href)").get()
        if prev_articles:
            yield response.follow(prev_articles, callback=self.parse)

    def parse_article(self, response):
        yield {
            "url": response.url,
            "title": response.css("h1.entry-title::text").get(),
            "content": " ".join(response.css(
                "div.entry-content p::text, "
                "div.entry-content h2::text, "
                "div.entry-content h3::text, "
                "div.entry-content ul li::text"
            ).getall())
        }

class HighScalabilitySpider(BaseSpider):
    name = "hsspider"
    start_urls = [
        "https://highscalability.com/page/2/"
    ]

    def parse(self, response):
        article_links = response.css("a.gh-card-link::attr(href)").getall()

        for link in article_links:
            if self.is_valid_article_link(link, response):
                yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        yield {
            "url" : response.url,
            "title" : response.css("h1::text").get(),
            "content" : " ".join(response.css("p::text").getall())
        }

        
class CssTricksSpider(BaseSpider):
    name = "css"
    start_urls = [
        "https://css-tricks.com/category/articles/"
    ]

    def parse(self, response):
        article_links = response.css("div.article-article h2 a::attr(href)").getall()

        for link in article_links:
            if self.is_valid_article_link(link, response):
                yield response.follow(link, self.parse_article)

        pagination_links = response.css('div.wp_page_numbers a::attr(href)').getall()
        yield from response.follow_all(pagination_links, self.parse)

    def parse_article(self, response):
        yield {
            "url" : response.url,
            "title" : response.css("header.mega-header h1::text").get(),
            "content" : " ".join(response.css("div.article-content *::text").getall())
        }