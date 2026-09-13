# Actorを使った画像の回転
import pgzrun
WIDTH, HEIGHT = 500, 400

alien = Actor("alienpink", center=(250, 200))

def draw():
  # 背景をクリアしてalienを描画
  screen.clear()
  alien.draw()

def update():
  # キー押下に応じてalienを回転
  if keyboard.RIGHT:
    alien.angle -= 2
  if keyboard.LEFT:
    alien.angle += 2

def on_mouse_move(pos):
  # マウスの動きでalienを回転
  alien.angle = alien.angle_to(pos)

pgzrun.go()
