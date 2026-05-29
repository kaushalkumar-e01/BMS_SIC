n = int(input("enter number of pair of shoes: "))
p = int(input("enter how many pairs they can carry: "))

shoes_pair = {}

customer_earning  = 0

for i in range(n):
    shoes_name = input("enter shoes name: ").lower()
    shoes_price = int(input("enter the price of this shoes"))

    shoes_pair[shoes_name] = shoes_price

for j in range(p):
    choice = input("enter name of the shoes: ").lower()
    if choice in shoes_pair:
        customer_earning+=shoes_pair[choice]

    else:
        print("this shoes not in sale!!")

if customer_earning>=0:
    print("you have to pay ", customer_earning)

else:
    print("owner will pay you Rs", customer_earning*(-1))