# 円と矩形の描画
import pgzrun
WIDTH, HEIGHT = 500, 450

def draw():
  # 線を描画
  for i in range(4): #1 座標の目印となる線を描画
    y = i * 100 + 50
    x = i * 100 + 100
    screen.draw.line((0, y), (WIDTH, y), (255, 255, 255))
    screen.draw.line((x, 0), (x, HEIGHT), (255, 255, 255))
  
  # 各図形（円・矩形 x 枠・塗りつぶし）を描画
  for i in range(4): #2 左から右へ描画
    y = i * 100 + 50
    c = (i * 80, 128, 0)

    screen.draw.circle((100, y), 40, c) #3 円
    screen.draw.filled_circle((200, y), 40, c) #4 塗りつぶしの円
    r0 = Rect(300, y, 60, 40)
    r1 = Rect(400, y, 40, 60)
    screen.draw.rect(r0, c) #5 矩形
    screen.draw.filled_rect(r1, c) #6 塗りつぶしの矩形

pgzrun.go()
