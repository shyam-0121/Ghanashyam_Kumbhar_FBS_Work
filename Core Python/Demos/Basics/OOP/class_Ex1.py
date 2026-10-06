class Student:
    def __init__(self,id, name, branch, marks):
        self.id = id
        self.name = name
        self.branch = branch
        self.marks = marks

    def getId(self):
        return self.id
    def setId(self,newId):
        self.id = newId

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName

    def getBranch(self):
        return self.branch
    def setBranch(self,newBranch):
        self.branch = newBranch

    def getMarks(self):
        return self.marks
    def setMarks(self,newMarks):
        if 0 <= newMarks <=100:
            self.marks = newMarks
        else:
            print('Invalid Marks')


    def __str__(self):
        return f'Id: {self.id} Name: {self.name} Branch: {self.branch} Marks: {self.marks}'

stud = Student(1,'Neymar','BCA',87)
print(stud)
print(stud.getId())
print(stud.getName())
print(stud.getBranch())
print(stud.getMarks())
stud.setId(12)
stud.setName('Shyam')
stud.setBranch('BCS')
stud.setMarks(80)
print(stud)