class Student:
    def __init__(self):
        self.__student_id = 0
        self.__marks = 0
        self.__age = 0
        self.__course_id = None
        self.__fees = None

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id

    def set_marks(self, marks):
        self.__marks = marks

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def get_marks(self):
        return self.__marks

    def get_course_id(self):
        return self.__course_id

    def get_fees(self):
        return self.__fees

    def validate_marks(self):
        if self.__marks >= 0 and 100 >= self.__marks:
            return True
        return False

    def validate_age(self):
        if self.__age > 20:
            return True
        return False

    def check_qualification(self):
        if not self.validate_age() or not self.validate_marks():
            return False
        if self.__marks >= 65:
            return True
        return False

    def choose_course(self, course_id):
        avaliable_courses = [1001, 1002]
        fees = {1001: 25575.0, 1002: 15500.0}
        if course_id not in avaliable_courses:
            return False
        
        self.__course_id = course_id
        self.__fees = fees[course_id]
        
        if self.__marks > 85:
            self.__fees = 25 / 100 * self.__fees
        return True


maddy=Student()
maddy.set_student_id(1004)
maddy.set_age(21)
maddy.set_marks(89)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1001)):
        print("Course allocated")
        print(maddy.get_fees())
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")