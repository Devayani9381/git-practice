# python program to find the factorial of given number.
class num:
    def factorial(self,n):
        if n<=0:
            print("invalid num")
        elif n==0:
            print(1)
        else:
            f=1
            for i in range(n,0,-1):
                f=f*i
            print(f)
n=int(input("enter number"))
obj=num()
obj.factorial(n)

