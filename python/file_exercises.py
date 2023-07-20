file = open("/Users/andreiturcila/test-repo-1.1/test-repo-1.1/python/interestingfile.txt", "r")

outfile = ""

for line in range(1, 10):
    if line % 2 == 0:
        outfile += file.readline()

    else:
        file.readline()


file = open("/Users/andreiturcila/test-repo-1.1/test-repo-1.1/python/interestingfile.txt", "w")
file.write(outfile)
file.close()

