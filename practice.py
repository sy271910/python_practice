# -*- coding: UTF-8 -

# Python语句中一般以新行作为语句的结束符，但是可以用斜杠（ \）将一行的语句分为多行显示
# Python 可以同一行显示多条语句，方法是用分号 ; 分开
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号
# Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。用缩进来写模块,缩进的空白数量是可变的，但是必须相同
# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。其中三引号可用于多行注释
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组

print("Hello, Python!")
print(str("Hello, Python!"))  # 函数返回一个用户易读的表达形式
print(repr("Hello, Python!"))  # 产生一个解释器易读的表达形式

# 数字
aa = int(990.04)
bb = 1
del bb
print(aa)

# 字符串
s = ('abcdef')
var1 = ('Hello World!')
print("更新字符串 :- ", var1[:6] + 'Runoob!')  # Hello Runoob!
print(s[1:5])  # [头下标，尾下标]     包头不包尾
print(s[:])  # 深复制
print(s[0])
print(s[1:])
print(s * 2)
print(s + "TEST")

# 列表
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)
# 列表推导式
print([str(round(355 / 113, i)) for i in range(1, 6)])

# 元祖
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出第二个至第三个的元素
print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)  # 输出元组两次
print(tuple + tinytuple)  # 打印组合的元组

# 字典
dict = {}
dict['one'] = "This is one"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(dict['one'])  # 输出键为'one' 的值
tinydict["code"] = 1016
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
# 字典推导式
print({x: x * 2 for x in (2, 4, 6)})

# Python指定任何非0和非空（null）值为true，0 或者 null为false
# 条件语句
# 与或非 and or not
num = 5
if num == 3:  # 判断num的值
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:  # 值小于零时输出
    print('error')
else:
    print('roadman')  # 条件均不成立时输出
# while循环
count = 0
while (count < 3):
    print('The count is:', count)
    count = count + 1

print("Good bye!")

# continue 语句跳出本次循环，而break跳出整个循环   pass是空语句，是为了保持程序结构的完整性
i = 1
while i < 6:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print(i)  # 输出双数2、4、6

i = 1
while 1:  # 循环条件为1必定成立
    print(i)  # 输出1~10
    i += 1
    if i > 4:  # 当i大于4时跳出循环
        break

# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b

# for循环
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print('当前水果 :', fruit)

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
for x in it:
    print(x)


def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))