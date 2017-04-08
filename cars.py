showroom = set()
showroom.add('Falcon')
showroom.add('Scout')
showroom.add('CJ-7')
showroom.add('Baja')
print(len(showroom))
showroom.add('Falcon')
print(showroom)
showroom.update(('Skylark', 'Land Cruiser'))
print(showroom)
showroom.discard('Land Cruiser')
print(showroom)
junkyard = set()
junkyard.update(('Focus', 'Pinto', 'Falcon', 'Scout', 'GTO', 'Jetta', 'Baja'))

cars_in_both = showroom.intersection(junkyard)
print(cars_in_both)

showroom = showroom.union(junkyard)
print(showroom)

showroom.discard('Pinto')
showroom.discard('Jetta')
print(showroom)


