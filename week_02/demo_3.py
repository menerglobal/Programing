sunny = True
print("sunny has type:", type(sunny))

temprature = 21
is_warm_outside = temprature >= 20
print("Is it warm?:", is_warm_outside)

should_go_to_beach = sunny or is_warm_outside
print("Go to beach?:", should_go_to_beach)
shouldnt_go_to_beach = not should_go_to_beach
print("shouldnt go?:", shouldnt_go_to_beach)
