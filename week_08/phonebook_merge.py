phonebook = {'Liv': ['55511112', '18777890'] ,
              'Mads': ['27274445', '48533336'],
              'Steve': ['45455555', '25455525']}

second_phonebook = {'Anna': ['89577772'] ,
                     'Steve': ['25257755', '25455525'],
                     'Mads': ['48533336', '27274445']}

for name in second_phonebook:
    if name in phonebook:
        list1 = phonebook[name]
        list2 = second_phonebook[name]
        print("List 1 before update")
        for number in list2:
            if not (number in list1):
                list1.append(number)
    else:
        phonebook[name] = second_phonebook[name]

print(phonebook)