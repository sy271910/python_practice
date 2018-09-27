# -*- coding: UTF-8 -

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


# 匿名函数 lambda [arg1 [,arg2,.....argn]]:expression
sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
printinfo(70, 60, 50)

x = set('runoob')
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

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x*x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

def python_sy():
    print("史远")
    return
