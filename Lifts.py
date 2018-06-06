"""
Реализовать класс лифта Elevator. Класс должен обладать методом, lift, отвечающий за вызов лифта. 
При сложении/вычитании экземпляров класса должно возвращаться значение производимой математической операции. 
Если производить вычитание у лифта, который еще не совершал поднятий, должна быть выведена
 ошибка неправильной операции. Предусмотреть возможность сравнения какой из лифтов совершил большее количество поднятий.
Также необходимо предусмотреть подсчет общего количества поднятий всех лифтов.
При строчных операциях необходимо вывести детальную информацию по лифту: наименование, количество поднятий и процент 
от общего количества поднятий всех лифтов. 
"""


import sys


class Elevator:
    total_up = 0

    def __init__(self, name):
        self.name = name
        self.up = 0

    def lift(self):
        self.up += 1
        Elevator.total_up += 1
        return self.up

    def __add__(self, other):
        return self.up + other.up

    def __radd__(self, other):
        return self.up + other.up

    def __sub__(self, other): #вычитание
        if self.up > 0:
            return self.up - other.up
        else:
            return('No moves yet')

    def __rsub__(self, other): #вычитание
        if self.up:
            return self.up - other.up
        else:
            return ('No moves yet')

    def __ge__(self, other): #больше или равно
        if self.up >= other.up:
            return "{} moves more often".format(self.name)
        else:
            return "{} moves more often".format(other.name)


    def __str__(self):
        return 'The elevator {} up {} times'.format(self.name, self.up)

    def total_count_of_lifts(self):
        print("All elevators moves is {}".format(Elevator.total_up))

    def ratio(self):
        if Elevator.total_up != 0:
            return "Lift up {}% of all moves".format(self.up / Elevator.total_up * 100)
        else:
            return 'No one lifts at this moment'


def define_elevators():
    try:
        num_elevators = int(input("Enter a number of elevators: "))
    except ValueError:
        print('Incorrect value.\nEnd of programm.')
        sys.exit()

    if num_elevators <= 0:
        print("No elevators")
        sys.exit()
    dict_elevators = {}

    for ind in range(num_elevators):
        name = (input("Enter a name of %d elevator: " % (ind + 1))).title()
        dict_elevators[name] = Elevator(name)
    return dict_elevators

def define_elev():
    try:
        el_name = input('Enter a name of elevator you want: ')
        elev = elev_dict[el_name.title()]
    except KeyError:
        print("No elevator with this name. Try again.")
        return define_elev()
    else:
        return elev


def print_commands():
    print("""
            =======================MENU======================
            Choose an action you want and promt a command:
            lift - to lift an elevator,
            plus - to add number of lifts of elevators,
            minus - to substract number of lifts of elevators,
            print - to see description of an elevator,
            compare - to compare number of lifts of elevators,
            total - to see number of all lifts of elevators,
            ratio - to see ratio of lifts of elevator to all lifts,
            commands - to see in-build commands,
            exit - to end work.
            """)

if __name__ == '__main__':
    elev_dict = define_elevators()
    print_commands()
    while True:

        comm = input('Your command:  ')
        if comm == 'lift':
            if len(elev_dict) == 1:
                elevat = list(elev_dict.values())[0]
            else:
                elevat = define_elev()
            elevat.lift()
        elif comm == 'plus':
            if len(elev_dict) < 2:
                print('Not enough elevators to compare')
            else:
                elevat1 = define_elev()
                print("And now the second")
                elevat2 = define_elev()
                print(elevat1 + elevat2)
        elif comm == 'minus':
            if len(elev_dict) < 2:
                print('Not enough elevators to compare')
            else:
                elevat1 = define_elev()
                print("And now the second")
                elevat2 = define_elev()
                print(elevat1 - elevat2)
        elif comm == 'compare':
            if len(elev_dict) < 2:
                print('Not enough elevators to compare')
            else:
                elevat1 = define_elev()
                print("And now the second")
                elevat2 = define_elev()
                print(elevat1 >= elevat2)
        elif comm == 'total':
            print('Total number of lifts is', Elevator.total_up)
        elif comm == 'ratio':
            elevat = define_elev()
            print(elevat.ratio())
        elif comm == 'print':
            if len(elev_dict) == 1:
                print(list(elev_dict.values())[0])
            else:
                elevat = define_elev()
                print(elevat)
        elif comm == 'commands':
            print_commands()
        elif comm == 'exit':
            print('Good luck!')
            break
        else:
            print("Command no found")
