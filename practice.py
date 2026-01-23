n = int(input("Enter the number? "))

#Natural number 
def natural():
  for num in range(1, n+1):
    print(num, end=" ")

#Reverse Natural number 
def reverse():
  for i in range(n, 0, -1):
    print(i, end=" ")
  
# All evens upto n
def allEvens():
  for i in range(1,n):
    if i % 2 == 0:
      print(i, end=" ")

#All odd upto n
def allOdds():
  for i in range(n):
    if i % 2 != 0:
      print(i, end=" ")

def squre1toN():
  for i in range(1, n+1):
    print(i*i, end=" ")


def num1ToNDivBy3():
  for i in range(1, n):
    if i%3 == 0:
      print(i, end=" ")

def cntDivBy5():
  cnt = 0
  for i in range(1, n+1):
    if i % 5 == 0:
      cnt += 1
  return cnt


def noExp7(n):
  for i in range(1, n+1):
    if i % 7 != 0:
      print(i, end=" ")

def sum1ToN(n):
  sum = 0
  for i in range(1, n+1):
    sum += i
  return sum

print(sum1ToN(n))
  