# python program to find the largest among three numbers.
class num:
    def three(self,num1,num2,num3):
        if num1>=num2 and num1>=num3:
            print("largest=num1")
        elif num2>=num3 and num2>=num1:
            print("largest=num2")
        elif num3>=num1 and num3>=num2:
            print("largest=num3")
        else:
            print("all are equal")
num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
obj=num()
obj.three(num1,num2,num3)
