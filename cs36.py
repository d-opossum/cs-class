# INCOMPLETE
# π/4 = 1 - 1/3 + 1/5 - 1/7 + . . .
def leibniz(n):
    pi = 0
    for i in range(1, n+1):
        pi += (-1)**(i+1)/(2*i-1)
    return 4*pi

input = int(input("Enter the number of iterations: "))
print(leibniz(input))
