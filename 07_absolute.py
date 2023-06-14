# 练习：
#   写程序，输入一个数
#     1) 用if语句计算出这个数的绝对值并打印出来
#     2) 用条件表达式计算出这个数的绝对值并打印出来

n = int(input("请输入一个数: "))

# 1) 用if语句计算出这个数的绝对值并打印出来
# 方法1
# if n < 0:
#     absolute = -n
# else:
#     absolute = n
# 方法2
absolute = n
if absolute < 0:
    absolute = -absolute
print("if语句计算的绝对值是:", absolute)

# 2) 用条件表达式计算出这个数的绝对值并打印出来
absolute = -n if n < 0 else n
print("条件表达式计算的绝对值是:", absolute)
