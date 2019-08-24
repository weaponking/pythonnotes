# !/usr/bin/python3
# !/usr/bin/env python
print("Hello, World!")
print("你好 世界!")

# 缩进代替{}
if True:
    print('True')
    print('--')
else:
    print('false')
print('end print')

# （ \）将一行的语句分为多行显示
item_one = '1'
item_two = '2'
item_three = '3'
total = item_one + \
        item_two + \
        item_three
print(total)

# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的
word = 'word'
sentence = "这是一个句子。"

'''
注释
区域
不执行
'''

"""
多行注释
双引号
"""

a, b = 0, 1
while a < 10:
    """
    赋值运算 先计算赋值号 计算等值 右边 那么 b=1 a+b=1
    """
    a, b = b, a + b
    print("a , b : ", a, b)

"""
x = int(input("Please enter an integer: "))
if x <= 0:
    print('x <= 0')
elif x == 1:
    print('x = 1')
else:
    print('more')
"""

words = ['1', '2', 'a', 'b', '1234567']
for w in words:
    print(w)

for w in words[:]:
    if len(w) > 6:
        print(w)
        # 1234567

# 0 - 4
for i in range(5):
    print(i)

# 5 - 9
for i in range(5, 10):
    print(i)


def ask_ok():
    v = 1
    while v < 10:
        v = v + 1
    else:
        return v


var = ask_ok()
print(var, " : v")

i = 5


def f(arg=i):
    print(arg)


i = 6
f()


def f(a1, l1=[]):
    l1.append(a1)
    return l1


print(f(1))
print(f(2))
print(f(3))


