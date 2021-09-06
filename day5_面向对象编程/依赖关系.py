class Dog:
    def __init__(self,name,age,breed,master):
        self.name = name
        self.age = age
        self.breed = breed
        self.master = master # master传进来的应该是个对象
        self.sayhi()  # 调用自己的方法在实例化的时候

    def sayhi(self):
        print("Hi, I'm %s, a %s dog, my master is %s" %(self.name,self.breed,self.master.name))


class Person:
    def __init__(self,name,age,sex):

        self.name = name
        self.age = age
        self.sex = sex

    def walk_dog(self,dog_obj):
        """遛狗"""
        print("主人[%s]带狗[%s]去溜溜。。。" % (self.name,dog_obj.name ))

p1 = Person("Alex",25,"M")

d1 = Dog("Mjj",2,"二哈",p1)
