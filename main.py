#Alannah Steck
#U3L2
#n factorial
#૮꒰ ˶• ༝ •˶꒱ა good luck bunny 

def forFactorial(n):
  sum = 0
  times = n-1
  if times == 0: #checks if n == 1. if so loop wont run
    return 1
  for time in range(times): 
    if times == n - 1: #multiplying
      sum += n * times
    else:
      sum *= times
    times -= 1
  return sum

def whileFactorial(n): #fix it -_-
  if n == 1: 
    return n
  sum = 0
  multiply = n-1
  while multiply > 0: #multiply
    if sum == 0:
      sum += n * multiply
    else:
      sum *= multiply
    multiply -= 1
  return sum
  
def recursionFactorial(n, sum=0, first=True):
  if n > 0:
    if first:
      sum += n * (n-1)
      first = False
      n -=1
    else:
      sum *= n
    n -=1
    sum = recursionFactorial(n,sum,first)
  return sum


def main():
  n = 4
  print("\n==For Factorial==\n")
  print(f"The factorial of {n} is {forFactorial(n)}\n")
  print("\n==While Factorial==\n")
  print(f"The factorial of {n} is {whileFactorial(n)}\n")
  print("\n==Recursion Factorial==\n")
  print(f"The factorial of {n} is {recursionFactorial(n)}\n")

if __name__ == "__main__":
  main()