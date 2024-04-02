# Question 0
import random
my_dict = {
    'info': {'name':'Mirsaid','student_id': 12225253,'age':17,'address':'Michuhol-gu','nationality':'Uzbek','department':'Integrated system engineering' },
    'subjects': ['Software Programming','Basic Korean','Advanced English','Phronesis seminar','Reading Seminar','Discrete Math']
}
my_p = {}
# print(my_dict)

# Question 1

#1

subjects = my_dict['subjects']
# print(subjects)

for subject in subjects:
        my_p[subject] = random.choice(range(0,100))
# print(my_points)
sorted_points = []
# Question 2 
for key,value in my_p.items():
    sorted_points.append((key,value))

print(sorted(sorted_points,key=lambda a: a[1]))




