def evaluate(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == "+":
                result = operand1 + operand2
            elif char == "-":
                result = operand1 - operand2
            elif char == "*":
                result = operand1 * operand2
            elif char == "/":
                result = operand1 / operand2
            stack.append(result)
    return stack.pop()

expression = "13*28*+3-"
print(evaluate(expression))
