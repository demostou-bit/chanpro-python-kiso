# Dollクラスを作成する
class Doll:
  def __init__(self, name): # 初期化メソッド
    self.name = name # インスタンス変数に代入
  def greet(self): # grretメソッドの定義
    print(f"私{self.name}ちゃん、よろしくね！")

# インスタンスの生成部分
rica = Doll("リカ")
rica.greet()
hana = Doll("ハナ")
hana.greet()
