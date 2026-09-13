import pgzrun
from random import randint
WIDTH, HEIGHT = 500, 400 # ウィンドウのサイズを幅500、高さ400pxに設定

bat = Actor("bat", center=(250,200))
score = 0
time = WIDTH

def draw():
	screen.clear() # 画面をクリアする
	
	# 残り時間のタイムゲージとスコアを描画
	screen.draw.filled_rect(Rect(0,0,time,10), (0,255,0))
	screen.draw.text(f"score:{score}", (50,50), color=(255,255,0), fontsize=40)

	# 時間切れになったらゲームオーバーに
	if time < 0:
			screen.draw.text("GAME OVER", (120,200), color=(255,255,0), fontsize=60)
	bat.draw()

def update():
	# 残り時間を徐々に減らす
	global time
	time -= 0.5

def animation_end():
	# アニメーション終了時に、次の場所へ移動
	if time > 0:
		animate(bat, pos=(randint(0,WIDTH), randint(0,HEIGHT)),
				on_finished=animation_end)

# こうもりをクリックしたときのポイント加算
def on_mouse_down(pos):
	global score
	if time > 0 and bat.collidepoint(pos):
		score += 1

# 最初の移動
animate(bat, pos=(randint(0,WIDTH), randint(0,HEIGHT)),
        on_finished=animation_end)

pgzrun.go()
