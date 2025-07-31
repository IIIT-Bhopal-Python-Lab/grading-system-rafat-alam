def get_grade():
  try:
    marks = input()

    # Exiting code
    if marks.lower() == "exit":
      print("\nExiting...")
      return

    marks = int(marks)

    # Condition Checks
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
    # Input unknown value
    print("Invalid Input\n")

if __name__ == "__main__":
  get_grade()
