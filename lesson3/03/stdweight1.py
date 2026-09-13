import tkinter as tk
import tkinter.messagebox

class StdWeight(tk.Frame):
  r_bmi = 22 # 標準のBMI値

  def __init__(self, master): # 初期化メソッド
    super().__init__(master, bg="yellow", padx=10, pady=30)
    master["bg"] = "yellow"
    self.pack()

    # 身長と体重を管理するウィジット変数をDoubleVarクラスの変数として宣言
    self.height_var = tk.DoubleVar()
    self.height_var.set(170.0) # setメソッドでデフォルトの身長を設定
    self.weight_var = tk.DoubleVar()
    self.weight_var.set(50.0) # setメソッドでデフォルトの体重を設定
    # ウィジットを生成はcreate_widgetメソッドにまとめ、以下で呼び出す
    self.create_widget()
  
  def calc(self):
    # 計算を実行し結果を表示する
    # try~except文で身長が数字であるかをチェック
    try:
      height = self.height_var.get()
    except:
      tk.messagebox.showerror("エラー", "身長は数字で入力してください")
      return
    # try~except文で体重が数字であるかをチェック
    try:
      weight = self.weight_var.get()
    except:
      tk.messagebox.showerror("エラー", "体重は数字で入力してください")
      return
    
    # 適正体重を計算して適正体重を表示
    std_weight = pow(height / 100, 2) * StdWeight.r_bmi
    # フォーマット文字列内で{変数:.2f}とすることで変数の値を小数点第2位まで表示
    self.r_label1["text"] = f"適正体重： {std_weight:.2f}kg"

    # BMIの値を計算し、if文でやせ型、肥満を判定してラベルに表示
    bmi = weight / pow(height / 100, 2)
    if bmi < 18.5:
      s = "やせ型"
    elif bmi < 25:
      s = "普通体重"
    elif bmi < 30:
      s = "肥満（1度）"
    elif bmi < 35:
      s = "肥満（2度）"
    elif bmi < 40:
      s = "肥満（3度）"
    else:
      s = "肥満（4度）"
    # フォーマット文字列内で{変数:.2f}とすることで変数の値を小数点第2位まで表示
    self.r_label2["text"] = f"BMI:{bmi:.2f} ー {s}"
  
  def clear(self):
    # 入力をクリアする
    self.height_var.set(0)
    self.weight_var.set(0)
    self.r_label1["text"] = ""
    self.r_label2["text"] = ""
  
  def create_widget(self):
    # ウィジットを生成する
    # 身長入力用Entry
    self.height_frame = tk.Frame(self, pady=2, padx=5, background="yellow")
    self.height_frame.pack()
    self.h_label1 = tk.Label(self.height_frame, text="身長")
    self.h_label1.pack(side=tk.LEFT)
    self.height_entry = tk.Entry(
      self.height_frame, width=10, textvariable=self.height_var)
    self.height_entry.pack(side=tk.LEFT)
    self.h_label2 = tk.Label(self.height_frame, text="cm")
    self.h_label2.pack(side=tk.LEFT)

    # 体重入力用Entry
    self.weight_frame = tk.Frame(self, pady=2, padx=5, background="yellow")
    self.weight_frame.pack()
    self.w_label1 = tk.Label(self.weight_frame, text="体重")
    self.w_label1.pack(side=tk.LEFT)
    self.weight_entry = tk.Entry(
      self.weight_frame, width=10, textvariable=self.weight_var)
    self.weight_entry.pack(side=tk.LEFT)
    self.w_label2 = tk.Label(self.weight_frame, text="kg")
    self.w_label2.pack(side=tk.LEFT)

    # 「計算」ボタンと「クリア」ボタン
    self.keisan_frame = tk.Frame(self, pady=2, padx=5, background="yellow")
    self.keisan_frame.pack()
    self.calc_btn = tk.Button(
      self.keisan_frame, text="計算", command=self.calc)
    self.calc_btn.pack(side=tk.LEFT)
    self.clr_btn = tk.Button(
      self.keisan_frame, text="クリア", command=self.clear)
    self.clr_btn.pack(side=tk.LEFT)

    # 結果を表示するフレーム
    self.result_frame = tk.Frame(self, pady=2, padx=5)
    self.result_frame.pack()
    self.r_label1 = tk.Label(text="", background="yellow", font=("", 20))
    self.r_label1.pack()
    self.r_label2 = tk.Label(text="", background="yellow", font=("", 20))
    self.r_label2.pack()

if __name__ == "__main__":
  root = tk.Tk()
  root.title("適正体重")
  root.geometry("400x300")
  app = StdWeight(master=root)
  root.mainloop()
