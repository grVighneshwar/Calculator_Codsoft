op1=float(input("enter operand 1:"))
op2=float(input("enter operator 2:"))
op=input("enter the operator:")

if op=='+':
    s=op1+op2
elif op=='-':
    s=op1-op2
elif  op=='/':
    try:
        s=op1/op2
    except ZeroDivisionError:
        print("cant divide by zero")
        exit
elif op=='*':
    s=op1*op2
elif op=='%':
    s=op1%op2
else:
    print("invalid operation")
try:
     print(f"{op1} {op} {op2} = {s}")
except NameError:
     pass
