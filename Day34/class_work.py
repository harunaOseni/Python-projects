# cardio_vascular disease risk program

# name = input("What is your name? ")
# age = int(input("How old are you? "))

# risk = 0

# if age < 20:
#     risk += 1
# elif age < 30:
#     risk += 2
# else:
#     risk += 3

# do_you_smoke = input("Do you smoke? ")
# if do_you_smoke == "yes":
#     risk += 4

# do_you_have_hight_blood_pressure = input("Do you have high blood pressure? ")
# if do_you_have_hight_blood_pressure == "yes":
#     risk += 2

# high_fat_diet = input("Do you have a high fat diet? ")
# if high_fat_diet == "yes":
#     risk += 1

# print(f"{name}, your risk of having a cardio_vascular disease risk is: {risk}")

# Type Hint
# Type Hint is a way to tell the computer what type of data you are expecting.
def add_sum(num1: int, num2: int) -> str:
    result = num1 + num2
    if result > 10:
        return 10
    else:
        return "Less than 10"


result = add_sum(10, 5)
print(result) 