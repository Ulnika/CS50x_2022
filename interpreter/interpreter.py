expression = input("Expression: ").split(" ")
x = int(expression[0])
y = expression[1]
z = int(expression[2])

if y == "+":
    print(float(x+z))
elif y == "-":
    print(float(x-z))
elif y == "*":
    print(float(x*z))
elif y == "/" and z!=0:
    print(float(x/z))