nitrate_level = 55.0

if (nitrate_level == 4.00 or nitrate_level < 4.0):
    nl = "Very low"

elif (4.00 < nitrate_level < 9.00):
    nl = "Low"

elif (9.00 < nitrate_level < 40.0):
    nl = "Normal"

elif (40.00 < nitrate_level < 50.0):
    nl = "High"

else :
    nl = "Very high"

print("The nitrate level", nitrate_level, "mg/l is", nl)
