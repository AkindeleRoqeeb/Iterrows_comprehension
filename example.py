student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
print(student_dict)

import pandas

student_dict_frame = pandas.DataFrame(student_dict)
print(student_dict_frame)

for (index, row) in student_dict_frame.iterrows():
    # print(index)
    # print(row)
    if row.student == "Angela":
        print(row.student)
        print(row.score)