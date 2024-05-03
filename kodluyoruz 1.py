from math import sqrt

points = [(3, 4), (5, 12), (8, 15), (7, 24)]
distances= []

def euclideanDistance(x, y):
    d=sqrt(((y[0]-x[0]) **2) + ((y[1]-x[1]) **2))
    return d

for x in points:
    for y in points:
        if x==y:
            continue
        else:
            distances.append(euclideanDistance(x, y))

print(min(distances))
