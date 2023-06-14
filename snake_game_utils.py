from turtle import Turtle
from random import randint

def move_snake(snake_head):
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

def make_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.speed("fastest")
    my_turtle.penup()
    return my_turtle

def change_food_position(food):
    food_rand_x_position = randint(-300, 300)
    food_rand_y_position = randint(-300, 300)
    food.setposition(food_rand_x_position, food_rand_y_position)

def check_collision(t1, t2):
    if t1.distance(t2) < 20:
        return True
    return False


