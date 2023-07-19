finalgrade = float(input("Please enter your final exam grade (/100): "))
assessment = float(input("Please enter your assessment grade (/50): "))
homework = float(input("Please enter your homework grade (/25): "))

def calculate(homework, assessment, finalgrade):
    homework = (homework / 25) * 100
    assessment = (assessment / 50) * 100
    total = (homework + assessment + finalgrade) / 3
    return total


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

gradeOverAll = calculate(homework, assessment, finalgrade)
print("Your final grade is: ", gradeOverAll)
print("Your final letter grade is: ", gradeLetter(gradeOverAll))  