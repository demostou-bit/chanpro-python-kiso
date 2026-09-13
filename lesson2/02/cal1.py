# 2026年10月のカレンダーを表示
import calendar #1

my_cal = calendar.TextCalendar() #2
my_cal.prmonth(2026, 10) #3

# モジュール名を間違えると
# ModuleNotFoundErrorと、
# 連鎖してAttributeErrorも起こる可能性もある

