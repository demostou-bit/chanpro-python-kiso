# Actorを使った画像の表示
import pgzrun
WIDTH, HEIGHT = 500, 400

alien = Actor("alienpink", center=(250, 200))

def draw():
  screen.clear()
  alien.draw()

pgzrun.go()
