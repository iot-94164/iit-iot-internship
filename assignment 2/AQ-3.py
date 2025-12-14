

def fibonacci(num):
    a,b=0,1
    for i in range(num):
        print(a, end=" ")
        a,b=b,a+b
num=int(input("enter a number: "))
fibonacci(num)
    


