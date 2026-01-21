name = input("What's your name? ")
def checkName(n):
  if name == "Abhi" or name == "Abhinash" or name == "abhi":
    print("Hii Abhinash")
  elif name == "Vashu":
    print("Hii Varsha")
  elif name == "mom":
    print("Good Morning MOM")
  else:
    print("Who are you")


def checkName2():
  match name:
    case "Abhi" | "Abhinash" | "a":
      print("Abhinash")
    case "Vashu":
      print("Varsha")
    case "watch":
      print("Hii watch")
    case _:
      print("Who?")
    

checkName2()