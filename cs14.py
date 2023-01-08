# Do not copy | My Personal Use Only 
# Originally on Replit
# -------------------------
def area_calculation(width, height):
  area = width * height
  return area
def area_output(area):
  print("The area is %a square units." % area)
def measure_input():
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
    return width, height
def ending():
    width, height = measure_input()
    area = area_calculation(width, height)
    area_output(area)
ending()
