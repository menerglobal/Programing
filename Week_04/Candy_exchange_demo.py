candies = 36
eaten = 0

while candies >= 5:
    candies = candies - 5 + 1
    eaten = eaten + 5
    print("I have eaten", eaten, "and I have", candies, "candies left.")

eaten = eaten + candies
candies = 0
print("Total eaten", eaten)
