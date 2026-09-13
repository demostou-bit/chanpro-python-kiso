# Actorを使った画像の移動
import pgzrun
WIDTH, HEIGHT = 500, 400

alien = Actor("alienpink", center=(250, 200))

def draw():
  screen.clear()
  alien.draw()

def on_key_down(key): #1 上下左右に移動
  if key == keys.UP:
    alien.y -= 2
  if key == keys.DOWN:
    alien.y += 2
  if key == keys.LEFT:
    alien.x -= 2
  if key == keys.RIGHT:
    alien.x += 2

pgzrun.go()
