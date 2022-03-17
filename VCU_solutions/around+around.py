sides = 3
#test = {[0,0] : 1,[1,0] : 2, [2,0] : 3,"""row 2"""[0,1] : 4,[1,1] : 5, [2,1] : 6,"""row 3"""[0,2] : 7,[1,2] : 8, [2,2] : 9}

test2 = {1 : [0,0],2 : [1,0], 3 : [2,0],4 : [0,1],5 : [1,1], 6 : [2,1],7 : [0,2],8 : [1,2], 9 : [2,2]}

value_list = test2.keys()
cordonite_list = test2.values()

def solve(value_list, cordonite_list, sides):
    final = []
    offset = 0 #controls offset when perimeters have been deleted

    while sides > 0:
        for x in range(offset,offset + (sides - 1)): #top
            pos = cordonite_list.index([x,offset])
            final.append(value_list[pos])
            
        for y in range(offset,offset + (sides-1)): #right
            pos = cordonite_list.index([sides - (offset + 1),y])
            final.append(value_list[pos])
            
        temp = []
        for x in range(offset,offset + sides): #bottom
            pos = cordonite_list.index([x,offset + sides - 1])
            temp.append(value_list[pos])
        temp.reverse()
        for thing in temp:
            final.append(thing)

        othtemp = []
        for y in range(offset + 1,offset + (sides - 2)): #left
            pos = cordonite_list.index([0,y]) 
            othtemp.append(value_list[pos])
        othtemp.reverse()
        for thingy in othtemp:
            final.append(thingy)  
        
        sides -= 2
        offset += 1


    return final

print(solve(value_list,cordonite_list, sides))