l1 = []
l2 = []

def shorter(a, b):
    if len(a) <= len(b):
        return a
    return b

def longer(a, b):
    if len(a) <= len(b):
        return b
    return a

short = shorter(l1,l2)
long = longer(l1,l2)
ind = 0
count = 0
for i in short:
    if i == longer[ind]:
        count += 1
    ind += 1 
final = count / len(short)