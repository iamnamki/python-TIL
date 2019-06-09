'''
s = Students()

# 1. 파일에서 학생정보를 읽는 메소드
s.read_students()

# 2. 학생정보를 출력하는 메소드
s.print_students('2. 학생정보')

# 3. 학생정보를 성적순으로 sorting하는 메소드 (sort)
s.sorting_students()
s.print_students('3. sorting ') #sorting이 되었는지 확인

# 4. 학생 성적으로 학점 매기는 메소드 (map, lambda)
s.grading_students()
s.print_students('4. 학점 확인')  #학점이 잘 들어갔는지 확인

# 5. 전체 학생의 총점과 평균을 구하는 메소드. (reduce,lambda)
s.get_sum()

# 6. 평균 이상인 학생정보를 출력하는 메소드 (filter, lambda)
s.print_above_avg() (edited) '''


class Students : 

    def __init__(self, line):
        return line

    def read_students(self, line) :
        name , gender , age , score = line.strip().split(',') #csv파일
        self.name = name
        self.gender = gender
        self.age = int(age)
        self.score = int(score)

    def print_students(self) :
        return "{} \t {} \t {} \t {} \t {}".format(self.name,self.gender,self.age,self.score)

    def sorting_students(self) :
        self.result = 0
        return self.result 

    def grading_students(self) :
        self.result = 0
        return self.result 

    def get_sum(self) :
        self.result = 0
        return self.result 

    def print_above_avg(self) :
        self.result = 0
        return self.result 







class Student(Students) :

    def __init__(self, line):
        return super().__init__(line) 
