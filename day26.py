# List comprehension and the Nato alphabet
# [expression contained in list for item in iterable if condition == True]


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆

# #Write your 1 line code 👇 below:
# squared_numbers = [num ** 2 for num in numbers]


# #Write your code 👆 above:

# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above

# #Write your 1 line code 👇 below:

# result = [num for num in numbers if num % 2 == 0]

# #Write your code 👆 above:

# print(result)

# with open('file1.txt', 'r') as file1:
#     file1 = file1.readlines()

# with open('file2.txt', 'r') as file2:
#     file2 = file2.readlines()

# file1_int = [int(line) for line in file1]
# file2_int = [int(line) for line in file2]

# intersection = [num for num in file1_int if num in file2_int]
# print(intersection)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow"


# def dict_amount_of_words(sentence):
#     sentence = sentence.split()
#     result = {word: len(word) for word in sentence}
#     return result

# print(dict_amount_of_words(sentence))

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24}


# change_c_to_f = {key: (9/5) * value + 32 for key, value in weather_c.items()}
# print(change_c_to_f)

student_grades = {
    "Student": ["Emmanuel", "Ebube", "Aliu", "Haruna", "Oluwafemi"],
    "Grade": [80, 75, 95, 100, 80]
}

import pandas as pd

# student_grades_df = pd.DataFrame(student_grades)
# print(student_grades_df)

# for (index, row) in student_grades_df.iterrows(): 
#     if row.Student == "Emmanuel":
#         print(row.Grade)


