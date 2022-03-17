#test = [1,5,3,2,2,1,5]

def missing(list):
    for i in list:
        newList = list
        newList.remove(i)
        if i not in newList:
            return i

print(missing([1,5,3,2,2,1,5]))



