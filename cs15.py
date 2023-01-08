# Do not copy | My Personal Use Only 
# Originally on Replit
# -------------------------------------
def userinput():
  base = float(input("Enter the base: "))
  height = float(input("Enter the height: "))
  return base, height
def area_cal(base, height):
  area = ((base * height) / 2)
  return area
def output_area(area):
  print ("The area is: %a square units." % area)
def ending():
  base, height = userinput()
  area = str(area_cal(base, height))
  output_area(area)
ending()
