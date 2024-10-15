class Student:
    time_table = {
        # class variable
        "Thursday": {
            1: "DBMS(PP)",
            2: "Python PP)",
            3: "DAA(PP)" 
        },
        "Friday": {
            1: "DBMS(PP)",
            2: "DAA(PP)",
            3: "Python PP)",
            4: "DBMS(PR)",
            5: "DAA(PR)"
        },
        "Saturday": {

        }
    }

    def __init__(self, name, course, age, gender, stu_id):
        self.name = name
        self.course = course
        self.age = age
        self.gender = gender
        self.stu_id = stu_id

    def __str__(self):
        return f"{self.name} is in {self.course}"
    
    @property # getter function
    def course(self):
        return self._course

    @course.setter  # setter function
    def course(self, new_course): 
        self._course = new_course

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("No name provided")
        self._name = name

    @property
    def gender(self):
        return self.gender
    
    @gender.setter
    def gender(self, gender):
        if gender not in ["M", "F"]:
            raise ValueError("Genders other than 'M' and 'F' are not allowed")
        self._gender = gender

    # using class method
    @classmethod
    def issue_time_table(cls, day):
        return cls.time_table[day.capitalize()]


def get_student():
    name = input("What's your name? ").capitalize()
    stu_id = input("What is your admission no.? ")
    course = input("What's your course name? ").capitalize()
    age = int(input("What's your age? "), base=10)
    gender = input("What is your gender M or F?  ").upper()

    return Student(name, course, stu_id=stu_id, age=age, gender=gender)

def main():
    student = get_student()
    print(student.issue_time_table("Thursday")) # type: ignore


if __name__ == "__main__":
    main()
