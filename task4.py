class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        grades_count = 0
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        result_ = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_str}\n' \
              f'Завершенные курсы: {finished_courses_str}'
        return result_

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        result_ = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return result_

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating

class Reviewer(Mentor):
        def __init__(self, name, surname):
            super().__init__(name, surname)
            self.name = name
            self.surname = surname
            self.courses_attached = []

        def rate_hw(self, student, course, grade):
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'

        def __str__(self):
            result_ = f'Имя: {self.name}\nФамилия: {self.surname}'
            return result_


# Лекторы и их курсы
best_lecturer_1 = Lecturer('Some1', 'Body1')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Some2', 'Body2')
best_lecturer_2.courses_attached += ['Java']

# Проверяющие и их курсы
cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('Any', 'Bud')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Java']

# Студенты их изучаемые и завершенные курсы
student_1 = Student('Ruoy', 'Eman')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Kolya', 'Novak')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

# Оценки лекторам
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Python', 6)
student_1.rate_hw(best_lecturer_2, 'Python', 1)

student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 8)

student_2.rate_hw(best_lecturer_2, 'Java', 9)
student_2.rate_hw(best_lecturer_2, 'Java', 10)


# Оценки студентам
cool_reviewer_1.rate_hw(student_1, 'Python', 7)
cool_reviewer_1.rate_hw(student_1, 'Python', 7)

cool_reviewer_2.rate_hw(student_2, 'Java', 5)
cool_reviewer_2.rate_hw(student_2, 'Java', 8)


print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}')
print()
print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}')
print()

print(f'Результат сравнения студентов (по средним оценкам за домашку): '
    f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
    f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')

# Списки студентов
student_list = [student_1, student_2]
# Список лекторов
lecturer_list = [best_lecturer_1, best_lecturer_2]

# функция для подсчета средней оценки за домашку

def student_rating(student_list, course_name):
  sum_all = 0
  count_all = 0
  for student_ in student_list:
     if student_.courses_in_progress == [course_name]:
          sum_all += student_.average_rating
          count_all += 1
  average_for_all = sum_all / count_all
  return average_for_all

# функция для подсчета средней оценки лекторов
def lecturer_rating(lecturer_list, course_name):
  sum_all = 0
  count_all = 0
  for lecturer_ in lecturer_list:
      if lecturer_.courses_attached == [course_name]:
          sum_all += lecturer_.average_rating
          count_all += 1
  average_all = sum_all / count_all
  return average_all

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
