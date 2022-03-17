def smart(sum,difference):
    if difference > sum:
        return "impossible"
    for i in range(sum):
        for j in range(sum):
            if (i + j) == sum and abs(i - j) == difference:
                return [i,j]

print(smart(20,40))