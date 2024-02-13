# python program to swap two variables.

class swap:
    def var(self,a,b):
        self.a=a
        self.b=b
        c=a
        a=b
        b=c
        print("swap =",a,b)
a=int(input("enter value"))
b=int(input("enter value"))
obj = swap()
obj.var(a,b)
