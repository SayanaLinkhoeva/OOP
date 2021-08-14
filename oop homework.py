class Student:
    def __init__(self,name,surname,gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
        self.lecturer_grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Такого студента нет')
            return
        else:
            compare = self.average_grade() < other_student.average_grade()
            if compare:
                print(f'{self.name} {self.surname} учится хуже чем {other_student.name} {other_student.surname}')
            else:
                print(f'{self.name} {self.surname} учится лучше чем {other_student.name} {other_student.surname}')

    def average_grade(self):
        if not self.grades:
            print('не оценивается')
        else:
            list_ = []
            for i in self.grades.values():
                list_ += i
            return round((sum(list_) / len(list_)), 2)

    def __str__(self):
        some_student = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за дз: {self.average_grade()}\nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'
        return some_student



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            print('не оценивается')
        else:
            list_ = []
            for i in self.grades.values():
                list_ += i
            return round((sum(list_) / len(list_)), 2)

    def __str__(self):
        some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'
        return some_lecturer

    def __lt__(self,other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Такого лектора нет')
            return
        else:
            compare = self.average_grade() < other_lecturer.average_grade()
            if compare:
                print(f'{self.name} {self.surname} проводит лекции хуже, чем {other_lecturer.name} {other_lecturer.surname}')
            else:
                print(f'{self.name} {self.surname} проводит лекции лучше ,чем {other_lecturer.name} {other_lecturer.surname}')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return some_reviewer


best_student = Student('Ann', 'Nickole', 'female')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

some_student = Student('Ruoy', 'Eman', 'male')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

best_lecturer = Lecturer('Tom', 'Ford')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['Git']

some_lecturer = Lecturer('Some', 'Boddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

cool_mentor = Reviewer('Adam', 'Turner')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']
some_reviewer = Reviewer('Will', 'Smith')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 9)
some_reviewer.rate_hw(best_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 9)
cool_mentor.rate_hw(some_student, 'Python', 9.5)
cool_mentor.rate_hw(some_student, 'Python', 9)
cool_mentor.rate_hw(some_student, 'Git', 7)
cool_mentor.rate_hw(some_student, 'Python', 10)
cool_mentor.rate_hw(some_student, 'Git', 9)

best_student.rate_lecturer(best_lecturer, 'Python', 9)
best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(some_lecturer, 'Python', 9)
best_student.rate_lecturer(some_lecturer, 'Git', 8)
some_student.rate_lecturer(best_lecturer, 'Python', 10)
some_student.rate_lecturer(best_lecturer, 'Python', 8)
some_student.rate_lecturer(some_lecturer, 'Git', 9)
some_student.rate_lecturer(some_lecturer, 'Git', 7)

# print(best_student.grades)
# print(some_lecturer.grades)
print(f"{best_student.surname}'s средний балл за дз: {best_student.average_grade()}")
print(f"{some_student.surname}'s средний балл за дз: {some_student.average_grade()}")
print(f"{some_lecturer.surname}'s средний балл за лекции: {some_lecturer.average_grade()}")
print(f"{best_lecturer.surname}'s средний балл за лекции: {best_lecturer.average_grade()}")
print(some_reviewer)
print(some_lecturer)
print(some_student)
some_student > best_student
some_lecturer > best_lecturer


# def средняя оценка (список студентов и название курса)

def average_grade_hw(student_list, course):
    total_grades = []
    for student in student_list:
        if course in student.courses_in_progress and student.grades.get(course) is not None:
            total_grades += student.grades.get(course)
    if sum(total_grades) != 0:
        print(f'Общая средняя оценка за дз по {course} : {round(sum(total_grades) / len(total_grades), 2)}')
    else:
        print('Нет оценок')


def average_grade_lecturer(lecturer_list, course):
    total_grades = []
    for lecturer in lecturer_list:
        if course in lecturer.courses_attached and lecturer.grades.get(course) is not None:
            total_grades += lecturer.grades.get(course)
    if sum(total_grades) != 0:
        print(f'Общая средняя оценка за лекции по {course} : {round(sum(total_grades) / len(total_grades), 2)}')
    else:
        print('Нет оценок')

    # list_grade = 0
    # for student in student_list:
    #   for subject,grades in Student.grades.items():
    #      if subject == course :
    #         list_grade += sum(grades) / len(grades)
    # return round(list_grade / len(student_list), 2)


average_grade_hw([best_student, some_student], 'Python')
average_grade_hw([best_student, some_student], 'Git')
average_grade_lecturer([best_lecturer, some_lecturer], 'Python')
average_grade_lecturer([best_lecturer, some_lecturer], 'Git')
