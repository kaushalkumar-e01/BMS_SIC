
n = int(input("enter a number: "))

sum=0
while n!=0:
    sum+=(n%10)
    n = n//10
    if sum>9 and n==0:
        n=sum
        sum=0

print(f"lucky digit of number you entered = {sum}")

