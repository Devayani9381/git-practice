# python program to generate a random number.
import random
class num:
    def rand(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print("randint = ",b)
        print("randrange m=",c)
a = print(random.random())
b = random.randint(3,100)
c = random.randrange(50,100)
obj=num()
obj.rand(a,b,c)

