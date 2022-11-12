class Member:
    def __init__(self , full_name ):
        self.full_name = full_name

    def introduce_massage(massage):
        return massage
class Student(Member):
    def __init__(self , full_name , reason_to_attending ):
        super().__init__(full_name )
        self.reason_to_attending = reason_to_attending

    def __str__(self):
        return f"{self.full_name} , {self.reason_to_attending}"


class Instructor(Member):
    def __init__(self, full_name, bio ):
        super().__init__(full_name)
        self.bio = bio 
        self.skills = []

    def __str__(self):
        return f"{self.full_name} , {self.bio}"


    def add_skill(self , new_skill):
        self.skills.append(new_skill)
    def show_skills(self):
        print(f"you skills are {self.skills}")


class Workshops:
    def __init__(self , date , subject):
        self.date = date
        self.subject = subject 
        self.instructors = []
        self.students = []

    def add_participant(self , member):
        if isinstance(member , Instructor):
            self.instructors.append(member)
        else:
            self.students.append(member)


    def print_details(self):
        print(f"workshop - {self.date} - {self.subject}")

        print("Students :")
        for student in self.students:
            print(student)
        print("instructor :")
        for instructor in self.instructors:
            print(f"{instructor} , ")
            for skill in instructor.skills:
                print(skill)

    def __str__(self) -> str:
        return f"{self.subject} in {self.date}"


workshop = Workshops("12/5/2022" , "study")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")

vicky.add_skill("html")
vicky.add_skill("css")
vicky.add_skill("javascript")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)

workshop.print_details()

