# Enter the wage: $15.50
# Enter the regular hours: 40
# Enter the overtime hours: 12

# The total weekly pay is $899.0
wage = float(input("Enter the wage: "))
hours = float(input("Enter the regular hours: "))
overtime = float(input("Enter the overtime hours: "))
reg = wage * hours
overT = (wage * 1.5) * overtime
total = reg + overT
print("The total weekly pay is $", total)