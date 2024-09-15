class Instructor:
    def __init__(self):
        self.__instructor_name = ""
        self.__technology_skill = []
        self.__experience = 0
        self.__avg_feedback = 0

    def set_technology_skill(self, technology_skill):
        self.__technology_skill = technology_skill

    def get_technology_skill(self):
        return self.__technology_skill

    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name

    def get_instructor_name(self):
        return self.__instructor_name

    def set_experience(self, experience):
        self.__experience = experience

    def get_experience(self):
        return self.__experience

    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback

    def get_avg_feedback(self):
        return self.__avg_feedback

    def check_eligibility(self):
        if self.__experience > 3:
            return self.__avg_feedback >= 4.5
        return self.__avg_feedback >= 4

    def allocate_course(self, technology):
        if not self.check_eligibility() or technology not in self.__technology_skill:
            return False
        return True

i1 = Instructor()
i1.set_avg_feedback(4.4)
i1.set_experience(4)
i1.set_instructor_name("A")
i1.set_technology_skill(['JAVA', 'PYTHON'])
print(i1.check_eligibility())
print(i1.allocate_course('PYTHON'))
