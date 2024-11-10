# Function to generate the first n powers of 2
def powers_of_two(n):
    return [2**i for i in range(1, n+1)]

# Test the function with different values of n
print(powers_of_two(1))   # For n = 1
print(powers_of_two(4))   # For n = 4
print(powers_of_two(10))  # For n = 10
