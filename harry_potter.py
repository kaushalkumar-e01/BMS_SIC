N = int(input("number of gold coins in harry potter's bag: "))
N_value = []
print("enter value of harry potter coins")
for i in range(N):
    n = int(input(f'enter coin {i+1} value: '))    #for this another method => N_value = [int(i) for i in input("enter coins value:").split()]
    N_value.append(n)

Q = int(input("enter number of instructions to harry: "))

X = int(input("At what amount monk will sleep:"))         
monk_bag = []


print("enter instructions:\n harry/remove")

for i in range(Q):
    instruction = input(f"instruction {i+1}: ").lower()
    if instruction == 'harry':
        monk_bag.append(N_value[0])
        N_value.pop(0)

    elif instruction == 'remove':
        monk_bag.pop()

    else:
        print("invalid input...your chance is gone!")

    if sum(monk_bag)==X:
        print(f"Harry potter wins!!\nno. of coins in monk's bag: {len(monk_bag)}")
        break 
else:
    print("harry loses!!")