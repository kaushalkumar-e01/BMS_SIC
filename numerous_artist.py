ls1 = [1, 1, 3]
ls2 = [1, 2, 2, 3]

def checking_permutation(ls1, ls2):

    missing_numbers = []

    for i in set(ls1 + ls2):

        if ls1.count(i) != ls2.count(i):
            missing_numbers.append(i)

    if len(missing_numbers) == 0:
        print("Lists are permutations")
    else:
        print("Lists are not permutations")
        print("Numbers with unequal frequencies:", sorted(missing_numbers))

checking_permutation(ls1, ls2)