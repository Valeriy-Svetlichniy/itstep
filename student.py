import random
class Student:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 100
        print(f"Hi! My name is {self.name}. I'm a student. My height is {self.height} cm.")

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def to_work(self):
        print("Time to work")
        self.progress += 0.2
        self.gladness -= 5
        self.money += 50

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.money -= 25
        self.progress -= 0.1

    def to_sleep(self):
        print("I'll sleep.")
        self.gladness += 3

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        elif self.money < 0:
            print("Debtor...")
            self.alive = False

    def end_of_day(self):
        print(f"gladness = {self.gladness}")
        print(f"progress = {round(self.progress, 2)}")
        print(f"money = {self.money}$")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")

        choice = random.randint(1,4)

        if choice == 1:
            self.to_study()
        elif choice == 2:
            self.to_chill()
        elif choice == 3:
            self.to_work()
        else:
            self.to_sleep()

        self.end_of_day()
        self.is_alive()


student = Student("Vadym",183)

for day in range(365):
    if student.alive == False:
        break
    student.live(day)