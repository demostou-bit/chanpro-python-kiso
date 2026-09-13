# 内包表記でリストからリストを生成する
# リストに小数を格納
nums = [1.5, 3.4, 5.5, 4.5]
# 内包表記を使って、リストからリストを生成
# round関数を使用してリストnumsの要素を丸め込んでリストint_numsを生成
int_nums = [round(n) for n in nums]
# round関数による丸め込みは、判定する値が5の場合、結果が偶数となる
print(int_nums)
