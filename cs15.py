# Do not copy | My Personal Use Only 
# Originally on Replit
# -------------------------------------
def userinput():
  base = float(input("Enter the base: "))
  height = float(input("Enter the height: "))
  return base, height
def area_cal():
  base, height = userinput()
  area = ((base * height) / 2)
  return area
def output_area():
  area = str(area_cal())
  print ("The area is: %a square units." % area)
output_area()
