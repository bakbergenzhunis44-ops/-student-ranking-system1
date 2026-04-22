class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"{self.name} - {self.gpa}"


def main():
    students = [
        Student("Aruzhan", 3.5),
        Student("Dias", 3.9),
        Student("Ali", 2.8),
        Student("Aikhanym", 3.7)
    ]

    # GPA бойынша сұрыптау (үлкеннен кішіге)
    students.sort(key=lambda s: s.gpa, reverse=True)

    print("📊 Student Ranking:\n")
    for student in students:
        print(student)


if __name__ == "__main__":
    main()
