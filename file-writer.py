filename = input("Enter the filename : ")
test = open(filename, "r+")
print("what to read/write to file? \n 1| Array\n 2| 2D Array\n 3| read")
c = input(">> ")
if c == "1":
    array = ["test1", "test2", "test3"]
    test.write(str(array))
if c == "2":
    array2 = [["test0.5", "test1"], ["test1.5", "test2"]]
    test.write(str(array2))
if c == "3":
    text = test.read()
    print(text)