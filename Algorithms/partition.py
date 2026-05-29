def partition_array(numbers):
    pivot = numbers[-1]
    i = 0 #to access each element as reference element
    j = 0 #to know/find the index of the pivot element

    for i in range(len(numbers)-1):
        if numbers[i] < pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j +=1 

    numbers[-1], numbers[j] = numbers[j], numbers[-1]

#sorting by partition arrray