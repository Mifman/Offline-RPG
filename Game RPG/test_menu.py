from os import system
from colorama import init
from colorama import Fore, Back, Style
init()

name = 'Hero'
while True:
    print(Back.GREEN, Fore.BLACK)
    print('=========OFFLINE RPG========')
    print(Back.CYAN,'    ПЕРСОНАЖ:', name)
    print(Back.MAGENTA,Fore.WHITE)
    print('0 - Характеристика персонажа\n1 - Инвентарь\n2 - Отправление в Дандж\n3 - Рынок\n4 - PVP Арена\n5 - Статистика\n6 - FAQ/Обновления\n7/exit - Сохранить и выйти')
    print(Back.GREEN,Fore.BLACK)
    print('============================\n')
    print(Fore.BLACK,Back.WHITE)
    x = input('ВАШ ВЫБОР: ==> ')
    print(Back.RESET,Fore.RESET)
    system('CLS')