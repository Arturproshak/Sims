import random

class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.gladness = 50
        self.satiety = 50
        self.money = 100
        self.alive = True
    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        if self.car.drive() == True:
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 5:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 5:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('Bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print('Happy')
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
    def days_indexes(self, day):
        day = f"Today the {day} of {self.name}'s life"
        print(f"{day:=^50}", '\n')
        human_indexess = self.name + "'s indexess"
        print(f"{human_indexess:=^50}", '\n')
        print(f'Money - {self.money}')
        print(f'Satiety - {self.satiety}')
        print(f'Gladness - {self.gladness}')
        home_indexess = "Home indexxes"
        print(f"{home_indexess:^50}", '\n')
        print(f'Food - {self.home.food}')
        print(f'Mess - {self.home.mess}')
        car_indexess = "Car indexess"
        print(f"{car_indexess:^50}", '\n')
        print(f'Brand - {brands_of_car}')
        print(f'State - {self.car.drive}')
        # Home Work - Написать код, который выводит всю инфу о машине, т.е. бренд, кол бензина и тех ссотояние
    def is_alive(self):
        if self.gladness <= 0:
            print('Dipression')
            self.alive = True
        elif self.satiety <= 0 and self.home.food <= 0:
            print('Hungry')
            self.alive = False
        elif self.money <= 5:
            print('No money')
            self.alive = False
        elif self.satiety <= 0 and self.home.food >= 5:
            while self.home.food >= 5:
                self.home.food -= 5
            while self.home.food >= 5:
                self.satiety += 5
            self.alive = True
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print('Settled in the house')
            self.get_home()
        if self.car is None:
            print('Buy the car')
            self.get_car()
            self.brand()
        if self.work is None:
            print('Find the work')
            self.get_job()
            self.job()
        # Аналогично 98 строке, проверьте наличие автомобиля и работы
        # И вывести инфу о марке авто
        # А также вывести инфу о работе с уровнем зарплаты

        # Самое интересное - устроить веселую жизнь герою (по аналогии со студентом)
        dice = random.randint(1, 4)
        if self.satiety < 10:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I'll go clean my home")
                self.clean_home()
            else:
                print("Let's chill")
                self.chill()
        elif self.money is True or False:
            print(self.money)
        elif self.car.drive is True or False:
            print(self.car.drive)
        # Проверить количество денег
        # Проверить тех состояние авто


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list)) # BMW
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel > self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salery = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary":70, "gladness_less": 1 }}



brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption": 6},
    "Lada":{"fuel":50, "strength":40, "consumption": 10},
    "Volvo":{"fuel":70, "strength":150, "consumption": 8},
    "Ferrari":{"fuel":80, "strength":120, "consumption": 14}}

