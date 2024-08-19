x=int(input("enter your a number"))
y=int(input("enter your a number"))
op=int(input("enter your a op"))
def add(x,y):
    return(x+y)
def multiply(x,y):
    return(x*y)
def subtract(x,y):
    return(x-y)
def division(x,y):
    return(x/y)
if(op==1):
    print(add(x,y))
elif(op==2):
    print(multiply(x,y))
elif(op==3):
    print(subtract(x,y))
elif(op==4):
    print(division(x,y))
else:
    print("invalid")
