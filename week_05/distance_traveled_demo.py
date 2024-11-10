
def distance_traveled(t):
    return  1/2 * 9.81 * t**2

test_1 = distance_traveled(5.5) == 148.37625
test_2 = distance_traveled(0) == 0
print(test_1, test_2)

