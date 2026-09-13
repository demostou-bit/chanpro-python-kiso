# Dollクラスを作成する
class Doll:
  def __init__(self, name): # 初期化メソッド
    self.name = name # インスタンス変数に代入
  def greet(self): # grretメソッドの定義
    print(f"私{self.name}ちゃん、よろしくね！")

# if文以降がテスト用ブロック。通常のプログラムとして実行した場合にif文が実行される
if __name__ == "__main__":
  rica = Doll("リナ")
  rica.greet()
  hana = Doll("ハナ")
  rica.greet()
