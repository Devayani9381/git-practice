# python program to check a leap year.
class leap:
    def year(self,a):
        self.a=self
        if a%4==0:
            print("year","is a leap year")
        else:
            print("year","is not a leap year")
a = int(input("enter a year"))
obj=leap()
obj.year(a)