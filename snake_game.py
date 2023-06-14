from turtle import Screen, Terminator
from time import sleep
from snake_game_utils import *

snake_bodies = []
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
main_surface.tracer(0)
snake_head = make_turtle("square", "black")
snake_head.direction = ""


food = make_turtle("circle", "red")
change_food_position(food)


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

    if check_collision(snake_head, food):
        change_food_position(food)
        new_tail = make_turtle("square","grey")
        snake_bodies.append(new_tail)

    for i in range(len(snake_bodies) - 1, 0, -1):
        xprev = snake_bodies[i-1].xcor()
        yprev = snake_bodies[i-1].ycor()
        snake_bodies[i].goto(xprev, yprev)

    if len(snake_bodies) > 0:
        xhead = snake_head.xcor()
        yhead = snake_head.ycor()
        snake_bodies[0].goto(xhead, yhead)

    
    # TODO در صورت خروج مار از چهار لبه صفحه
    # if conditions:
        # reset(snake_head, snake_bodies)
        
    # بازی ریست شود
    # برای ریست شدن بازی میبایست 
    # یک تابع جدید در ماژول کمکی ایجاد کنی
    # درون این تابع می بایست سر مار را به نقطه اول 
    # یعنی صفر و صفر قرار دهی
    # همینطور تکه های بدن مار که در لیست قرار داده شدند
    # را با کمک تابع زیر مخفی کنی
    # hideturtle() or ht()
    # در نهایت می بایست لیست را پاک کنی



    move_snake(snake_head)
    sleep(0.1)

# https://stackoverflow.com/questions/50654793/how-to-detect-x-close-button-in-python-turtle-graphics
# number1 = int(input('enter a number :'))
# number2 = int(input('enter a number :'))
# try:
#     print(number1/number2)
# except:
#     pass
