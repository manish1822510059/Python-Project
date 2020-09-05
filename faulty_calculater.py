operator = input("Enter operator(+,-,*,/):")
val1 = int(input("Enter first operand = "))
val2 = int(input("Enter second operand = "))

if operator == "+":
    if val1 == 56 and val2 == 9:
        print("77")
    else:
        print("Sum is:",val1 + val2)
if operator == "-":
    print("Substract is:",val1-val2)
if operator == "*":
    if val1 == 45 and val2 == 3:
        print("555")
    else:
        print("Multiply is :",val1*val2)
if operator == "/":
    if val1 ==56 and val2 == 6:
        print("4")
    else:
        print("Divide is:",float(val1/val2))
