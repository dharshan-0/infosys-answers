class Student:
    def __init__(self):
        self.__student_id = 0
        self.__marks = 0
        self.__age = 0

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