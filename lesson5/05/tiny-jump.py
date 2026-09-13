import pgzrun
from random import randint
WIDTH, HEIGHT = 1024, 512
back = Actor("bg")
score = 0
gameOver = False

# パラパラアニメーション用のActorクラス
class AnimateActor(Actor):
	# アニメーションのように画像を切り替えるため、画像のリスト, 何枚目の画像を表示するか, x、yの移動速度を指定
	def __init__(self, images, pos, speed):
		# 親クラスを初期化
		super().__init__(images[0], center=pos)
		self.images = images
		self.index = 0
		self.speed = speed

	# 画像を切り替えながら、spped分移動する
	def move(self):
		# 次の絵に切り替えて移動
		self.index = (self.index + 1) % len(self.images)
		self.image = self.images[self.index]
		self.x += self.speed[0]
		self.y += self.speed[1]

# アニメーションの画像リスト
images = [f"p1_walk/p1_walk{i:02}" for i in range(1, 12)]

# alienオブジェクトの作成
alien = AnimateActor(images, pos=(150, 450), speed=[0, 0])

# 敵のオブジェクトのリスト
enemies = [
	AnimateActor(["fish1", "fish2"], pos=[1300, 200], speed=[-5, 0]),
	AnimateActor(["snail1", "snail2"], pos=[800, 450], speed=[-2, 0]),
	AnimateActor(["spider1", "spider2"], pos=[1500, 450], speed=[-4, 0]),
	AnimateActor(["fly1", "fly2"], pos=[1200, 300], speed=[-8, 0]),
]


def draw():
	# 背景、alien、敵などの描画
	back.draw()
	alien.draw()
	for e in enemies:
		e.draw()
	screen.draw.text(f"score:{score}", (50, 50),
										color=(0, 0, 255), fontsize=60)
	if gameOver:
		screen.draw.text("GAME OVER", (250, 200),
											color=(0, 0, 255), fontsize=120)

def update():
	global score, gameOver
	if gameOver:
		return # GAME OVERがTrueの時、すぐにreturn

	score += 1
	# それぞれの敵を移動し、衝突判定
	for e in enemies: # 敵を取り出して移動させる
		e.move()
		if e. x < 0: # 画面の左外に出た場合、x座標を更新して画面右外に移動
				e.x = WIDTH + randint(0, 300)
		if e.colliderect(alien):
				gameOver = True # 主人公と衝突したらgameOverをTrueにする

	alien.move()
	# 重力加速度を加える
	alien.speed[1] += 0.2

	# 床についた時の処理
	if alien.y > 450:
		alien.speed[1] = 0 # y座標が450を超えたらy方向のスピードを0にする
		alien.y = 450

	# 背景スクロール
	back.x -= 1
	if back.x < 0:
		back.x = 1024

def jump():
	if alien.y >= 450:
		alien.speed[1] = -12 # ジャンプするよう、主人公のy方向の速度に-12を設定

def on_mouse_down(pos):
	jump()

def on_key_down(key):
	jump()

pgzrun.go()
