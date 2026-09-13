import pgzrun
WIDTH, HEIGHT = 700, 350

def draw():
  # (100, 100)の場所に文字を描画
  screen.draw.line((100, 0), (100, HEIGHT), (255, 255, 255)) #1 (100, 100)の座標が交わるようにlineメソッドで線を描画
  screen.draw.line((0, 100), (WIDTH, 100), (255, 255, 255))
  screen.draw.text("Hello", (100, 100), fontsize=50) #2 座標(100, 100)を指定して、"Hello"という文字をfontsizeが50の大きさで描いている

  # いろいろな引数で文字を描画
  #3 textメソッドではいろいろな指定ができる
  screen.draw.text("Hello", (0, 200), fontsize=30)
  screen.draw.text("Hello", (100, 200), fontsize=50)
  screen.draw.text("Hello", (200, 100), fontsize=50, color=(0, 255, 0))
  screen.draw.text("Hello", (300, 100), fontsize=50,
                   color=(0, 255, 0), background=(200, 200, 200))
  
  # textboxで文字を描画
  for i in range(4):
    y = i * 50 + 50
    r = Rect(400, y, 100 + i*50, 40)
    screen.draw.rect(r, (255, 255, 255))
    screen.draw.textbox("World", r) #4 指定された矩形の中に文字を描画。

pgzrun.go()
