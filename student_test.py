class Student :
    grade = ''
    def __init__(self, line):
        name , gender , age , score = line.strip().split(',') #csv파일
        self.name = name
        self.gender = gender
        self.age = int(age)
        self.score = int(score)
    def __str__(self) :
        return "{} \t {} \t {} \t {} \t {}".format(self.name,self.gender,self.age,self.score, self.grade)
    
    def make_grade(self):
        grade_dict = {10 : 'A+', 9 :'A', 8 : 'B', 7 : 'C' , 6 : 'D' ,5:'F',4:'F',3:'F',2:'F',1:'F'}
        self.grade = grade_dict[ int(self.score) // 10]
                   
with open("student.csv","r",encoding="utf-8") as file :
    for idx , line in enumerate(file):
        if idx != 0 :
            print(Student(line))


from functools import reduce

class Students :
    def read_students(self) :
        self.stu = []
        with open("student.csv","r",encoding="utf-8") as file :
            for idx , line in enumerate(file):
                if idx != 0 :
                    self.stu.append(Student(line))
    def print_students(self) :
        for i in self.stu :
            print(i)
            
    def sorting_students(self) :
        self.stu = sorted(self.stu, key = lambda student  : student.score , reverse=True)
        
 
    def grading_students(self) :
        for i in self.stu :
            i.make_grade()

    def get_sum(self) :
        self.total = reduce(lambda x, y: (x if type(x) == int else x.score) + y.score, self.stu)
        self.avg = self.total / len(self.stu)
        print("총점 : {} \n 평균 :{}".format(self.total,self.avg))
        
    def print_above_avg(self) :
        s = filter(lambda x : x.score > self.avg , self.stu )
        for i in s :
            print(i) 


