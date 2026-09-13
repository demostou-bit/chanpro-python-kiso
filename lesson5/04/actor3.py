# Actorを使った画像の移動
import pgzrun
WIDTH, HEIGHT = 500, 400

alien = Actor("alienpink", center=(250, 200))

def draw():
  screen.clear()
  alien.draw()

def update(): #1 1秒間に60回呼び出される、キーボードが押されているかを判定
  if keyboard.UP:
    alien.y -= 2
  if keyboard.DOWN:
    alien.y += 2
  if keyboard.LEFT:
    alien.x -= 2
  if keyboard.RIGHT:
    alien.x += 2

pgzrun.go()

