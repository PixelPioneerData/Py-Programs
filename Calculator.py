A = int(input("Enter 1st value\n"))

op = input("Enter opperator\n")

B = int(input("Enter 2nd Value\n"))

if op == "+":
    print(A+B)

elif op == "-":
    print(A-B)

elif op == "*" or "x":
    print(A*B)

elif op == "/":
    print(A/B)

else:
    print("Invalid Statement")

