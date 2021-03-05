# by Kami Bigdely
# Replace magic numbers with named constanst

# First Section
# Given two point charges, calcualte the electric force exerted on them.
coulumb_constant = 8.9875517923 * 1e9
q1 = int(input("Enter a value of charge q1: "))
q2 = int(input("Enter a value of charge q2: "))
distance = int(input("Enter the distance be10tween two charges: "))
force = coulumb_constant * q1 * q2 / (distance ** 2)
print("Electric Force between q1 and q2 is: ", force, "Newton")

# Second Section
modulus_even = 2
num = int(input("Enter an integer number: "))

if num % modulus_even == 0:
    print(num, "is an even number.")
print(num, "is an odd number.")
