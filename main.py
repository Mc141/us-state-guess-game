import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S. States Game")

img = "blank_states_img.gif"

turtle.addshape(img)
turtle.shape(img)

writer = turtle.Turtle()
writer.hideturtle()


data = pandas.read_csv("50_states.csv")

state_names = data.state.to_list()
state_x_coordinates = data.x.to_list()
state_y_coordinates = data.y.to_list()


correct_guesses = []
score = 0

game_is_running = True


while game_is_running:
    answer = screen.textinput(title=f"Guess the State {score}/50", prompt="What's another state's name?")


    
    if answer == "Exit" or answer is None:
        break

    answer = answer.title()

    if answer in state_names:
        index = state_names.index(answer)
        x_cor = state_x_coordinates[index]
        y_cor = state_y_coordinates[index]

        writer.penup()
        writer.goto(x_cor, y_cor)
        writer.pendown()
        writer.write(answer)

        correct_guesses.append(answer)
        score+=1




unknown__states = list(set(state_names).difference(set(correct_guesses)))




#states_to_learn.csv

data = {
    "Learn these states": unknown__states
}



frame = pandas.DataFrame(data)

frame.to_csv("states_to_learn.csv", index=False)