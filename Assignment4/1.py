import os

if os.path.exists("sample.txt"):
    print("This is a sample text file")
    f = open("sample.txt")
    data = f.readline()
    print(data)
    f.close()
else:
    print("The file 'sample.txt' was not found")
    