__author__ = 'Justin'

dict = {}

for x in range(0, 10):
    for y in range(0, 10):
        for z in range (0, 10):
            dict[(x, y, z)] = 'whee'

print dict