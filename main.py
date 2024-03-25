import art
from replit import clear

res = 0

def add(num1, num2 ):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  if num2 == 0:
    print("Divide by zero is not permitted.")
    return

  return num1 / num2

def operation(num1, num2, op):
  if op == "+":
    return add(num1=num1, num2=num2)
  elif op == "-":
    return subtract(num1=num1, num2=num2)
  elif op == "*":
    return multiply(num1=num1, num2=num2)
  else:
    return divide(num1=num1, num2=num2)

def get_and_print(num1, num2, op):
  res = operation(num1=num1, num2=num2, op=op )
  print(f"{num1} " + op + f" {num2} = {res}")
  return res
  
print(art.logo)

flag = True
restart = True

while flag:
  if restart:
    num1 = int(input("What is the first number?: "))
  else:
    num1 = res

  op = input("+\n-\n*\n/\nPick an operation: ")
  num2 = int(input("Whats the next number?: "))
  res = get_and_print(num1=num1,num2=num2,op=op)

  if res == None:
    restart = True
    continue
    
  ip = input(f"Type 'y' to continue calculate with {res},or 'n' to start a new calculation: ")
  if ip.lower() == 'y':
    restart = False
  else:
    clear()
    restart = True
    