# マウスの挙動と座標を表示
import pgzrun
WIDTH, HEIGHT = 550, 150

status = ""

def draw():
    # 画面をクリアしてマウスの状態を描画
    screen.clear()
    screen.draw.text(f"{status}", (50,50), color=(255,255,255), fontsize=50)

def on_mouse_down(pos):
    #1 マウス押下時にstatusを更新
    global status
    status = f"on_mouse_down({pos})"
def on_mouse_move(pos):
    #2 マウス移動時にstatusを更新
    global status
    status = f"on_mouse_move({pos})"
def on_mouse_up(pos):
    #3 マウスリリース時にstatusを更新
    global status
    status = f"on_mouse_up({pos})"

pgzrun.go()