# finding Euclidian distance
pointA = (0,0)
pointB = (3,4)

print( pointA[0])

def distance(pointA, pointB):
    lenC = ((pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2)**0.5
    return lenC

dist = distance(pointA, pointB)
print(f'distance is {dist}')