# How to open, read and write file using the with keyword.
with open("my_file.txt", mode="w") as day24_file:
    day24_file.write("I am going to start a company with my cofounder that\
 will be of enormous value to each of the 4 billion internet users.")

with open("my_file.txt", mode="r") as day24_file:
    print(day24_file.read())
