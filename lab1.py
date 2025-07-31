def get_grade():
  try:
    marks = input()

    if marks.lower() == "exit":
      print("\nExiting...")
      return

    marks = int(marks)

    if marks < 0 or marks > 100:
      print("Invalid Input\n")
    elif marks >= 90:
      print("Grade : A\n")
    elif marks >= 75:
      print("Grade : B\n")
    elif marks >= 60:
      print("Grade : C\n")
    elif marks >= 40:
      print("Grade : D\n")
    else:
      print("Grade : F\n")
  except ValueError:
    print("Invalid Input\n")

if _name_ == "_main_":
  get_grade()
