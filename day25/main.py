import turtle
from tstate import State
import pandas
data = pandas.read_csv(r"C:\Users\User\Desktop\100 days\day25\50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"C:\Users\User\Desktop\100 days\day25\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_name = State()
all_states = data.state.to_list()
while len(state_name.states) < 50:
  answer_state = screen.textinput(
      title=f"{len(state_name.states)}/50 States Correct",
      prompt="What's another state's name?"
  )
  
  if answer_state:
      answer_state = answer_state.strip().title()
      if answer_state == "Exit":
            missing_states = [statee for statee in all_states if statee not in state_name.states ]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break
      if answer_state in data["state"].values:
            xcor = data[data.state == answer_state].x.iloc[0]
            ycor = data[data.state == answer_state].y.iloc[0]
            new_state = State()
            state_name.states.append(new_state)
            new_state.state_position(answer_state, xcor, ycor)
      

    

