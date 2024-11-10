d = 170
s = 150

#is_prehigh_or_lower = (s < 140 and d < 90)
#is_prehigh = is_prehigh_or_lower and (s > 120 or d > 80)

#print("is_prehigh", is_prehigh)
#print("is_prehigh_or_lower", is_prehigh_or_lower)

if (s < 90 and d < 60):
    bp = "Low"
elif (s < 120 and d < 80):
    bp = "Normal"
elif ( s < 140 and d < 90):
    bp = "Prehigh"
elif (s < 160 and d < 100):
      bp = " Stage 1 high"
else:
    bp ="Stage 2 high"


print("Blood pressure is", bp)
