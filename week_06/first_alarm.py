'''
water_levels = [1.52, 1.29, 1.18, 1.45, 1.63, 1.81, 1.95, 2.11, 2.09, 1.98, 1.30]

def fist_alarm(water_levels):
    for idx in range(1, len(water_levels)):
        if water_levels[idx] > 2.0:
            return idx
            print("Alarm at", idx)
        elif idx : 0
            if(water_levels[idx] - water_levels[idx - 1]) > 0.2 and water_levels[idx] > 1.5:
                        return idx
return -1
print(first_alarm(water_levels))
print(first_alarm([1,1,1,1]))
'''