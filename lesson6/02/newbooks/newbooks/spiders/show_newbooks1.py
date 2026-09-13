import scrapy

#1 スパイダークラスがscrapy genspiderコマンドで入力したスパイダー名を元にした
#1 ShowNewbooks1Spiderという名前で作成される
class ShowNewbooks1Spider(scrapy.Spider): # scrapyモジュールのSpiderクラスのサブクラス
    name = "show_newbooks1" # 変数nameはscrapy genspiderコマンドで指定したスパイダー名
    allowed_domains = ["book.impress.co.jp"] # スパイダーがアクセスできるドメイン名が格納されている
    start_urls = ["https://book.impress.co.jp"] # spiderがスクレイピングを開始するURLが設定されている

    def parse(self, response): # スクレイピングの処理を行うメソッド
        # module-book-list-item-body-headのdiv要素を順に取り出す
        for book in response.css("div.module-book-list-item-body-head"):
            yield { # yield文で順にキーと値のペアを辞書として戻す
                "title": book.css("h4 a::text").get(), # タイトルの値として書籍タイトル
                "url": "https://book.impress.co.jp/" + book.css("h4 a").attrib['href'] # リンク先のURLを返す
            }
