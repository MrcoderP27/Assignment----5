try:
    Marks = {"Alice": 85, "Ram": 92, "John": 78, "Sam": 90}
    student = input("Enter the student's name: ")
    student = student.strip().lower().capitalize()
    print(f"{student}'s marks: {Marks[student]}")
except KeyError:
    print("Student not found.")