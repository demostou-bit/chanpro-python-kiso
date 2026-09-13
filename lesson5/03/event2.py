import pgzrun
WIDTH, HEIGHT = 450, 150

status = ""

def draw():
    # 画面をクリアしてキーの押下状態を描画
    screen.clear()
    screen.draw.text(f"{status}", (50,50), color=(255,255,255), fontsize=50)

def on_key_down(key):
    #1 キー押下時にstatusを更新
    global status
    status = f"on_key_down({key})"

def on_key_up(key):
    #2 キーを離した時にstatusを更新
    global status
    status = f"on_key_up({key})"

pgzrun.go()