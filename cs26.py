# Modify the following code

# Request the input
mass = float(input("Enter the object's mass: ")) 
velocity = float(input("Enter the object's velocity: "))  

# Compute the results
momentum = mass * velocity

ke = ((mass * pow(velocity, 2)) / 2)
# Display the results
print('''
The object's momentum is {} 
The object's kinetic energy is {}
'''.format(momentum, ke))