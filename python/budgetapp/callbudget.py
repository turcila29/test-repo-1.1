from budgetapp import Account


if __name__ == "__main__":
    food = Account("Food", 50)
    clothing = Account("Clothing", 100)
    entertainment = Account("Entertainment", 150)

    print(f"{food.category} fund is {food.funds}")
    print(f"{clothing.category} fund is {clothing.funds}")
    print(f"{clothing.category} fund is {clothing.funds}")
    print()

    food.withdrawmoney(5000)
    clothing.addmoney(50)
    entertainment.addmoney(100)

    food.transfer(5, clothing)