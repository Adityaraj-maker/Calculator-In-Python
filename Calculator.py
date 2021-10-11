add=lambda x,y:x+y
div=lambda x,y:x/y
sub=lambda x,y:x-y
multipy=lambda x,y:x*y
square=lambda x:x*x

x=float(input("\nEnter first number: "))
y=float(input("Enter second number: "))
operation=input("Enter operation symbol: ")

if operation=="+":
    print(f'Answer is {add(x,y)}')

elif operation=='-':
    print(f'Answer is {sub(x,y)}')

elif operation=='/':
    try:print(f'Answer is {div(x,y)}')
    except ZeroDivisionError:print("Please enter a value other than 0")

elif operation=='*':
    print(f'Answer is {multipy(x,y)}')

elif operation=="sq":
    print(f"square {x} is {square(x)}")

else:print("Invalid operator, Only valid + - / * sq")

