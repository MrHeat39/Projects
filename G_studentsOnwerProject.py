students = {}

def addStudent():
    id = int(input("Enter id of student: "))
    name = input("Give this student name: ")
    age = int(input("How old is this student: "))
    grade = int(input("His note: "))
    students[id] = {"name": name, "age": age, "grade": grade}

while True:
    print("\nChoose one of these choices")
    print("1_Add student")
    print("2_Search student")
    print("3_Information of student")
    print("4_Exit")

    chose = int(input("Give number of your choice: "))

    if chose == 1:
        addStudent()

    elif chose == 2:
        id = int(input("Enter id to search: "))
        if id in students:
            print(students[id])
        else:
            print("This student is unavailable")

    elif chose == 3:
        id = int(input("Enter id to show info: "))
        if id in students:
            print(students[id])
        else:
            print("This student is unavailable")

    elif chose == 4:
        break
