# Simple snake game using turtle module in python 3

import turtle
import time
import random


delay = 0.1
# setting up the main screen

main_screen = turtle.Screen()
main_screen.title('Snake Game')
main_screen.bgcolor('green')
main_screen.setup(width=600, height=600)
main_screen.tracer(0)  # tracer() turns off the screen updates


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)


segments = []

# Scoring
score = 0
high_score = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.shape('square')
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0  Highscore: 0 ', align="center", font=('Courier', 24, 'normal'))
# Functions


def go_up():
    '''Function to go up'''
    if head.direction != 'down':
        head.direction = 'up'


def go_down():
    '''Function to go down'''
    if head.direction != 'up':
        head.direction = 'down'


def go_left():
    '''Function to go left'''
    if head.direction != 'right':
        head.direction = 'left'


def go_right():
    '''Function to go right'''
    if head.direction != 'left':
        head.direction = 'right'


def move():
    '''Function to move snake head'''
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)


# Keybord Bindings
main_screen.listen()
main_screen.onkeypress(go_up, 'w')
main_screen.onkeypress(go_down, 's')
main_screen.onkeypress(go_left, 'a')
main_screen.onkeypress(go_right, 'd')


# main game loop
while True:
    main_screen.update()

    # check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        # Hide the segment

        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segment lists
        segments.clear()

        # Reset the Score
        score = 0

        # Update the Score
        pen.clear()
        pen.write('Score: {}  High Score: {}'.format(score, high_score),
                  align='center', font=('Courier', 24, 'normal'))

    # check for collision with a food
    if head.distance(food) < 20:
        # Move food to random cordinates
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add segments
        new_segments = turtle.Turtle()
        new_segments.speed(0)
        new_segments.shape('square')
        new_segments.color('grey')
        new_segments.penup()
        segments.append(new_segments)

        # shorten the delay
        delay -= 0.001

        # Increase score
        score += 10
        if score > high_score:
            high_score = score

        # Update the Score
        pen.clear()
        pen.write('Score: {}  High Score: {}'.format(score, high_score),
                  align='center', font=('Courier', 24, 'normal'))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for head collision with body new_segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            # Hide the segment

            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segment lists
            segments.clear()

            # Reset the Score
            score = 0

            # Update the Score
            pen.clear()
            pen.write('Score: {}  High Score: {}'.format(score, high_score),
                      align='center', font=('Courier', 24, 'normal'))

    time.sleep(delay)


main_screen.mainloop()
