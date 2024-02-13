# python program to check if a number is odd or even.
class num:
    def evenodd(self,n):
        self.n=n
        if n%2==0:
            print("even")
        else:
            print("odd")
n = int(input("enter value"))
obj=num()
obj.evenodd(n)
