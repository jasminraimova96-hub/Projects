class Student:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
class Subject:
    def __init__(self, name):
        self.name = name
        self.students = []
    def __add__(self, s):
        self.students.append(s)
        return self
    def __sub__(self, s):
        self.students.remove(s)
        return self
    def __call__(self):
        print(self.name, self.students)
    def __lt__(self, other):
        return len(self.students) < len(other.students)
    def __getitem__(self, i):
        return self.students[i]
s1, s2 = Student("Mahmud"), Student("Olga")
math = Subject("Math")
physics = Subject("Physics")
math + s1 + s2
physics + s1
math()
print(math < physics, math[0])
