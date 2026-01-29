def errorHandler():
  try:
    x = int(input("What's x ? "))
  except ValueError:
    print("x is not an integer")
  else:
    print(f"x is {x}")


def errorhandlerStr():
  try:
    userName = input("what's x? ")
  except:
    print("X is not a string ")
  else:
    if userName % 1 != 0:
      print(f"userName is '{userName}'")
    else:
      print("invalid userName try again")


def userNamezValidChecker():
  userName = input("what's username? ")

  if " " in userName:
    print("Invalid username: space not allowed")
  if not userName[0].isalpha():
    print("Invalid username: must start with a letter")
  if not userName.isalpha():
    print("Invalid username: only letter Allowed")
    return
  
  print(f"valid username: '{userName}'")


userNamezValidChecker()