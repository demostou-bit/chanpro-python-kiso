# Actorを使った画像のアニメーション
import pgzrun
WIDTH, HEIGHT = 500, 400

alien = Actor("alienpink", center=(0, 200))

# アニメーションの種類のリスト
#1
tweens = ["linear", "accelerate", "decelerate", "accel_decel", "in_elastic",
          "out_elastic", "in_out_elastic", "bounce_end", "bounce_start",
          "bounce_start_end"]

def draw():
  # 背景をクリアしてアニメーションの名前をtextで描画
  screen.clear()
  #2 リストの文字を描画。enumerate関数でリストなどからインデックスと値を同時に取得
  #2 以下のようにすることで、リストtweensのインデックスをi、値をtに代入
  for i, t in enumerate(tweens):
    screen.draw.text(t, ((i%5)*100, (i//5)*30), fontsize=20)
  alien.draw()

def animation_end():
  #3 アニメーション終了時にalienをもとの場所に戻す
  alien.x, alien.y = 0, 200

def on_mouse_down(pos):
  # クリックされた場所にあるアニメーションを適用
  x = min(pos[0] // 100, 4) # min関数は2つ以上の引数のうち、最小値を戻す
  y = min(pos[1] // 30, 1)
  t = tweens[y * 5 + x]
  # クリック座標の値からどの文字がクリックされたかを求め、animate関数を実行
  animate(alien, pos=(450, 200), tween=t, duration=2, on_finished=animation_end)

pgzrun.go()
