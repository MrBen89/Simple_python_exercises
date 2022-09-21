import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

cars = []

class CarManager(Turtle):
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.initial()

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def initial(self):
        for i in range(20):
            random_x = 300- random.randint(0,30)*20
            random_y = 220- random.randint(0,22)*20
            car = Car()
            car.create_car((random_x,random_y))
            cars.append(car)

    def create_car(self):
        if len(cars) <20:
            random_y = 220- random.randint(0,22)*20
            car = Car()
            car.create_car((300,random_y))
            cars.append(car)

    def move_cars(self):
        for car in cars:
            car.move(self.speed)
            if car.xcor() < -300:
                cars.remove(car)
                car.hideturtle()

    def collision(self, player_x, player_y):
        for car in cars:
            if car.distance(player_x, player_y) < 22:
                return True

class Car(Turtle):
    def __init__(self):
        super().__init__()


    def move(self, speed):
        self.forward(speed)

    def create_car(self, origin):
        self.setheading(180)
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.speed("fastest")
        self.goto(origin)
