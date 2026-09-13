# 2つの座標を結ぶ線の描画
import pgzrun
WIDTH, HEIGHT = 300, 300

def draw():
  #1 0、10、20、...290まで30回繰り返す
    for i in range(0, 300, 10):
        #2 2つの座標を結ぶ線を描画。(0,i)が開始の座標、(i, 300)が終点の座標
        #2 (i/2, 255, 255-i/2)が色の指定
        screen.draw.line((0, i), (i, 300), (i/2, 255, 255-i/2))

pgzrun.go()
