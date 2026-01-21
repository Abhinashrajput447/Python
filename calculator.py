# # score = int(input("Enter your score:  "))

# def grade():
#   if score >= 100:
#     print("Score doesn't exist for a single subject")
#   elif score >= 90:
#     print("Grade A")
#   elif score >= 80:
#     print("Grade B")
#   elif score >= 70:
#     print("Grade C")
#   elif score >= 60:
#     print("Grade D")
#   else:
#     print("Grade F")


# num = int(input("enter your number: "))

# def checkEvenOrOdd():
#   if num%2 == 0 :
#     # print("Even")
#     return True
#   else:
#     # print("Which number you have entred that is odd")
#     return False

# grade()
# checkEvenOrOdd()
# # if


def main():
  x = int(input("what's x ? "))
  if(is_even(x)):
    print("Even")
  else:
    print("Odd")


def is_even(n):
  if n%2 == 0 :
    return True
  else:
    return False
  
main()