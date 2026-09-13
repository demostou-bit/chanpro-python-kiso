# Pygame Zeroをインストール
# 実行できない場合、「Ctrl」+「Shift」+「P」を押してインタープリターを選択
# anaconda3～を選択してから実行する
#1 requestsモジュールをインポート

import pgzrun # モジュールの読み込み

# ウィンドウのサイズ指定
WIDTH = 300
HEIGHT = 300

def draw(): #3 draw関数を定義して描画が必要になったときに呼び出す
  screen.fill((128, 0, 0)) #4 背景色の設定

pgzrun.go()
