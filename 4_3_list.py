students = ["egoing", "sori", "maru"]
grades = [1, 2, 3]

print('students[0] = ', students[0])
print('grades[0] = ', grades[0])
print('students[1] = ', students[1])
print('grades[1] = ', grades[1])
print('students[2] = ', students[2])
print('grades[2] = ', grades[2])

print("len(students) = ", len(students))


print("min(grades) = ", min(grades))
print("max(grades) = ", max(grades))

import statistics
print("statistics.mean(grades) = ", statistics.mean(grades))

import random
print("random.choice(students) = ", random.choice(students))