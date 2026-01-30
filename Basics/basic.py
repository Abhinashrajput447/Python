def main():
  x = get_int()
  print(f"x is {x}")

def errorHandler():
  try:
    x = int(input("What's x ? "))
  except ValueError:
    print("x is not an integer")
  else:
    print(f"x is {x}")

def get_int():
  while True:
    try:
      return int(input("What's x ? "))
    except ValueError:
      pass

    
    # else:
    #   return x
  # return x
  # print(f"x is {x}")


get_int()


def userNamezValidChecker():
  userName = input("what's username? ")

  if " " in userName or userName[0].isalpha():
    print("user anme contain 'a-z', 'A-Z', '0-9'")
    # if not userName[0].isalpha():
    #   print("Invalid username: must start with a letter")
  if not userName.isalpha():
    print("Invalid username: only letter Allowed")
    return
  
  print(f"valid username: '{userName}'")


# userNamezValidChecker()