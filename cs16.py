# Do not copy | My Personal Use Only 
# Originally on Replit
# ---------------------------
def user_input():
  radius = float(input("Enter the radius: "))
  return radius
def area_cal(radius):
  area = (3.14 * (pow(radius, 2)))
  return area
def output_area(area):
  print("The area is: %a" % area)
radius = user_input()
area = area_cal(radius)
output_area(area)
