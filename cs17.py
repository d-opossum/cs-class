# Do not copy | My Personal Use Only 
# Originally on Replit
# -------------------------
def user_input():
  name = input("Enter your name: ")
  age = int(input("Enter your age: "))
  return name, age
def print_user_input():
  name, age = user_input()
  print("{} is {} years old.".format(name, age))
print_user_input()
