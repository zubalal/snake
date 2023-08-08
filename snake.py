from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.x_start = 0
        self.y_start = 0
        self.segments = [] #каждый элемент этого списка отдельная черепаха.
        self.create_segments()   #Вызываем метод для создания первых трех сегментов змейки
        self.snake_head = self.segments[0]

    def create_segments(self):
        for i in range(3):
            snake_segment = Turtle("square")
            snake_segment.penup()
            snake_segment.color("white")
            snake_segment.goto(self.x_start, self.y_start)
            self.x_start -= 20
            self.segments.append(snake_segment)

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())







    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_coord = self.segments[seg_num - 1].xcor()
            y_coord = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_coord, y_coord)
        self.snake_head.forward(MOVE_DISTANCE)

    # Меняем направление головы змейки
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.seth(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.seth(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.seth(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.seth(RIGHT)










