# キャンバスのテスト
import tkinter as tk

# メインウィンドウ
root = tk.Tk()
# タイトル
root.title("Canvasのテスト")
# Canvasを生成している部分で、幅500、高さ300ピクセル
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

# 直線を描く。最初の2つの引数で起点の座標x1,y1、終点の座標x2,y2を指定
# widthで線幅を、fillで塗りの色を指定
canvas.create_line(10, 10, 400, 40, width=10, fill="lightblue")
# 長方形を描く。引数で左上隅x1,y1、右下隅x2,y2を指定。outlineは枠線の色を指定
canvas.create_rectangle(400, 50, 450, 200, fill="green",
                        outline="purple", width=15)
# 楕円を描く。引数で楕円を囲む左上隅x1,y1、右下隅x2,y2
canvas.create_oval(10, 50, 400, 200, fill="yellow",
                   outline="blue", width=10)
# テキストを描く。位置は中心の座標で指定。textオプションで表示するテキスト
# fontでフォントをタプルで指定
canvas.create_text(250, 250, text="キャンバスのテスト", font=("", 30))

# メインループ
root.mainloop()



