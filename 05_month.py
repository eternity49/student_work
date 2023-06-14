# 05_month.py


# 2. 输入一年中的月份(1~12), 输出这个月在哪儿个
#    季度，如果输入的是其它数，提示您的输入有误!

month = int(input("请输入月份: "))
if 1 <= month <= 3:
    print("春季")
elif 4 <= month <= 6:
    print("夏季")
elif 7 <= month <= 9:
    print("秋季")
elif 10 <= month <= 12:
    print("冬季")
else:
    print("您的输入有误！")
