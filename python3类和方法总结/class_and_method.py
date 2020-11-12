class Chezi():
    def che(self):
        print("我是一辆跑车")


class Fangzi():
    def __init__(self, name='Mr.jiang', address='江西'):#__init__构造函数;实例化的时候就会运行这里；
        self.name = name
        self.address = address
        print(name, address)

    def fang(self):
        print("我是商品房")

"""类，class开头，且类名第一个字母大写。（）内默认继承object类,也可以不带括号创建类"""
class Ass:
    def aff(self):
        print('类')

class People(Chezi, Fangzi):#继承后，直接使用里面的方法
    def __init__(self, name='yaya'):
        super(People, self).__init__()#相当于吧父类的构造函数复制过来了。然后重新定义了一些属性
        self.name = name
        print(name)

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def pull(self):
        print("拉")

    def scatter(self):
        print("撒")

    def summary(self):
        print("人这一生啊，就是：")
        self.eat()
        self.drink()
        self.pull()
        self.scatter()

    def che(self):#方法重构，继承的类中有该方法；
        print("重买一辆路虎")

    def ziliao(self):
        print(f'我叫{self.name},来自{self.address}')#一个类里面可以调用定义过的属性;

    def fang(self):
        super().fang()#super是调用父类的方法
        print("加一层")

if __name__ == '__main__':
    """实例化类，然后可以使用。可以多个实例化；类里面，可以调用写过的类。"""
    a = People()#给属性重新赋值
    b = People()
    a.che()
    a.fang()
    print(a.che())#定义的方法没有return,返回值为None,跟函数一样；
    a.fang()
    import os
    n = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ke13.py")
    print(n)
    """pytest的类的用例是可以直接运行的，不用实例化类，框架帮忙解决了这些事情；"""
