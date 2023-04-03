from datetime import datetime
import json
import time
import scrapy
from urllib.parse import urlencode


class WalmartSpider(scrapy.Spider):
    # Spider name
    name = "walmart"

    def start_requests(self):
        """Give your keyword to scraper so its start scraping data from it"""
        # User desired keyword for scraping
        keyword = input("Write your keyword:")
        # Pre-defining URL parameters
        url_params = {
            "q": keyword,
            "sort": "best_match",
            "page": 1,
            "affinityOverride": "default",
            "location": "New York",
        }
        # Creating URL for scrapings
        walmart_search_url = "https://www.walmart.com/search?" + urlencode(url_params)
        # Sending the request and forwarding the response to parse_search_results function
        yield scrapy.Request(
            url=walmart_search_url,
            callback=self.parse_search_results,
            meta={"keyword": keyword, "page": 1},
        )

    def parse_search_results(self, response):
        """This function is parsing the response which it get from start_requests"""
        page = response.meta["page"]
        keyword = response.meta["keyword"]
        # Walmart store data in script tag so getting all the data via xpath
        script_tag = response.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        # Converting JSON data into python dictionary
        if script_tag is not None:
            json_blob = json.loads(script_tag)

            ## Getting the each product url and further sending it to parse_product_data to get data from the listing
            product_list = json_blob["props"]["pageProps"]["initialData"][
                "searchResult"
            ]["itemStacks"][0]["items"]
            for product in product_list:
                walmart_product_url = (
                    "https://www.walmart.com"
                    + product.get("canonicalUrl", "").split("?")[0]
                )
                yield scrapy.Request(
                    url=walmart_product_url,
                    callback=self.parse_product_data,
                    meta={"keyword": keyword, "page": page},
                )

            ## For scraping all the page results shown in search result
            if page == 1:
                # Getting Total number of pages appear in search result
                total_page_count = json_blob["props"]["pageProps"]["initialData"][
                    "searchResult"
                ]["paginationV2"]["maxPage"]
                for p in range(2, total_page_count):
                    url_params = {
                        "q": keyword,
                        "sort": "best_match",
                        "page": p,
                        "affinityOverride": "default",
                        "location": "New York",
                    }
                    walmart_search_url = "https://www.walmart.com/search?" + urlencode(
                        url_params
                    )
                    yield scrapy.Request(
                        url=walmart_search_url,
                        callback=self.parse_search_results,
                        meta={"keyword": keyword, "page": p},
                    )

    def parse_product_data(self, response):
        script_tag = response.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        if script_tag is not None:
            json_blob = json.loads(script_tag)
            raw_product_data = json_blob["props"]["pageProps"]["initialData"]["data"][
                "product"
            ]
            p_name = raw_product_data.get("name")
            yield {
                "Date": datetime.today().strftime("%m-%d-%Y"),
                "City Name": "New York",
                "Country Name": "USA",
                "Product Name": p_name,
                "Price": raw_product_data["priceInfo"]["currentPrice"].get(
                    "priceDisplay"
                ),
                "Available Packing": p_name.split(",")[1] if "," in p_name else p_name,
                "Price/Unit": raw_product_data["priceInfo"]["unitPrice"].get(
                    "priceString"
                )
                if raw_product_data["priceInfo"]["unitPrice"] is not None
                else "-",
                "Product Link": response.url,
            }
