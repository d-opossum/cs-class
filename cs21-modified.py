def fixed():
  taxRate = 0.20
  stdDed = 10000.0
  depDed = 3000.0
  return (taxRate, stdDed, depDed)
def user_input():
  grossInc = float(input("Enter the gross income: "))
  numDep = int(input("Enter the number of dependents: "))
  return (grossInc, numDep)
def compute_tax(grossIncome, numDependents):
  taxRate, stdDed, depDed = fixed()
  grossInc, numDep = user_input()
  taxInc = grossIncome - stdDed - \
                depDed * numDep
  incomeTx = round((taxInc * taxRate), 2)
  return incomeTx
def output_incometx(incomeTx):
  print("The income tax is $" + str(incomeTx))
def ending():
  grossInc, numDep = user_input()
  incomeTx = compute_tax(grossInc, numDep)
  output_incometx(incomeTx)
ending()
