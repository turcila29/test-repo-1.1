class Account:



    def __init__(self, category, funds=0):
        self.category = category
        self.funds = funds

    
    def addmoney(self, amount):
        if self.funds < amount:
            print("Not enough money")
        else:
            self.funds -= amount
            print("You have successfuly moved {amount} to {self.category} ")
            print("New amount is {self.funds}")

    def transfer(self, amount, othercategory):
        if self.funds < amount:
            print("Not enough funds")
        else:
            self.funds -= amount
            othercategory.funds += amount
            print(" Congratulations, {amount} was moved from {self.category} to {othercategory.category}")
            print("The new {self.category} fund is {self.fund}")
            print("The {other_category} fund is {othercategory.fund}")


    def withdrawmoney(self, amount):
        if self.funds < amount:
                print("Not enough money")
        else:
                self.funds -= amount
                print("You have successfuly moved {amount} to {self.category} ")
                print("New amount is {self.funds}")


