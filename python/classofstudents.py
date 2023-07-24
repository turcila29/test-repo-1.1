class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
      
"""
a class that identifies students by age and name

"""


John = Student("John", "21")
Jane = Student("Jane", "22") 

print(getattr(John, "age"))

test3 = float(input("Please enter your first assessment grade (/100): "))
test2 = float(input("Please enter your second assessment grade (/100: "))
test1 = float(input("Please enter your third assessment grade (/100): "))
"""

this is an input for the grades

"""


def calculate(test1, test2, test3: int) -> int:
    test1 = (test1 / 100) * 100
    test2 = (test2 / 100) * 100
    test3 = (test3 / 100) *100
    total = (test1 + test2 + test3) / 3
    return total
"""
function for calculating the scores of the tests
"""

def gradeLetter(gradeOverAll):
    if gradeOverAll >= 90:
        return "A"
    elif gradeOverAll >= 80:
        return "B"
    elif gradeOverAll >= 70:
        return "C"
    elif gradeOverAll >= 60:
        return "D"
    else:
        return "F"
"""
function that converts the grades from numbers to letters
"""
gradeOverAll = calculate(test1, test2, test3)
print("Your final grade is: ", gradeOverAll)
print("Your final letter grade is: ", gradeLetter(gradeOverAll))  