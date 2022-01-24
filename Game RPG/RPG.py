import random as rdm
from time import sleep as slp
from os import system # для быстрой очистки экрана
import dunges as d # файл dunges.py
from colorama import init
from colorama import Fore, Back, Style
init()

start_new = False # Изначально обучение отключено. Оно включается только в самом начале прохождения

# Быстрая очистка экрана
def cls():
    system('CLS')

def fun_err():
    cls()
    print('\nПРОГРАММА: Папки System не существует.\nПожалуйста, создайте её, и тогда у меня как у программы\nПоявится возможность создать файлы в ней. :з')
    fun_error = input('\nENTER - хорошо, так и сделаю\n1 - Какого хрена?!\nВАШ ОТВЕТ: ==> ')
    if fun_error == "":
        exit()
    elif fun_error == "1":
        print('\nПРОГРАММА: К сожалению, мой разработчик поленился сделать мне такую функцию.\nТак что вам самим придётся это делать :(')
        input('\nНАЖМИТЕ ENTER для выхода.')
        slp(1)
        print('\nВЫ: Ну и хрен с вами!')
        slp(3)
        exit()
    else:
        print('\nПРОГРАММА: Раз вы написали всякую ахинею, я вынуждена отключиться...')
        slp(4)
        exit()

# Основной класс персонажа игрока
class Person:
    # Основной класс оружия игрока
    class Weapon:
        name = None
        level = 0
        power = 5
        critical = power + 1

    name = None
    special = None
    xp = 0
    coins = 500
    crystals = 1
    day = 0

# Проверка целостности файлов

# Проверка на наличие файла "save.txt" в папке System
try:
    save = open('System/save.txt', 'r')
except FileNotFoundError:
    print('Файла save.txt не существует. Создание нового сохранения...')
    slp(1)
    try:
        save = open('System/save.txt', 'w')
        save.write('0')
        save.close()
    except FileNotFoundError:
        fun_err()

# Проверка на наличие файла "pack.txt" в папке System
try:
    pack = open('System/pack.txt', 'r')
except FileNotFoundError:
    print('Файла pack.txt не существует. Создание нового файла...')
    slp(1)
    try:
        pack = open('System/pack.txt', 'w')
        pack.write('0000')
        pack.close()
    except FileNotFoundError:
        fun_err()

# Проверка на наличие файла "name.txt" в папке System
try:
    name = open('System/name.txt', 'r')
except FileNotFoundError:
    print('Файла name.txt не существует. Создание нового файла...')
    slp(1)
    try:
        name = open('System/name.txt', 'w')
        name.write('Герой')
        name.close()
    except FileNotFoundError:
        fun_err()

# ВНИМАНИЕ! При проверке и одновременно чтение файла, чтение сдвигается!
save = open('System/save.txt', 'r')
save.seek(0)
if save.read(1) != '0': # Суть данного if-а: Если сохранение было изменено: то ...
    # Снова становление начала чтения на начало
    save.seek(0)
    # Окончательная проверка
    if save.read(1) != '1':
        print('Файл save.txt Был необратимо изменен. Создание нового сохранения...')
        slp(1.2)
        try:
            save = open('System/save.txt', 'w')
            save.write('0')
            save.close()
        except FileNotFoundError:
            fun_err()

# Открытие файла save.txt
save = open('System/save.txt', 'r')
save.seek(0)
# Если в файле не указано наличие имени: то ...
if save.read(1) == '0':
    Person.name = input('\n\nВведи своё имя: ==> ')
    # Запись в файл name.txt нового имени
    text_name = open('System/name.txt', 'w')
    text_name.write(Person.name)
    print('\nВаше новое имя:',Person.name)
    print('Чтобы его изменить, пройдите по пути:\n "Корневая папка/System/name.txt"\nИ прописывайте новое, оригинальное на ваш взгляд имя :)\n\nВНИМАНИЕ! Настоятельно не рекомендуем удалять файл name.txt\n')
    slp(5)
    text_name.close()
    # Выбор класса перса
    print('\n КЛАССЫ:\n0 - МЕЧНИК (Основное оружие: Меч)\n1 - ЛУЧНИК (Основное оружие: Лук)\n2 - МАГ (Основное оружие: Магическая трость)\n3 - БРОНЕВИК (Основное оружие: Щит)')

    while True:
        Person.special = str(input('\nВыбери свой класс персонажа: ==> '))
        if Person.special != '0' and Person.special != '1' and Person.special != '2' and Person.special != '3':
            print('\nТакого класса не существует. Выбери класс из списка (введи ID класса)\n')
            input('ДЛЯ ПРОДОЛЖЕНИЯ НАЖМИ ENTER')
        else:
            if Person.special == '0':
                Person.special = 'Мечник'
                Person.Weapon.name = 'Меч'

            elif Person.special == '1':
                Person.special = 'Лучник'
                Person.Weapon.name = 'Лук'

            elif Person.special == '2':
                Person.special = 'Маг'
                Person.Weapon.name = 'Магическая трость'

            elif Person.special == '3':
                Person.special = 'Броневик'
                Person.Weapon.name = 'Щит'
            break

    # Создание нового/Замена старого файла и запись новых дефолд данных
    save = open('System/save.txt', 'w')
    # подробнее есть в файле "моя рпгшка.txt"

    save.writelines(['1\n', '{0}\n'.format(Person.special), '0\n', '0\n', '500\n', '1\n', '0\n', Person.Weapon.name])
    save.close()
    slp(1)
    cls()
    # После записи всех данных, начинается заставка (она появляется если не было наличия имени в save.txt)
    print('\nПриветствую тебя, {0}!\n\nДобро пожаловать в Оффлайн текстовую рпг игру, где тебе предстоит много путешествовать по загадочному и опасному миру в поисках приключений!\n'.format(Person.name))
    input('ДЛЯ ПРОДОЛЖЕНИЯ НАЖМИ ENTER')
    print('Перед тем, как ты отправишься бороздить просторы, мне нужно рассказать тебе азы.\n')
    input('ДЛЯ ПРОДОЛЖЕНИЯ НАЖМИ ENTER')
    print('В игре, помимо драк и разрушений, можно прокачивать своего персонажа (чтобы потом отпинывать врагов ещё сильней)\n')
    input('ДЛЯ ПРОДОЛЖЕНИЯ НАЖМИ ENTER')
    cls()
    print('В данный момент, у тебя должно быть в карманах 500 монет и 1 кристалл.\nЭто так называемая игровая валюта, на которую можно покупать различные предметы, а также прокачивать своего персонажа.\n')
    input('ДЛЯ ПРОДОЛЖЕНИЯ НАЖМИ ENTER')
    cls()
    print('Ты, конечно, можешь прямо сейчас пойти и крушить всех направо и налево, но это вряд ли.\nВедь у тебя нет выбора, кроме как читать мои монологи и делать то, что я тебе прикажу :)\nНапример:\n')
    input('ДЛЯ ПРОДОЛЖЕНИЯ НАЖМИ ENTER')
    print('Ладно. Давай уже купим что-нибудь...\n')
    input('НАЖМИ ENTER ЧТОБЫ НАКОНЕЦ УЙТИ')
    start_new = True # По игре будет разбросаны всякие проверки на эту переменную. Это нужно исключительно в самом начале игры

# Основное меню
def menu():
    cls()
    if start_new == True:
        print("Если возникнут вопросы, пиши в меню хелп/help")

    print(Back.GREEN, Fore.BLACK)
    print('=========OFFLINE RPG========')
    print(Back.CYAN, '    ПЕРСОНАЖ:', Person.name)
    print(Back.MAGENTA, Fore.WHITE)
    print(
        '0 - Характеристика персонажа\n1 - Инвентарь\n2 - Отправление в Дандж\n3 - Рынок\n4 - PVP Арена\n5 - Статистика\n6 - FAQ/Обновления\n7/exit - Сохранить и выйти')
    print(Back.GREEN, Fore.BLACK)
    print('============================\n')
    print(Fore.BLACK, Back.WHITE)
    choose = input('ВАШ ВЫБОР: ==> ')
    print(Back.RESET, Fore.RESET)
    if choose == '0':
        cls()
        print(Back.GREEN, Fore.BLACK)
        print('============================')
        print(Back.CYAN, '    ПЕРСОНАЖ:', Person.name)
        print(Back.MAGENTA, Fore.WHITE)
        # Решил разделить на несколько принтов, так редактировать проще
        print('Класс:', Person.special)
        print('Опыт:', Person.xp)
        print('Монет:', Person.coins)
        print('Кристаллов: ', Person.crystals)
        print('--------------------------')
        print('    Характеристика оружия:')
        print('Название:', Person.Weapon.name)
        print('Уровень:', Person.Weapon.level)
        print('Сила:', Person.Weapon.power)
        print('Критический урон:', Person.Weapon.critical)
        print(Back.GREEN, Fore.BLACK)
        print('============================\n')
        print(Fore.BLACK, Back.WHITE)
        choose = input('НАЖМИТЕ ENTER ЧТОБЫ ВЫЙТИ В МЕНЮ')
        print(Back.RESET, Fore.RESET)
        menu()

    elif choose == '1':
        cls()
        print(Back.GREEN, Fore.BLACK)
        print('============================')
        print(Back.CYAN, '    ВАШ ИНВЕНТАРЬ:')
        print(Back.MAGENTA, Fore.WHITE)
        # Недоделал инвентарь
        print('============================\n')
        print(Fore.BLACK, Back.WHITE)
        choose = input('НАЖМИТЕ ENTER ЧТОБЫ ВЫЙТИ В МЕНЮ')
        print(Back.RESET, Fore.RESET)
        menu()


# Недоделал

# Сама игра

# Загрузка сохранения
save = open('System/save.txt', 'r')
###########
# Загрузка класса персонажа
save.seek(0)
save.readline()
Person.special = save.readline()

###########
save.seek(0) # Сброс на начало файла

# Загрузка опыта, монет и кристаллов
###########
# xp
for i in range(2):
    save.readline()
Person.xp = save.readline()
save.seek(0)
# coins
for i in range(3):
    save.readline()
Person.Weapon.level = save.readline()
save.seek(0)
# crystals
for i in range(5):
    save.readline()
Person.crystals = save.readline()
save.seek(0)
###########
# Загрузка дней, проведённых за игрой
###########
for i in range(6):
    save.readline()
Person.day = save.readline()
save.seek(0)
###########
# Загрузка названия оружия
###########
for i in range(7):
    save.readline()
Person.Weapon.name = save.readline()
###########
save.close() # Закрытие сохранения

# Загрузка имени
text_name = open('System/name.txt', 'r')
Person.name = text_name.read()
text_name.close()


cls()
if start_new == True:
    print('Вот меню, которое ты будешь видеть при каждом заходе в игру. Пора уже привыкать...\n')
    input('НАЖМИ ENTER ЧТОБЫ ЕГО УВИДЕТЬ')
    cls()

menu()




