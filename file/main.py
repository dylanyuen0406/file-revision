with open("./file/important.txt") as f:
    impt = f.read()


list1 = impt.split('\n')
print(list1)

with open("./file/important.txt", "w") as f:
    f.write("This file has been overwritten")