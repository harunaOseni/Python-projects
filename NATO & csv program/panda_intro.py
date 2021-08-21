# Analyzing data (in csv file and format) with pandas.

# with open("weather_data.csv", "r") as weather_data:
#     data = weather_data.readlines()

import csv
import pandas as pd

# with open("weather_data.csv", "r") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = [int(row[1]) for row in data if row[1] != "temp"]
#     print(temperature)
#     for row in data:
#         print(row)
# data = pd.read_csv("weather_data.csv")
# print(data)
# print the temperature column
# data_to_dict = data.to_dict()
# print(data_to_dict)
# temp_list = data["temp"].tolist()
# print(temp_list)

# total_sum_of_temps = 0
# for temp in temp_list:
#     total_sum_of_temps += temp

# average_temp = round(total_sum_of_temps / len(temp_list))
# print(average_temp)

# max_data_value = max(data["temp"])
# print(data[data["temp"] == max_data_value])

# monday = data[data["day"] == "Monday"]

# celsius = monday.temp
# conv_fahrenheit = (celsius * 1.8) + 32
# print(conv_fahrenheit)

# data_dict = {
#     "students": ["Ayo", "Berta", "Cecilia", "Dario", "Elvira"],
#     "grades": [80, 90, 100, 100, 80]
# }

# convert to pandas dataframe
# df = pd.DataFrame(data_dict)

# create csv file and write to it
# df.to_csv("student_grade.csv")

squirrel_data = pd.read_csv("squirrel-data.csv")
gray_squirrel_data = squirrel_data[squirrel_data["PrimaryFurColor"] == "Gray"]
cinammon_data = squirrel_data[squirrel_data["PrimaryFurColor"] == "Cinnamon"]
black_squirrel_data = squirrel_data[squirrel_data["PrimaryFurColor"] == "Black"]
# find the sum of the gray squirrels
total_gray_squirrels = len(gray_squirrel_data)
# find the sum of the cinammon squirrels
total_cinammon_squirrels = len(cinammon_data)
# find the sum of the black squirrels
total_black_squirrels = len(black_squirrel_data)

squirrel_data_dict = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [total_gray_squirrels, total_cinammon_squirrels, total_black_squirrels]
}

sq_df = pd.DataFrame(squirrel_data_dict)
sq_df.to_csv("gcb_squirrel_data.csv")
