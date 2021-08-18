from turtle import Turtle, Screen, textinput
import pandas as pd

screen = Screen()
screen.title("U.S State Game")

screen.addshape("blank_states_img.gif")
map = Turtle()
Writer = Turtle()
Writer.hideturtle()
map.shape("blank_states_img.gif")
us_50_states_data = pd.read_csv("50_states.csv")

us_state_list = us_50_states_data["state"].tolist()

# function to find the coordinate of state


def get_state_coordinate(answer):
    country_data = us_50_states_data[us_50_states_data["state"] == answer]
    x = float(country_data.x)
    y = float(country_data.y)
    Writer.penup()
    Writer.setposition(x, y)
    Writer.write(answer, align="center", font=("Arial", 12, "normal"))


correct_guesses = []
missing_states = []
country = us_50_states_data["state"].tolist()
country_sum = len(country)
score = 0

while score < country_sum:
    users_answer = textinput(title=f"Score: {score}/{country_sum}",
                             prompt=("Enter the name of a state: ").title())
    if users_answer.lower() == "Exit".lower():
        for state in us_state_list:
            if state not in correct_guesses: 
                missing_states.append(state)
        states_to_learn = pd.DataFrame(missing_states, columns=["state"])
        states_to_learn.to_csv("states_to_learn.csv", index=False)
        break
    for state in us_state_list:
        if state.lower() == users_answer.lower():
            score += 1
            correct_guesses.append(state)
            get_state_coordinate(state)
           


screen.mainloop()
