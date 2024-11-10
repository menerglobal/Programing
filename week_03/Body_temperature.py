t = 37.2


if (t == 35 or 35 > t ):
    bp = "Hypothermia"

elif (35 < t < 37.5 ):
    bp = "Normal"

elif (t == 37.5 or 37.5 < t < 40):
    bp = "Hyperthermia"

else:
    bp = "Hyperpyrexia"
    

print("The temperature", t, "is",  bp)

