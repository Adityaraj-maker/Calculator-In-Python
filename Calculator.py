# Program to creat four function calculator.
answer=0
num1=int(input("Enter your first number:"))
num2=float(input("Enter your second number"))
operator=input("Enter the Operator (+,-,*,/):")
if operator=="+":
    answer = num1+num2
elif operator == "-":
    answer = num1-num2
elif operator=="*":
    answer=num1*num2
elif operator=="/":
    if num2==0:
        print("Enter a value other than 0")
    else:
        answer=num1/num2
else:
    print("Error")
print("Answer = ",answer)

