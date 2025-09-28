dict ={
    "Alice":90,
    "John":80,
    "Abhudaya":100
}
a = input("Enter the student's name")
if a in dict:
    print(f"{a}'s marks: {dict[a]}")
else:
    print("Student not found")