# python program to display the multiplication table.
class table:
    def mult(self,num):
        for i in range(1,21):
            print(num,"x",i,"=",num*i)
num=int(input("enter number"))
obj=table()
obj.mult(num)
