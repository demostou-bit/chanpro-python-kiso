import scrapy


class ShowNewbooks2Spider(scrapy.Spider):
	name = "show_newbooks2"
	allowed_domains = ["book.impress.co.jp"]
	start_urls = ["https://book.impress.co.jp"]

	def parse(self, response):
		for book in response.css("div.module-book-list-item"):
			yield {
					"title": book.css("h4 a::text").get(),
					"url": "https://book.impress.co.jp/" + book.css("h4 a").attrib['href'],
					# キャッチコピー
					"copy": book.css("div.div.module-book-list-item-body-txt p:first-child::text").get(),
					# 発売日
					"sale-date": book.css("p.module-book-sale-date::text").get(),
					# ジャンル
					"genre": book.css("p.module-book-cate::text").get()
			}
