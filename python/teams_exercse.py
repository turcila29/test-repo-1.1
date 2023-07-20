with open ("teams.txt", "w") as file:
    for n in range (1):
        newline = "Chelsea" + "\n"
        file.write(newline)
        newline = "Dinamo" + "\n"
        file.write(newline)
        newline = "Arsenal" + "\n"
        file.write(newline)
        newline = "Juventus" + "\n"
        file.write(newline)
        newline = "Manchester United"  + "\n"
        file.write(newline)

file.close

file = open ("teams.txt", "r")

files = file.readlines()


print(files[0], files[3])

    
    


