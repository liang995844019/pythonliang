# print("Hello World")
# # 我是单行注释
# num1 = 20
# d = type(num1 )
# print(d)
#
#
# print('hello')
#
# num1 = 2
# d = num1
# print(d)
for i in range(1, 5):
    print(i)
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input('请输入退出')
# input("点击 enter 键退出")