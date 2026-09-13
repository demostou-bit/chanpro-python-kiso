from doll2 import Doll #1 doll2.pyからDollクラスをインポート

class ModernDoll(Doll): #2 Dollクラスから継承するModernDollクラスの定義
  def goodbye(self): #3 新たにgoodbyeメソッドを定義
    print(f"私{self.name}ちゃん、さようなら！")

rica = ModernDoll("リカ") #4 ModernDollクラスのインスタンスを生成し、ricaに代入
rica.greet() #5 元のクラスであるDollクラスのgreetメソッドを
rica.goodbye() #6 ModernDollクラスに追加したgoodbyeメソッドを呼び出す
