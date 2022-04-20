def scalar(vector, factor):
    final_vec = []
    try:
        for i in vector:
            final_vec.append(int(i) * int(factor))
    except:
        return "no floating point values"

    return final_vec

vector = input().split()
factor = input()

print(scalar(vector, factor))