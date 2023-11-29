class Student:
    def __init__(self,name,rollno):
        self.name =  name
        self.rollno = rollno
        self.sub = self.Subjects()
    
    def showStudents(self):
        print("Student Details :", self.name, self.rollno,  self.sub)
    
    class Subjects:
        def __init__(self):
            self.subname =  "Science"
       
        def showSubjects(self):
            print(self.subname)
            
s1 = Student('Mike', 20)
print(s1.sub.subname)
s2 = s1.sub
s2.showSubjects()
s = Student.Subjects()
s.showSubjects()