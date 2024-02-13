# python program to calculate the area of triangle.
class area:
    def f1(self,l,b):
        self.l = l
        self.b = b
        area=self.l*self.b
        print("area =",area)
l = int(input("enter length"))
b = int(input("enter breadth"))
obj = area()
obj.f1(l,b)