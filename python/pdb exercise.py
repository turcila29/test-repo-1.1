#import pdb

#pdb.set_trace()

user_funds = 10.30
item_price = 5.99

if item_price < user_funds:
    print("You have enough money!")
if item_price == user_funds:
    print("You have the precise amount of money")
if item_price < user_funds:
    print("Sorry you don't have enough money")





    def product(n):
        total = 1
        for i in n:
            total *= i
        return total

print(product([4,4,5]))








def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
    return True




item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(i)
    n+=1

print (item_list[4])