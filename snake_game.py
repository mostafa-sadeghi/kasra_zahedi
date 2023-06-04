from turtle import Screen, Turtle, Terminator
from time import sleep
from random import randint


def move_snake():
    if snake_head.direction == "up":
        snake_head_y_position = snake_head.ycor()
        snake_head_y_position += 20
        snake_head.sety(snake_head_y_position)
    if snake_head.direction == "down":
        snake_head_y_position = snake_head.ycor()
        snake_head_y_position -= 20
        snake_head.sety(snake_head_y_position)
    if snake_head.direction == "right":
        snake_head_x_position = snake_head.xcor()
        snake_head_x_position += 20
        snake_head.setx(snake_head_x_position)
    if snake_head.direction == "left":
        snake_head_x_position = snake_head.xcor()
        snake_head_x_position -= 20
        snake_head.setx(snake_head_x_position)


def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


main_surface = Screen()
main_surface.bgcolor("blue")
main_surface.title("snake Game")
main_surface.setup(width=600, height=600)

snake_head = Turtle()
snake_head.shape("square")
snake_head.color("black")
snake_head.speed("fastest")
snake_head.penup()
snake_head.direction = ""


food = Turtle()
food.shape('circle')
food.color('red')
food.shapesize(0.4, 0.4)
food.speed('fastest')
food.penup()
food_rand_x_position = randint(-300, 300)
food_rand_y_position = randint(-300, 300)
food.setposition(food_rand_x_position, food_rand_y_position)


main_surface.listen()
main_surface.onkeypress(go_up, 'Up')
main_surface.onkeypress(go_down, 'Down')
main_surface.onkeypress(go_right, 'Right')
main_surface.onkeypress(go_left, 'Left')

canvas = main_surface.getcanvas()  # or, equivalently: turtle.getcanvas()
root = canvas.winfo_toplevel()


def on_close():
    global running
    running = False


root.protocol("WM_DELETE_WINDOW", on_close)


running = True
while running:
    try:
        main_surface.update()
    except Terminator:
        break
    move_snake()
    sleep(0.1)

# https://stackoverflow.com/questions/50654793/how-to-detect-x-close-button-in-python-turtle-graphics
# number1 = int(input('enter a number :'))
# number2 = int(input('enter a number :'))
# try:
#     print(number1/number2)
# except:
#     pass
