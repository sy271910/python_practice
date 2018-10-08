# -*- coding: UTF-8 -
from enum import Enum,unique




# 定义一个函数
#必选参数在前 默认参数在后 调用时默认参数可省略，默认参数必须指向不变对象
def changeme(mylist,aa=1):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return  # return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None

mylist = [10, 20, 30]
changeme(mylist)
print("mylist")


# *args是非关键字参数，用于元组，**kw是关键字参数，用于字典
def printinfo(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

# 匿名函数 lambda [arg1 [,arg2,.....argn]]:expression
sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
printinfo(70, 60, 50)

# 创建一个集合
aa={'a','a','b'}
print(aa)
x = set('aabbcc')
print(x)


# python 面向对象
class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass()
# 访问类的属性和方法
print(x.i)
print(x.f())

# 在Python中，实例的变量名如果以__(双下划线)开头，就变成了一个私有变量（private），只有内部可以访问
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())

# 继承 多态
class Animal(object):
    def run(self):
        print("Animal is running")


class Dog(Animal):
    def eat(self):
        print("meat")


dog = Dog()
dog.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())

# map()
def f(x):
    return x*x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#filter()
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# __slots__
class uzi():
    __slots__ = ('name', 'age')

uu=uzi()
uu.name='简自豪'
#@property
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s=Student()
s.score=99
#枚举
class Color(Enum):
    red = 1
    yellow = 2
print(Color(1))
for color in Color.__members__.items():
     print(color)



def python_sy():
    print("史远")
    return
