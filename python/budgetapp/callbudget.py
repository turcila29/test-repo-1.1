from budgetapp import Account


if __name__ == "__main__":
    food = Account("Food", 200)
    clothing = Account("Clothing", 300)
    entertainment = Account("Entertainment", 400)

    print(f"{food.category} fund is {food.funds}")
    print(f"{clothing.category} fund is {clothing.funds}")
    print(f"{clothing.category} fund is {clothing.funds}")
    print()

    food.withdrawmoney(10000)
    clothing.addmoney(20)
    entertainment.addmoney(3000)
    food.transfer(50, clothing)