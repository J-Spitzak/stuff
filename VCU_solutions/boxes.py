import math
from random import shuffle

boxes = [[5,7,6],[5,5,4],[3,4,3],[4,4,4]]
        

def configs(list):
    origin = list
    finalList = [origin]
    length = 0
    finalList.append([list[0],list[2],list[1]])
    finalList.append([list[1],list[2],list[0]])
    finalList.append([list[1],list[0],list[2]])
    finalList.append([list[2],list[1],list[0]])
    finalList.append([list[2],list[0],list[1]])
    return finalList



"""for box in configs(boxes):
            pass
"""

print(configs([1,2,3]))