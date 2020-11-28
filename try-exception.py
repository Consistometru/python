print("welcome")
from operator import pow, truediv, mul, add, sub, floordiv, mod

operators = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': truediv,
  '^': pow,
  '//': floordiv,
  '%': mod
}

def calculate(s):
    if s.isdigit():
        return float(s)
    for c in operators.keys():
        left, operator, right = s.partition(c)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))
file = open("history.txt", "w")
input1 = input("continue? yes / no: ")
while input1 == "yes":
    calc = input("Type calculation:\n")
    print("Answer: " + str(calculate(calc)))
    file.write(calc + "Answer: " + str(calculate(calc)))
    input1 = input("continue? yes / no: ")
file.close()