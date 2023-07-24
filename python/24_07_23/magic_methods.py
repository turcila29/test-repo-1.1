class Dog():
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    
    def __str__(self) -> str:
        return f"a {self.age}-year-old {self.breed} called {self.name}"


    def __bool__(self):
        return self.breed != ""


if __name__ == '__main__':
    fido = Dog('fido', 5, 'labrador')  # Dog.__new__() gets called and returned dog is passed to Dog.__init__(...)
    print(fido)
