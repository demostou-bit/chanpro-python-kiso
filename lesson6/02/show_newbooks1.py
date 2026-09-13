# scrapy crawl show_newbooks1 スパイダーを実行
import scrapy

class ShowNewbooks1Spider(scrapy.Spider):
  name = "show_newbooks1"
  allowed_domains = ["book.impress.co.jp"]
  start_urls = ["https://book.impress.co.jp"]

  def perse(self, response):
    #1 module-book-list-item-body-headクラスのdiv要素を順に取り出し、変数bookに格納
    for book in response.css("div.module-book-list-item-body-head"):
      # yield文で順にキーと値のペアの辞書として戻す
      yield {
        # 書籍タイトル
        "title": book.css("h4 a::text").get(),
        # 詳細情報のリンク先のURL
        "url": "https://book.impress.co.jp/" + book.css("h4 a").attrib['href']
      }
