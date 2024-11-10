'''
#Code 4.1: Print song lyrics
for i in range(72):
    print("Around the world, around the world")
#Code 4.2: Printing all numbers
text = ""
for n in range(1,21):
    text = text + str(n) + " "
    print("")  
print(text)
#Code 4.3: Sum of numbers
current_sum = 0
for element in range(1, 6):
    current_sum = current_sum + element
print(current_sum)


#Code 4.4: Geometric cake
'''
def cake_eating_simulation():
    cake_left = 50.0
    for day in range(1, 100):  # Large range, loop will break early
        if cake_left < 1:
            print(f"There is less than 1 pct cake left on day {day}")
            break
        
        print(f"There is {cake_left:.1f} pct cake left on day {day}")
        cake_left /= 2  # Eat half of what's left each day
