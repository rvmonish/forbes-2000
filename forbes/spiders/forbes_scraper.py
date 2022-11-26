import scrapy


class ForbesScraperSpider(scrapy.Spider):
    name = "forbes_scraper"
    allowed_domains = ["www.forbes.com"]
    start_urls = ["https://www.forbes.com/lists/global2000/?sh=7215a7835ac0"]

    def parse(self, response):
        for item in response.css("div.table-row-group a"):
            yield {
                "rank": item.css("div.rank.first.table-cell.rank::text").get(),
                "organisation_name": item.css(
                    "div.organizationName.second.table-cell.name::text"
                ).get(),
                "country_name": item.css("div.country.table-cell.country::text").get(),
                "revenue": item.css("div.revenue.table-cell.sales::text").get(),
                "profit": item.css("div.profits.table-cell.profit::text").get(),
                "asset": item.css("div.assets.table-cell.assets::text").get(),
                "market_value": item.css(
                    "div.marketValue.table-cell.market.value::text"
                ).get(),
                "link": item.css("a::attr(href)").get(),
            }
        pass
