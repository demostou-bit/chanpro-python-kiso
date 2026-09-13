# 描画イベント
import pgzrun
WIDTH, HEIGHT = 250, 150

count = 0

def draw(): #1 countの値を描画
  screen.clear()
  screen.draw.text(f"count={count}", (50, 50),
                   color=(255, 255, 255), fontsize=50)
  
def update(): #2 countの値を1増やす
  global count
  count += 1

pgzrun.go()
