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
paragraph = """这是一个段落。