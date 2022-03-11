from ast import NotIn
import math
from random import randint

boxes = [[5,7,6],[5,5,4],[3,4,3],[4,4,4]]

def shuffle(list):
    finalList = list
    run = True
    while run:
        z_list = []
        ind = 0
        for item in list:
            z = randint(0,len(list))
            z_list.append(z)
            if z not in z_list:
                finalList[z] = item
    return finalList
        

def configs(list):
    
    while length < math.factorial(len(list)):
        newList = []
        
        shuffle(list)



for box in configs(boxes):
            pass
