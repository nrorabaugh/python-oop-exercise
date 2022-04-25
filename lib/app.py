# Write your code here!
class Member: 
    def __init__(self, name):
        self.full_name=name 
    
    def introduce(self):
        print(f'Hi, I\'m {self.full_name}!')

class Student(Member):
    def __init__(self, name, reason):
        super().__init__(name)
        self.reason=reason

payvand = Student('Payvand', 'Money')

class Instructor(Member):
    def __init__(self, name, bio, skillset):
        super().__init__(name)
        self.bio=bio
        self.skillset=skillset

    def add_skill(self, skill):
        self.skillset.append(skill)

brandon=Instructor('Brandon', 'I am a genius', ['React', 'Node', 'C'])

class Workshop():
    def __init__(self, date, subject, instructors, students):
        self.date=date
        self.subject=subject
        self.instructors=instructors
        self.students=students
    
    def add_participant(self, participant):
        if participant.__class__.__name__ == 'Instructor':
            self.instructors.append(participant)
        if participant.__class__.__name__ == 'Student':
            self.students.append(participant)

    def print_details(self):
        print(f'Date: {self.date}\nSubject: {self.subject}\n')
        print('Instructors:')
        for i in self.instructors:
            print(f'\n{i.full_name}\n{i.bio}')
            print('Skills:')
            for r in i.skillset:
                print(r)

        print('\nStudents:')
        for s in self.students:
            print(f'\n{s.full_name}\n{s.reason}\n')

sei=Workshop('12/12/19', 'SEI', [], [])
sei.add_participant(brandon)
sei.add_participant(payvand)
sei.print_details()


"""
workshop = Workshop("12/03/2014", "Shutl", [], [])

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.", ['React', 'Node', 'C'])
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love", ['React', 'Node', 'C'])
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
"""