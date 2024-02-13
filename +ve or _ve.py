# python program to check if a number is positive or negative.
class num:
    def pos(self,a):
        self.a=a
        if a>0:
            print("positive")
        elif a<0:
            print("negative")
        else:
            print("zero")
a=int(input("enter value"))
obj=num()
obj.pos(a)

