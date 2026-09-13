# 任意の数の整数を引数として受け取り、その総和を求める関数
def sum(*nums):
  result = 0
  for n in nums:
    result = result + n
  return result

# 定義したsum関数を呼び出す
sum1 = sum(1, 9, 100)
print(sum1)
sum2 = sum(9, 10, 5, 3, -5)
print(sum2)
