# Actorを使った画像の衝突
import pgzrun
from random import randint
WIDTH, HEIGHT = 500, 400

alien = Actor("alienpink", center=(250, 200))
bat = Actor("bat")

def draw():
  screen.clear()
  alien.draw()
  bat.draw()

def update():
  # キー押下に応じて移動
  if keyboard.UP:
    alien.y -= 2
  if keyboard.DOWN:
    alien.y += 2
  if keyboard.LEFT:
    alien.x -= 2
  if keyboard.RIGHT:
    alien.x += 2
  
  # 衝突時は移動
  if alien.colliderect(bat): #2 衝突判定
    bat.x = randint(0, WIDTH)
    bat.y = randint(0, HEIGHT)

pgzrun.go()