#Enter the starting salary: $30000
#Enter the annual % increase: 2
#Enter the number of years: 10
import decimal
starting_salary = int(input("Enter the starting salary: "))
percentage_inc = float(input("Enter the annual % increase: "))
number_years = int(input("Enter the number of years: "))
print("\nYear   Salary\n-------------")
deced = decimal.Decimal(str(starting_salary))
num_base = str(1) + "    " +'$'+ str (deced.quantize(decimal.Decimal('.01'), decimal.ROUND_HALF_DOWN)) + '\n'
print(num_base)
for number_years in range(1,number_years):
  starting_salary = (starting_salary + (starting_salary*percentage_inc)/100)
  deced = decimal.Decimal(str(starting_salary))
  num = (str(number_years+1) + "    " +'$'+ str (deced.quantize(decimal.Decimal('.01'), decimal.ROUND_HALF_DOWN)) + '\n')
  print(num)
