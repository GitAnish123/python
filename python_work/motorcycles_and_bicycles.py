bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0])
print(bicycles[3])
print(bicycles[2])
print(bicycles[-3])
print(bicycles[-2].title())
bicycles = ['trek','cannondale','redline','specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
last_owned_sentence = f"The last motorcycle I owned was a {last_owned.title()}."
print(last_owned_sentence)
motorcycles = ['honda', 'yamaha', 'suzuki']
first_popped_motorcycles = motorcycles.pop(0)
print(first_popped_motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me!!!")
removing_ducati_reason = f"\nA {too_expensive.title()} is too expensive for me!!!"
print(removing_ducati_reason)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles[4])
# The print(motorcycles[4]) is wrong because the index is out of range.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles[-1])
# This one is right because this one is in range. The result will be 'ducati'
# Make sure your lists and your index are in range and in good sorted shape.