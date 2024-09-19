class Teacher:
    def __init__(self, name):
        self.name = name
        self.schools = []

    def add_school(self, school):
        self.schools.append(school)


class School:
    def __init__(self, name):
        self.name = name
        self.professors = []

    def add_professor(self, professor):
        self.professors.append(professor)
        professor.add_school(self)


if __name__ == "__main__":
    teacher1 = Teacher("Dr. Silva")
    teacher2 = Teacher("Dr. Costa")

    school1 = School("Escola A")
    school2 = School("Escola B")

    school1.add_professor(teacher1)
    school1.add_professor(teacher2)

    school2.add_professor(teacher1)

    print("{} teaches at: {}".format(teacher1.name, [school.name for school in teacher1.schools]))
    print("{} teaches at: {}".format(teacher2.name, [school.name for school in teacher2.schools]))
