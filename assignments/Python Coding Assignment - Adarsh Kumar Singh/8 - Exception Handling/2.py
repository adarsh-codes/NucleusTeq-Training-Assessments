try:
  number = int(input("Enter a number : "))
  print("Your number is :",number)
except TypeError:
  print("Invalid Input. Enter only a number.")
except ValueError:
  print("Invalid Input. Enter only a number.")
except Exception:
  print("Please Try again.")
