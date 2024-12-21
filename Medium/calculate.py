def calculate(s: str) -> int:
    stack = []
    current_number = 0
    operator = '+'
    
    s = s + '+'
    
    for i, char in enumerate(s):
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        
        if char in '+-*/' or i == len(s) - 1:
            if operator == '+':
                stack.append(current_number)
            elif operator == '-':
                stack.append(-current_number)
            elif operator == '*':
                stack[-1] = stack[-1] * current_number
            elif operator == '/':
                stack[-1] = int(stack[-1] / current_number)  
            current_number = 0
            operator = char
    
    return sum(stack)

s = "3+2*2"
print(calculate(s))  

s = "3/2"
print(calculate(s)) 

s = "3+5/2"
print(calculate(s))  
