# ユーザーがCanvasの内部をクリックすると、その位置にランダムな大きさの正方形を描く
import tkinter as tk
import random

# メインウィンドウ
root = tk.Tk()
# タイトル
root.title("Canvasのテスト")

# コールバック関数
def button_pressed(event):
  # randint関数は引数1から引数2までの整数の乱数を発生させる
  size = random.randint(50, 100)
  # 正方形を描く
  canvas.create_rectangle(event.x - size, event.y - size,
                          event.x + size, event.y + size,
                          outline="green", width=5)

# Canvasを生成する
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Canvasをクリックすると、button_pressedを呼び出す
canvas.bind("<ButtonPress-1>", button_pressed)

# メインループ
root.mainloop()

