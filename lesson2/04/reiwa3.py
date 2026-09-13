# 無限ループとループの脱出
reiwa = 1

while True: #1 whileにTrueを指定して無限ループ化
  print(f'令和{reiwa}年は西暦{reiwa + 2018}年')
  reiwa = reiwa + 1
  if reiwa > 10: #2 reiwaが11以上の場合
    break #3 ループを脱出

