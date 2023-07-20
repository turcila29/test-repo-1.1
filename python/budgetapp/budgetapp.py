class Account:



    def __init__(self, category, funds):
        self.category = category
        self.funds = funds

    
    def addmoney(self, amount):
        if self.funds < amount:
            print("Not enough money")
        else:
            self.funds += amount
            print(f"You have successfuly moved {amount} to {self.category}" )
            print(f"New amount is {self.funds}")

    def transfer(self, amount, othercategory):
        if self.funds < amount:
            print("Not enough funds")
        else:
            self.funds -= amount
            othercategory.funds += amount
            print(f"Congratulations, {amount} was moved from {self.category} to {othercategory.category}")
            print(f"The new {self.category} fund is {self.funds}")
            print(f"The {othercategory} fund is {othercategory.funds}")


    def withdrawmoney(self, amount):
        if self.funds < amount:
                print("Not enough money")
        else:
                self.funds -= amount
                print(f"You have successfuly moved {amount} to {self.category} ")
                print(f"New amount is {self.funds}")


