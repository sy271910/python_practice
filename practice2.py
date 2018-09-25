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


# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。加了两个星号 ** 的参数会以字典(dict)的形式导入
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

#递归函数  一个函数在内部调用自身本身






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

# 属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问
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

#python 动态语言 鸭子类型 它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
#  继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写
# 由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态
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


def python_sy():
    print("史远")
    return
