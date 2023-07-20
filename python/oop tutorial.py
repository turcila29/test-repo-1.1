from abc import ABC, abstractclassmethod

class Bird(ABC):
    fly = True
    babies = 0

def noise(self):
    return "Squawk"

def reproduce(self):
    self.babies += 1

    @abstractclassmethod
    def eat(self):
        pass

    extinct = False


    class Owl(Bird):
        def reproduce(self):
            self.babies += 6

        def eat(self):
            return "Peck Peck"
        
    class Dodo(Bird):
        fly = False
        extinct = True

        def eat(self):
            return "Nom Nom"
        

        def reproduce(self):
            if not self.extinct:
                self.babies += 1
