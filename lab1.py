def calc_grade():
  while True:
    try:

      # Input Marks
      marks = input("Please enter marks [0, 100]: ")

      if(marks == "exit"):
        print("\nExiting...")
        break

      marks = int(marks)

      # Marks Validation
      if(marks < 0 or marks > 100):
        print("Marks is not in range of [0, 100]\n")
        continue
      else:

        # Grade Evaluation
        if(marks >= 90):
          print("Grade : A\n")
        elif(marks >= 75):
          print("Grade : B\n")
        elif(marks >= 60):
          print("Grade : C\n")
        elif(marks >= 40):
          print("Grade : D\n")
        else:
          print("Grade : F\n")
    except ValueError:
      # Marks integer input exception handling
      print("Oops! That was not a valid marks. Try again...\n")

# Choice Selection
print("Please choose an option")
print("1. Calculate grade")
print("2. Exit")


choice = ""

while True:
  ch = input("Enter your choice number : ");
  if(ch == "1"):
    choice = ch
    print("\nNote : For exiting option enter \"exit\" in marks\n")
    break
  elif(ch == "2"):
    choice = ch
    break
  else:
    print("Wrong choice. Try Again.\n")

calc_grade()