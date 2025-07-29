num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
operation=input("Enter an operation(+,-,*,/):")
if operation=='+':
    result=num1+num2
elif operation=='-':
    result=num1-num2
elif operation=='*':
    result=num1*num2
elif operation=='/':
    if num2!=0:
        result=num1/num2
    else:
        result="undefined(division of zero)"
else:
    result=("invalid operation")
print(f"{num1}{operation}{num2}={result}")