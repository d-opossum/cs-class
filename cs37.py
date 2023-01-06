# INCOMPLETE
#Enter the starting salary: $30000
#Enter the annual % increase: 2
#Enter the number of years: 10
import decimal
starting_salary = int(input("Enter the starting salary: "))
percentage_inc = float(input("Enter the annual % increase: "))
number_years = int(input("Enter the number of years: "))
print("\nYear   Salary\n-------------")
for number_years in range (number_years):
  num = (str(number_years+1) + "    " +'$'+ str (starting_salary))
  print(num)
  starting_salary = decimal(round((starting_salary + (starting_salary*percentage_inc)/100), 2))
