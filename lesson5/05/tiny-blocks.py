import pgzrun
from math import radians, sin, cos
from random import randrange
WIDTH, HEIGHT = 600, 700

# ブロッククラス
class Block(Rect):
	def __init__(self, x, y, c, p):
		super().__init__(x, y, 80, 20)
		self.color = c # ブロックの色
		self.point = p # 壊したときに加算する点数
		self.erase = False # 画面から消えるか否か

score = 0
ball = [300, 200]
angle = randrange(90-45, 90+45)
speed = 5
cols = ["red", "orange", "yellow", "blue"]
paddle = Block(300, 650, "yellow", 0) # パドルを作成

# ブロックを配置
blocks = []
for i, y in enumerate(range(4)): # 2重forループを使ってブロックを作成し、リストblocksに追加
	for x in range(6):
		blocks.append(Block(x*100+10, y*30+60, cols[i], (5-i)*20))

def draw():
	# 背景クリア、スコアとパドルの描画
	screen.clear()
	screen.draw.text(f"score:{score}", (30, 10), fontsize=30, color="yellow")
	screen.draw.filled_rect(paddle, paddle.color)

	# ブロックの描画
	for b in blocks: # ブロックを取り出し描画
		screen.draw.filled_rect(b, b.color)
	if len(blocks) == 0: # ブロックが空になったらクリア
		screen.draw.text("CLEAR!!!", (160, 300), fontsize=100, color="yellow")
		return
	if ball[1] > HEIGHT: # ボールのY座標がHEIGHTを超えるとゲームオーバー
		screen.draw.text("Game Over!!!", (160, 300), fontsize=70, color="yellow")

	# ボールの描画
	screen.draw.filled_circle(ball, 10, color="yellow")

def update():
	global angle, blocks, score, speed
	# 角度とスピードからx軸、y軸の移動量を計算
	ball[0] += speed * cos(radians(angle))
	ball[1] += speed * sin(radians(angle))
	if ball[0] < 0 or ball[0] > WIDTH:
		angle = 180 - angle
	if ball[1] < 0:
		angle = -angle
		speed = 10

	# パドルとボールの衝突判定
	if paddle.collidepoint(ball):
		r = (ball[0] - paddle.center[0]) / paddle.width  # r = -0.5 ~ +0.5
		angle = -90 + 60 * r

	# ブロックとボールの衝突判定
	for b in blocks:
		if b.collidepoint(ball):
			b.erase = True
			score += b.point
			angle = -angle
			break

	blocks = [b for b in blocks if not b.erase]

def on_mouse_move(pos):
	paddle.center = (pos[0], 650)

pgzrun.go()
