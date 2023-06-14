# 06_score.py

# 练习：
#   输入一个学生的成绩(0~100),
#   判断这个学生的成绩是优（90~100），良(80~89)，及格(60~79)，不及格，成绩不合法5种状态
#   (建议使用if语句嵌套)

score = int(input("请输入一个学生的成绩: "))
if 0 <= score <= 100:
    if score < 60:
        print("不及格")
    elif 60 <= score < 80:
        print("及格")
    elif score < 90:
        print("良好")
    else:
        print("优秀")
else:
    print("成绩不合法")