a = 0.0
theSum = 0.0
data = input("Enter a number: ")
while (data != ""):
    count = float(a+1)
    number = float(data)
    theSum += number
    a += 1
    theAvr = (theSum / a)
    data = input("Enter the next number: ")
print('''
The sum is {}
The average is {}
'''.format(theSum, theAvr))
