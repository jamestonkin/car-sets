showroom = {'Nissan', 'Toyota', 'Audi', 'Honda'}

print (len(showroom))

showroom.add('Toyota')
print (showroom)

showroom.update({'Ford', 'Chevy'})
print(showroom)

showroom.discard('Honda')
print(showroom)

junkyard = {'GM', 'Chrysler', 'Ford', 'Chevy'}
new_set = set(showroom) & set(junkyard)
print(new_set)

showroom = set(showroom) | set(junkyard)
print(showroom)

showroom.discard('Chrysler')
print(showroom)
