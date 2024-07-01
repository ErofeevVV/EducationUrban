grades = [[5, 3, 3, 5, 4, 5, 3],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 2],
          [5, 5, 5, 4, 5]]
students = {'Johnny',
            'Bilbo',
            'Steve',
            'Khendrik',
            'Aaron'}

student_1_point = grades[0]
total_points_student_1 = sum(student_1_point)
number_of_ratings_student_1 = len(student_1_point)
gta_student_1 = round(total_points_student_1 / number_of_ratings_student_1, 2)

student_2_point = grades[1]
total_points_student_2 = sum(student_2_point)
number_of_ratings_student_2 = len(student_2_point)
gta_student_2 = round(total_points_student_2 / number_of_ratings_student_2, 2)

student_3_point = grades[2]
total_points_student_3 = sum(student_3_point)
number_of_ratings_student_3 = len(student_3_point)
gta_student_3 = round(total_points_student_2 / number_of_ratings_student_3, 2)

student_4_point = grades[3]
total_points_student_4 = sum(student_4_point)
number_of_ratings_student_4 = len(student_4_point)
gta_student_4 = round(total_points_student_4 / number_of_ratings_student_4, 2)

student_5_point = grades[4]
total_points_student_5 = sum(student_5_point)
number_of_ratings_student_5 = len(student_5_point)
gta_student_5 = round(total_points_student_5 / number_of_ratings_student_5, 2)

#print('Средняя оценка студентов:''\n', gta_student_1, '\n', gta_student_2, '\n', gta_student_3, '\n', gta_student_4, '\n', gta_student_5)
list_students = list(students)
list.sort(list_students)
student_1_name = list_students[0]
student_2_name = list_students[1]
student_3_name = list_students[2]
student_4_name = list_students[3]
student_5_name = list_students[4]
#print('Имена студентов:', '\n', student_1_name, '\n', student_2_name, '\n', student_3_name, '\n', student_4_name, '\n', student_5_name)

dict_students_gta = {student_1_name: gta_student_1,
                     student_2_name: gta_student_2,
                     student_3_name: gta_student_3,
                     student_4_name: gta_student_4,
                     student_5_name: gta_student_5}

print(dict_students_gta)

#print('Оценки студендов:', '\n',
#     student_1_name, ':', 'средний балл:', gta_student_1, ';' ' всего оценок:', len(student_1_point), ';' ' оценки:', grades[0], '.', '\n',
#     student_2_name, ':', 'средний балл:', gta_student_2, ';' ' всего оценок:', len(student_2_point), ';' ' оценки:', grades[1], '.', '\n',
#     student_3_name, ':', 'средний балл:', gta_student_3, ';' ' всего оценок:', len(student_3_point), ';' ' оценки:', grades[2], '.', '\n',
#     student_4_name, ':', 'средний балл:', gta_student_4, ';' ' всего оценок:', len(student_4_point), ';' ' оценки:', grades[3], '.', '\n',
#     student_5_name, ':', 'средний балл:', gta_student_5, ';' ' всего оценок:', len(student_5_point), ';' ' оценки:', grades[4], '.')
