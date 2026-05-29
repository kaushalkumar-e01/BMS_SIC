n = int(input())

boys = list(map(int, input().split()))
girls = list(map(int, input().split()))

boys.sort()
girls.sort()

combined = []

if boys[0] <= girls[0]:
    for i in range(n):
        combined.append(boys[i])
        combined.append(girls[i])
else:
    for i in range(n):
        combined.append(girls[i])
        combined.append(boys[i])
        

is_possible = True
for i in range(len(combined) - 1):
    if combined[i] > combined[i + 1]:
        is_possible = False
        break


if is_possible:
    print("YES")
else:
    print("NO")