import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data.state.tolist()
guessed_states= []

label = turtle.Turtle()
label.speed("fastest")
label.penup()
label.hideturtle()

def get_state_coord(state):
    x = int(data[data.state == state].x)
    y = int(data[data.state == state].y)
    return (x, y)

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

def write_state(state, coord):
    label.goto(coord)
    label.write(f"{state}", False, "center", ("Arial", 10, "normal"))

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the state. {len(guessed_states)}/50", prompt = "What's another state's name?")
    for state in states:
        if answer_state.lower() == state.lower():
            guessed_states.append(answer_state)
            states.remove(state)
            print(guessed_states)
            print(len(states))
            write_state(state, get_state_coord(state))


turtle.mainloop()
