class NastyClass:
    def __eq__(self, other):
        # 相手が誰であろうと「Noneと等しい」と主張するクラス
        return True

value = NastyClass()

# if value == None: の場合
if value == None:
    print("Noneだと思われた！")  # これが実行されてしまう

# if value is None:なら実行されない
#「None を書き換えること」はできませんが、「== を使った比較は、
# 相手の実装次第で意図しない結果を招くことがある」というのが、
# is None が推奨される最大の理由です。