# Prompts user for expression and splits it at whitespace
ex = input("Expression: ").split()

x = float(ex[0]) # x is number before the operator
z = float(ex[-1]) # z is the number after the operator

# matches cases for each operator
match ex[1]:
    case "+":
        print(f"{x + z}")
    case "-":
        print(f"{x - z}")
    case "*":
        print(f"{x * z}")
    case "/":
        print(f"{x / z}")