x, y, z = float(input("Enter the first side: ")), float(input("Enter the second side: ")), float(input("Enter the third side: "))
if ((x**2 == y**2 + z**2) or (x**2 + y**2 == z**2) or (x**2 + z**2 == y**2)):
  print("The triangle is a right triangle.")
else:
  print("The triangle is not a right triangle.")
  