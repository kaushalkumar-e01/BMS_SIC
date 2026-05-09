ls = [45, 34, 13, 55, 9, 77, 22, 35, 99]
for i in range(len(ls)):
    element = ls[i]
    index = i
    for j in range(i+1, len(ls)):
        if element > ls[j]:
            element = ls[j]
            index = j
            
    ls[i], ls[index] = ls[index], ls[i]

print(ls)