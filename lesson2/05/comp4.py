# 拡張子が.pngの要素のみを取り出してリストpng_imagesを生成
files = ["news.png", "readme.txt", "sky.png",
         "index.html", "cat.png", "dog.jpg"]
# endswithはstrクラスのメソッドで、文字列の最後が引数で
# 指定した値と同じであればTrue、そうでなければFalseを戻します。
png_images = [f for f in files if f.endswith(".png")]
print(png_images)