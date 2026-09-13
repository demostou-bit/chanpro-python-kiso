import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 400

# フルーツクラス
class Fruit(Actor):
	def __init__(self, file, bomb):
		super().__init__(file)
		self.bomb = bomb # 爆弾か否か
		self.setup()

	def setup(self):
		# オブジェクトの初期化・リセット
		self.x = randint(50,WIDTH-100) # 座標
		self.y = HEIGHT
		self.sx = randint(-2, 2) # 速度
		self.sy = randint(-10, -5)
		self.time = frameCount + randint(0,100) # 投げる時刻

	def move(self):
		# 座標を更新し、y方向の加速度を増やす
		self.x += self.sx
		self.y += self.sy
		self.sy += 0.1

fruits = []
mouse, pmouse = None, None
score = 0
frameCount = 0
flash = False
timeUp = False
isDown = False

# フルーツを作成してリストに追加
for i in range(3):
	fruits.append(Fruit(f"fruit{i}", i == 0))

def draw():
	global flash
	# タイムゲージとスコアの描画
	screen.draw.filled_rect(Rect((0,0), (frameCount/2, 5)), (0,0,255))
	screen.draw.text(f"Score:{score}", (20,40), color="yellow", fontsize=40)

	if timeUp:
		# 時間切れ
		screen.draw.text(f"Time UP", (200,200), color="yellow", fontsize=40)
		return

	for f in fruits:
		# フルーツの移動と描画
		if f.time < frameCount:
			f.move()
			f.draw()

		# 落下して画面の下を過ぎたら、次に投げる時刻を設定
		if f.y > HEIGHT * 2:
			f.setup()

	if flash:
		# 画面点滅時の描画
		screen.draw.filled_rect(Rect((0,0), (WIDTH, HEIGHT)), (255,255,0))
		flash = False

	if mouse and pmouse:
		# マウスの軌跡の描画
		screen.draw.line(pmouse, mouse, (255,255,255))
    
def update():
	# 時間切れかどうかのフラグをセット
	global frameCount, timeUp
	frameCount += 1
	timeUp = frameCount/2 > WIDTH
	screen.blit("black500x400",(0,0)) # 残像の効果を表現するため半透明の黒色の画像を描画

def on_mouse_down(pos):
	global isDown, pmouse, mouse
	isDown, pmouse, mouse = True, pos, pos

def on_mouse_up():
	global isDown, pmouse, mouse
	isDown, pmouse, mouse = False, None, None

def on_mouse_move(pos):
	global score, pmouse, mouse, flash
	if isDown:
		# マウス押下状態
		pmouse = mouse
		mouse = pos
		for f in fruits:
			if f.collidepoint(pos):
				# フルーツとマウスの衝突処理
				if f.bomb:
					score = 0
					flash = True
				else:
					score += 1
				f.setup()

pgzrun.go()
