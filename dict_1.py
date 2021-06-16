lexus = {
   'Make': 'Lexus',
   'Model': 'RX 350',
   'Year': '2015',
   'Engine': '3.5 L V6'
}


# print value with a key 'Model' from lexus dictionary
print(lexus['Year'])

# adding key-value pair to the dictionary
lexus['Doors'] = 4
print(lexus)

# adding new key-value pair to the dictionary
lexus['Color'] = 'red'
print(lexus)

# update the value from 2015 to 2021 where we have 'Year' key
lexus['Year'] = '2021'
print(lexus)

# delete a key-value pair by key 'Doors' from the dictionary
del lexus['Doors']
print(lexus)








