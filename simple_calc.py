def calc(a,b,c):
  if(a=='+'):
    print(b,"+",c,"=",b+c)
  elif(a=='-'):
    print(b,"-",c,"=",b-c)
  elif(a=='*'):
    print(b,"*",c,"=",b*c)
  elif(a=='/'):
    print(b,"/",c,"=",b/c)
  else:
    print("invalid input")
x=input("choose the operator")
num1=float(input("enter the first value"))
num2=float(input("enter the second value"))
calc(x,num1,num2)