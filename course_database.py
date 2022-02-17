import sys


class User:
    def __init__(self, name):
        self.user_name = name
        self.user_courses_dict = {}

    def join_course(self, courses_list):
        if len(self.user_courses_dict) == 0:
            print('На какой курс зачислить?')
            i = 1
            for course in courses_list:
                print(str(i) + '). ' + str(course.course_name))
                i += 1
            choice_3 = input('Ваш выбор: ')
            print()
            self.user_courses_dict[courses_list[int(choice_3) - 1]] = 'нет оценки'
        else:
            temporary_user_courses_list = []
            approved_courses_list = []
            for course in self.user_courses_dict.keys():
                temporary_user_courses_list.append(course)
            for course in courses_list:
                if course not in temporary_user_courses_list:
                    approved_courses_list.append(course)
            if len(courses_list) == len(self.user_courses_dict):
                print('Нет доступных курсов для записи данного пользователя.\n')
            else:
                print('На какой курс зачислить?')
                i = 1
                for course in approved_courses_list:
                    print(str(i) + '). ' + str(course.course_name))
                    i += 1
                choice_3 = input('Ваш выбор: ')
                print()
                self.user_courses_dict[approved_courses_list[int(choice_3) - 1]] = 'нет оценки'


class Student(User):
    def __init__(self, name):
        super().__init__(name)

    def show_courses_and_marks(self):
        if len(self.user_courses_dict) == 0:
            print('\nЗачислите данного студента на курсы.\n')
        else:
            i = 1
            for course, mark in self.user_courses_dict.items():
                print(str(i) + '). Курс: ' + str(course.course_name) + ', оценка: ' + str(mark))
                i += 1
            print()


class Teacher(User):
    def __init__(self, name):
        super().__init__(name)

    def show_courses(self):
        if len(self.user_courses_dict) == 0:
            print('\nЗачислите данного преподавателя на курсы.\n')
        else:
            i = 1
            for course in self.user_courses_dict.keys():
                print(str(i) + '). Курс: ' + str(course.course_name))
                i += 1
            print()


class Course:
    def __init__(self, name):
        self.course_name = name


class Interface():

    def create_user(self, teachers_list, students_list):
        print('Какая роль?')
        print('1). Преподаватель.')
        print('2). Студент.')
        choice_2 = int(input('Ваш выбор: '))
        if choice_2 == 1:
            name = input('\nВведите имя преподавателя: ')
            print()
            teacher = Teacher('Преподаватель ' + name)
            teachers_list.append(teacher)
        elif choice_2 == 2:
            name = input('\nВведите имя студента: ')
            print()
            student = Student('Студент ' + name)
            students_list.append(student)

    def create_course(self, courses_list):
        name = input('\nВведите название курса: ')
        print()
        course = Course(name)
        courses_list.append(course)

    def interface_join_course(self, teachers_list, students_list, courses_list):
        if len(students_list) == 0 and len(teachers_list) == 0:
            print('\nДобавьте пользователей.\n')
        if len(courses_list) == 0:
            print('\nДобавьте курсы.\n')
        else:
            print('\nКого зачислить на курс?')
            i = 1
            if len(teachers_list) > 0:
                for teacher in teachers_list:
                    print(str(i) + ').' + str(teacher.user_name))
                    i += 1
            if len(students_list) > 0:
                for student in students_list:
                    print(str(i) + ').' + str(student.user_name))
                    i += 1
            choice_3 = input('Ваш выбор: ')
            if len(teachers_list) > 0:
                if int(choice_3) - 1 < len(teachers_list):
                    teachers_list[int(choice_3) - 1].join_course(courses_list)
            if len(students_list) > 0:
                if int(choice_3) - 1 >= len(teachers_list):
                    students_list[int(choice_3) - len(teachers_list) - 1].join_course(courses_list)

    def get_mark(self, students_list):
        if len(students_list) == 0:
            print('\nДобавьте студентов.\n')
        else:
            i = 1
            print('Кому поставить оценку?')
            for student in students_list:
                print(str(i) + ').' + str(student.user_name))
                i += 1
            choice_5 = input('Ваш выбор: ')
            if len(students_list[int(choice_5) - 1].user_courses_dict) == 0:
                print('\nЗачислите данного студента на курсы.\n')
            else:
                print('По какому курсу поставить оценку?')
                i = 1
                temporary_list = []
                for course in students_list[int(choice_5) - 1].user_courses_dict.keys():
                    print(str(i) + ').' + str(course.course_name))
                    temporary_list.append(course)
                    i += 1
                choice_6 = input('Ваш выбор: ')
                mark = input('Введите оценку за курс: ')
                print()
                students_list[int(choice_5) - 1].user_courses_dict[temporary_list[int(choice_6) - 1]] = mark

    def show_teacher_courses(self, teachers_list):
        if len(teachers_list) == 0:
            print('\nДобавьте преподавателей.\n')
        else:
            i = 1
            print('Чьи данные вывести?')
            for teacher in teachers_list:
                print(str(i) + ').' + str(teacher.user_name))
                i += 1
            choice_7 = input('Ваш выбор: ')
            teachers_list[int(choice_7) - 1].show_courses()

    def show_student_courses_and_marks(self, students_list):
        if len(students_list) == 0:
            print('\nДобавьте студентов.\n')
        else:
            i = 1
            print('Чьи данные вывести?')
            for student in students_list:
                print(str(i) + ').' + str(student.user_name))
                i += 1
            choice_8 = input('Ваш выбор: ')
            students_list[int(choice_8) - 1].show_courses_and_marks()

    def show_users(self, teachers_list, students_list):
        if len(students_list) == 0 and len(teachers_list) == 0:
            print('\nДобавьте пользователей.\n')
        else:
            i = 1
            if len(teachers_list) > 0:
                for teacher in teachers_list:
                    print(str(i) + ').' + str(teacher.user_name))
                    i += 1
            if len(students_list) > 0:
                for student in students_list:
                    print(str(i) + ').' + str(student.user_name))
                    i += 1
            print()


if __name__ == '__main__':
    students_list = []
    teachers_list = []
    courses_list = []
    interface = Interface()
    flag = True
    while flag:
        i = 1
        print('Что вы хотите сделать?')
        print(str(i) + '). Создать пользователя.')
        i += 1
        print(str(i) + '). Создать курс.')
        i += 1
        print(str(i) + '). Зачислить пользователя на курс.')
        i += 1
        print(str(i) + '). Выставить итоговую оценку по курсу.')
        i += 1
        print(str(i) + '). Вывести список курсов преподавателя.')
        i += 1
        print(str(i) + '). Вывести список курсов студента с оценками.')
        i += 1
        print(str(i) + '). Вывести список всех пользователей.')
        i += 1
        print(str(i) + '). Выход.\n')
        choice_1 = input('Ваш выбор: ')
        if int(choice_1) == 1:
            interface.create_user(teachers_list, students_list)
        elif int(choice_1) == 2:
            interface.create_course(courses_list)
        elif int(choice_1) == 3:
            interface.interface_join_course(teachers_list, students_list, courses_list)
        elif int(choice_1) == 4:
            interface.get_mark(students_list)
        elif int(choice_1) == 5:
            interface.show_teacher_courses(teachers_list)
        elif int(choice_1) == 6:
            interface.show_student_courses_and_marks(students_list)
        elif int(choice_1) == 7:
            interface.show_users(teachers_list, students_list)
        elif int(choice_1) == 8:
            flag = False
    sys.exit()
