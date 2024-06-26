import random as rdm
import random as rdm
from time import sleep as slp
from os import system  # для быстрой очистки экрана

# Проверка наличия dunges.py
try:
    import dunges as d  # файл dunges.py
except ModuleNotFoundError:
    print('ОШИБКА! В КОРНЕВОМ КАТАЛОГЕ НЕ НАЙДЕН ФАЙЛ "dunges.py"')
    slp(99999)

from colorama import init
from colorama import Fore, Back, Style

init()

# Технические переменные
##################
start_new = False  # Изначально обучение отключено. Оно включается только в самом начале прохождения
x = 0  # Для рынка

# БОТ
v1 = 0
v2 = 0
v3 = 0
v4 = 0

# Выбор попавшегося врага
this_enemy = False  # True, если данный враг может попасться в данном дандже
enemy_forest = ["Гоблин", "Орк", "Кикимора", "Энт", "Кентавр", "Тролль", "Тэнгу", "Оборотень", "Персонаж"]
enemy_dungeon = ["Гоблин", "Орк", "Кикимора", "Тролль", "Оборотень", "Персонаж", "Паук", "Элементаль", "Горгона",
                 "Скелет", "Зомби"]
enemy_dense_forest = ["Гоблин", "Орк", "Кикимора", "Энт", "Кентавр", "Тролль", "Тэнгу", "Оборотень", "Персонаж", "Паук",
                      "Элементаль", "Горгона", "Циклоп"]
enemy_castle = ["Гоблин", "Орк", "Кикимора", "Тролль", "Персонаж", "Паук", "Элементаль", "Горгона", "Скелет", "Зомби",
                "Лич", "Демон"]
enemy_super_dungeon = ["Гоблин", "Орк", "Кикимора", "Тролль", "Персонаж", "Паук", "Элементаль", "Горгона", "Скелет",
                       "Зомби", "Лич", "Демон"]
enemy_emerald_forest = ["Орк", "Кикимора", "Тролль", "Оборотень", "Персонаж", "Паук", "Элементаль", "Горгона", "Демон",
                        "Циклоп", "Кентавр", "Энт", "Тэнгу"]


# enemy_list = ["Гоблин", "Орк", "Паук", "Кикимора","Энт", "Кентавр", "Элементаль", "Тролль","Циклоп", "Демон", "Тэнгу", "Горгона", "Скелет","Оборотень", "Лич", "Зомби", "Персонаж"]

##################
# Техническая(-ие) функция(-и)
def potion_more(x):
    print(Back.RED, Fore.WHITE, '\nВы не можете хранить больше 9-ти зелий/сундуков/кристаллов одного вида!')
    Person.coins += x
    x = 0
    input('\nНАЖМИТЕ ENTER, ЧТОБЫ ПРОДОЛЖИТЬ')
    market()


##################

# Быстрая очистка экрана
def cls():
    print(Fore.WHITE, Back.BLACK)
    system('CLS')


def fun_err():
    cls()
    print(
        '\nПРОГРАММА: Папки "System" в корневом каталоге не существует.\nПожалуйста, создайте её, и тогда у меня как у программы\nПоявится возможность создать файлы в ней. :з')
    fun_error = input('\nENTER - хорошо, так и сделаю\n1 - Какого хрена?!\nВАШ ОТВЕТ: ==> ')
    if fun_error == "":
        exit()
    elif fun_error == "1":
        print(
            '\nПРОГРАММА: К сожалению, мой разработчик поленился сделать мне такую функцию.\nТак что вам самим придётся это делать :(')
        input('\nНАЖМИТЕ ENTER для выхода.')
        slp(1)
        print('\nВЫ: Ну и хрен с вами!')
        slp(3)
        exit()
    else:
        print('\nПРОГРАММА: Раз вы написали всякую ахинею, я отключаюсь...')
        slp(4)
        exit()


# Основной класс персонажа игрока
class Person:
    # Основной класс оружия игрока
    class Weapon:
        name = None
        level_w = 0
        multiplier = level_w * 9  # Множитель уровня (именно столько нужно опыта для достижения нового уровня)
        # ВНИМАНИЕ! Опыт у оружия и персонажа общий!! При достижении multiplier опыт не сбрасывается!!!
        power = 5 + (level_w)
        power_default = 5 + (level_w)
        critical = power * 1.5
        critical_default = power * 1.5

    name = None
    special = None
    xp = 0  # Опыт
    level = 1  # Уровень
    multiplier = level * 12  # Множитель уровня (именно столько нужно опыта для достижения нового уровня)
    day = 0  # Дни, проведённые за игрой (игровые, вычисляются битвами)
    can_dunge = 0  # Переменная, позволяющая ходить на другие данджи (нужна в меню выбора данджа. Она играет чисто декоративную роль)
    current_dunge = None  # Переменная, определяющая в каком дандже сейчас находится игрок
    coins = 50
    crystals = 1

    # Для битв
    hp = 18 + (level + 1)  # Кол-во жизней
    hp_default = 18 + (level + 1)  # По умолчанию
    stamina = hp / 3  # Выносливость персонажа
    stamina_default = hp / 3  # По умолчанию
    mana = 10 + level  # Если класс персонажа Маг, данная переменная играет роль, в остальном нет
    mana_default = 10 + level  # По умолчанию

    # Арена
    rand_bet = rdm.randint(10, 35)  # Для арены (ставка для входа)

    # Достижения
    ach_0 = "Не выполнено"  # Пройдите всё обучение (пометка: необходимо выполнить ни разу не закрыв игру)
    ach_1 = "Не выполнено"  # Сходите первый раз в дандж
    ach_2 = "Не выполнено"  # Уничтожьте первого врага
    ach_3 = "Не выполнено"  # Получите 2 уровень персонажа
    ach_4 = "Не выполнено"  # Получите 10 уровень персонажа
    ach_5 = "Не выполнено"  # Сходите в дандж "Подземелье"
    ach_6 = "Не выполнено"  # Получите 30 уровень
    ach_7 = "Не выполнено"  # Получите 40 уровень
    ach_8 = "Не выполнено"  # Получите 50 уровень
    ach_9 = "Не выполнено"  # Получите 60 уровень
    # Идёт по порядку достижений
    a_0 = 0
    a_1 = False
    a_2 = False
    a_3 = False
    a_4 = False
    a_5 = False
    a_6 = False
    a_7 = False
    a_8 = False
    a_9 = False

    # Зелья
    potion_pow = 0
    potion_heal = 0
    potion_mana = 0
    # Сундуки
    pack_chest = 0

    # Класс статистики (цифра 5 в меню)
    class Stats():
        coins_up = 0  # Всего заработано монет
        crystals_up = 0  # Всего заработано кристаллов
        chests_open = 0  # Всего открытых сундуков


l_market = ["Зелье Силы", "Зелье Здоровья", "Зелье маны", "Сундук", "Кристалл"]


# Создание класса market (рынок)
# Всего 5 ларьков. Они генерятся случайным образом
class Market:
    # Ларьки
    stall_0 = rdm.choice(l_market)
    stall_1 = rdm.choice(l_market)
    stall_2 = rdm.choice(l_market)
    stall_3 = rdm.choice(l_market)
    stall_4 = rdm.choice(l_market)
    # Переменная, позволяющая изменить генерацию ларьков (True - может/False - не может). По умолчанию False
    edit = False
    # Цена товара на рынке
    price_0 = rdm.randint(3, 30)
    price_1 = rdm.randint(3, 30)
    price_2 = rdm.randint(3, 45)
    price_3 = rdm.randint(5, 30)
    price_4 = rdm.randint(3, 20)
    price_5 = rdm.randint(7,14)


# Пересохраение основного "save.txt"
def m_write_save():
    save = open('System/save.txt', 'w')
    save.write(
        '1\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n{10}'.format(Person.special, Person.xp, Person.level,
                                                                           Person.Weapon.level_w, Person.coins,
                                                                           Person.crystals, Person.day,
                                                                           Person.Weapon.name, Person.Stats.coins_up,
                                                                           Person.Stats.crystals_up,
                                                                           Person.Stats.chests_open))
    save.close()


# Пересохраение инвентаря игрока (pack.txt)
def m_write_pack():
    save_inventory = open('System/pack.txt', 'w')
    save_inventory.seek(0)
    save_inventory.write(
        '{0}{1}{2}{3}'.format(Person.potion_pow, Person.potion_heal, Person.potion_mana, Person.pack_chest))
    save_inventory.close()


# Пересохраение достижений (achievements.txt)
def m_write_achievements():
    achievements = open('System/achievements.txt', 'w')
    achievements.seek(0)
    achievements.write(
        '{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}'.format(Person.ach_0, Person.ach_1, Person.ach_2,
                                                                  Person.ach_3, Person.ach_4, Person.ach_5,
                                                                  Person.ach_6, Person.ach_7, Person.ach_8,
                                                                  Person.ach_9))
    achievements.close()


# Проверка целостности файлов

# Для упрощения
def reset_game():
    try:
        save = open('System/save.txt', 'w')
        save.write('0')
        save.close()

        pack = open('System/pack.txt', 'w')
        pack.write('0000')
        pack.close()

        achievements = open('System/achievements.txt', 'w')
        achievements.write('Не выполнено\nНе выполнено\nНе выполнено\nНе выполнено\nНе выполнено\nНе выполнено\n'
                           'Не выполнено\nНе выполнено\nНе выполнено\nНе выполнено')  # Достижения
        achievements.close()

        name = open('System/name.txt', 'w')
        name.write('Герой')
        name.close()
    except FileNotFoundError:
        fun_err()


# Проверка на наличие файла "save.txt" в папке System
try:
    save = open('System/save.txt', 'r')
except FileNotFoundError:
    print('Файла save.txt не существует. Сброс игры...')
    slp(1)
    reset_game()

# Проверка на наличие файла "pack.txt" в папке System
try:
    pack = open('System/pack.txt', 'r')
except FileNotFoundError:
    print('Файла pack.txt не существует. Сброс игры...')
    slp(1)
    reset_game()

# Проверка на наличие файла "name.txt" в папке System
try:
    name = open('System/name.txt', 'r')
except FileNotFoundError:
    print('Файла name.txt не существует. Сброс игры...')
    slp(1)
    reset_game()

# Проверка на наличие файла "achievements.txt" в папке System
try:
    achievements = open('System/achievements.txt', 'r')
except FileNotFoundError:
    print('Файла achievements.txt не существует. Сброс игры...')
    slp(1)
    reset_game()

# ВНИМАНИЕ! При проверке и одновременно чтение файла, чтение сдвигается!
save = open('System/save.txt', 'r')
save.seek(0)
if save.read(1) != '0':  # Суть данного if-а: Если сохранение было изменено: то ...
    # Снова становление начала чтения на начало
    save.seek(0)
    # Окончательная проверка
    if save.read(1) != '1':
        print('Файл save.txt Был необратимо изменен. Сброс игры...')
        slp(1.2)
        reset_game()

# Открытие файла save.txt
save = open('System/save.txt', 'r')
save.seek(0)
# Если в файле не указано наличие имени: то ...
if save.read(1) == '0':
    Person.name = input('\n\nВведи своё имя: ==> ')
    # Запись в файл name.txt нового имени
    text_name = open('System/name.txt', 'w')
    text_name.write(Person.name)
    print('\nВаше новое имя:', Person.name)
    print(
        '\nЧтобы его изменить, пройдите по пути:\n "Корневая папка/System/name.txt"\nИ прописывайте новое, оригинальное на ваш взгляд имя :)\n\n',
        Back.RED, Fore.WHITE, 'ВНИМАНИЕ! Настоятельно не рекомендуем удалять файлы из папки "System"!\n')
    print(Fore.WHITE, Back.BLACK)
    slp(5)
    text_name.close()
    # Выбор класса перса
    print(
        '\n\n КЛАССЫ:\n0 - МЕЧНИК (Основное оружие: Меч)\n1 - ЛУЧНИК (Основное оружие: Лук)\n2 - МАГ (Основное оружие: Магическая трость)\n3 - БРОНЕВИК (Основное оружие: Щит)')

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

    save.writelines(
        ['1\n', '{0}\n'.format(Person.special), '0\n', '{0}\n'.format(Person.level), '0\n', '50\n', '1\n', '0\n',
         Person.Weapon.name, '\n0\n', '0\n', '0'])
    save.close()
    slp(1)
    cls()
    # После записи всех данных, начинается заставка (она появляется если не было наличия имени в save.txt)
    print(
        '\nПриветствую тебя, {0}!\n\nДобро пожаловать в Оффлайн текстовую рпг игру, где тебе предстоит много путешествовать по загадочному и опасному миру в поисках приключений!\n'.format(
            Person.name))
    input('ДЛЯ ПРОДОЛЖЕНИЯ НАЖМИ ENTER')
    print('Перед тем, как ты отправишься бороздить просторы, мне нужно рассказать тебе азы.\n')
    input('ДЛЯ ПРОДОЛЖЕНИЯ НАЖМИ ENTER')
    print(
        'В игре, помимо драк и разрушений, можно прокачивать своего персонажа (чтобы потом отпинывать врагов ещё сильней)\n')
    input('ДЛЯ ПРОДОЛЖЕНИЯ НАЖМИ ENTER')
    cls()
    print(
        'В данный момент, у тебя должно быть в карманах 50 монет и 1 кристалл.\nЭто так называемая игровая валюта, на которую можно покупать различные предметы, а также прокачивать своего персонажа.\n')
    input('ДЛЯ ПРОДОЛЖЕНИЯ НАЖМИ ENTER')
    cls()
    print(
        'Ты, конечно, можешь прямо сейчас пойти и крушить всех направо и налево, но это вряд ли.\nВедь у тебя нет выбора, кроме как читать мои монологи и делать то, что я тебе прикажу :)\nНапример:\n')
    input('ДЛЯ ПРОДОЛЖЕНИЯ НАЖМИ ENTER')
    print('Ладно. Давай уже купим что-нибудь...\n')
    input('НАЖМИ ENTER ЧТОБЫ НАКОНЕЦ УЙТИ')
    start_new = True  # По игре будет разбросаны всякие проверки на эту переменную. Это нужно исключительно в самом начале игры


# Основное меню
def menu():
    print(Back.BLACK, Fore.WHITE)
    cls()
    if start_new == True:
        if Person.a_0 == 0:
            print("Если возникнут вопросы, пиши в меню: 6\n")
    print(Back.GREEN, Fore.BLACK)
    print('=========OFFLINE RPG========')
    print(Back.CYAN, '    ПЕРСОНАЖ', Person.name)
    print(Back.MAGENTA, Fore.WHITE)
    print(
        '0 - Характеристика персонажа\n1 - Инвентарь\n2 - Отправление в Дандж\n3 - Рынок\n4 - PVP Арена\n5 - Статистика\n'
        '6 - FAQ/Обновления\n7 - Достижения\n8/exit - Сохранить и выйти')
    print(Back.GREEN, Fore.BLACK)
    print('============================\n')
    print(Fore.BLACK, Back.WHITE)
    choose_menu = input('ВАШ ВЫБОР: ==> ')
    print(Back.RESET, Fore.RESET)
    if choose_menu == '0':
        cls()
        print(Back.GREEN, Fore.BLACK)
        print('============================')
        print(Back.CYAN, '    ПЕРСОНАЖ:', Person.name)
        print(Back.MAGENTA, Fore.WHITE)
        # Решил разделить на несколько принтов, так редактировать проще
        print('Класс:', Person.special)
        print('Опыт: ', Person.xp,'/',Person.multiplier,sep='')
        print('Уровень:', Person.level)
        print('Монет:', Person.coins)
        print('Кристаллов: ', Person.crystals)
        print('--------------------------')
        print('    Характеристика оружия:\n')
        print('Название:', Person.Weapon.name)
        print('Уровень: ', Person.Weapon.level_w,'| До повышения: ',Person.Weapon.multiplier,sep='')
        print('Сила:', Person.Weapon.power)
        print('Критический урон:', Person.Weapon.critical)
        print(Back.GREEN, Fore.BLACK)
        print('============================\n')
        print(Fore.BLACK, Back.WHITE)
        choose = input('НАЖМИТЕ ENTER ЧТОБЫ ВЫЙТИ В МЕНЮ')
        print(Back.RESET, Fore.RESET)
        menu()

    elif choose_menu == '1':
        cls()
        print(Back.GREEN, Fore.BLACK)
        print('============================')
        print(Back.CYAN, '    ВАШ ИНВЕНТАРЬ:')
        print(Back.MAGENTA, Fore.WHITE)
        print('Монет:', Person.coins)
        print('Кристаллов: ', Person.crystals)
        print('Зелье силы:', Person.potion_pow)
        print('Зелье здоровья:', Person.potion_heal)
        if Person.special == 'Маг':
            print('Зелье маны:', Person.potion_mana)
        print('Сундуков:', Person.pack_chest)
        print(Back.GREEN, Fore.BLACK)
        print('============================\n')
        print(Fore.BLACK, Back.WHITE)
        choose = input('1. Открыть сундук\n'
                       'ENTER - ВЫЙТИ В МЕНЮ\n'
                       '\n'
                       'Ваш выбор: ==>')
        print(Back.RESET, Fore.RESET)
        if choose == "1":
            if Person.pack_chest > 0:
                Person.pack_chest -= 1
                rand_open_chest = rdm.randint(0, 5)

                # Открытие сундука
                for i in range(5):
                    cls()
                    t = "."
                    print("\nОткрывается сундук", t * i, sep='')
                    slp(0.5)
                all_pot = ''
                if rand_open_chest <= 3:
                    print(Back.WHITE, Fore.BLACK)
                    print("\nВ сундуке пусто...")
                    slp(3.5)
                elif rand_open_chest == 4:
                    rand_coins_amount = rdm.randint(1, 4)
                    print(Back.GREEN, Fore.BLACK)
                    print("\nВ сундуке найдено", rand_coins_amount, "монет!")
                    Person.coins += rand_coins_amount
                    Person.Stats.coins_up += rand_coins_amount
                    slp(3.5)
                elif rand_open_chest == 5:
                    print(Back.GREEN, Fore.BLACK)
                    rand_potion = rdm.randint(0, 2)
                    if rand_potion == 0:
                        rand_potion = "Силы"
                        if Person.potion_pow < 9:
                            Person.potion_pow += 1
                        else:
                            all_pot = '(Переполнен инвентарь)'
                    elif rand_potion == 1:
                        rand_potion = "Здоровья"
                        if Person.potion_heal < 9:
                            Person.potion_heal += 1
                        else:
                            all_pot = '(Переполнен инвентарь)'
                    elif rand_potion == 2:
                        if Person.special != "Маг":
                            rand_potion = "Здоровья"
                            if Person.potion_heal < 9:
                                Person.potion_heal += 1
                            else:
                                all_pot = '(Переполнен инвентарь)'
                        else:
                            rand_potion = "Маны"
                            if Person.potion_mana < 9:
                                Person.potion_mana += 1
                            else:
                                all_pot = '(Переполнен инвентарь)'

                    print("\nВ сундуке найдено зелье", rand_potion, all_pot)
                    slp(4)

                Person.Stats.chests_open += 1
                m_write_save()
                m_write_pack()
                menu()

            else:
                print(Back.WHITE, Fore.BLACK)
                print("\nУ вас нет сундуков!")
                slp(3)
                menu()

        else:
            menu()

    elif choose_menu == '2':
        go_dunge()

    elif choose_menu == '3':
        market()

    elif choose_menu == '4':
        cls()
        # Вход
        cycle = True
        if Person.level >= 8:
            while cycle == True:
                cls()
                print(Back.WHITE,Fore.BLACK)
                print("\nДобро пожалось на арену! Для принятия участия необходимо внести в банк", Person.rand_bet, "монет.")
                print("У вас",Person.coins,"монет.")
                print("\n1. Внести", Person.rand_bet, "монет\n"
                      "ENTER - Выход")
                bet = input("\nВаш выбор: ==>")
                if bet == "1":
                    if Person.coins < Person.rand_bet:
                        print(Back.RED, Fore.BLACK)
                        print("У вас не хватает монет!")
                        slp(3)
                    else:
                        slp(1.5)
                        Person.coins -= Person.rand_bet
                        Person.rand_bet += Person.rand_bet
                        player_arena()
                        print("Ставки сделаны! Вашим противником станет", Enemy.name)
                        slp(2.3)
                        print("\nНа кону",Person.rand_bet, "монет.")
                        сountdown = 5
                        cycle = False
                        for i in range(5):
                            cls()
                            print(Back.WHITE, Fore.BLACK)
                            print("Вход через ", end='')
                            print(сountdown)
                            slp(1)
                            сountdown -= 1
                            cls()
                        fight(v1,v2,v3,v4)

                        # После битвы
                        cls()
                        slp(1)
                        if Person.hp > 0:
                            print(Back.GREEN, Fore.BLACK)
                            print("\nВы одержали победу на арене!")
                            print("Получено",Person.rand_bet,"монет!")
                            Person.coins += Person.rand_bet
                            slp(3)
                            # Настройки по умолчанию
                            Person.hp = Person.hp_default
                            Person.Weapon.power = Person.Weapon.power_default
                            Person.Weapon.critical = Person.Weapon.critical_default
                            Person.stamina = Person.stamina_default
                            Person.mana = Person.mana_default

                            Person.day += 1

                            Enemy.hp = Enemy.hp_default
                            Enemy.stamina = Enemy.stamina_default

                            # Начисление XP
                            Person.xp += round(rdm.randint(10, 25) / 1.5, 3)
                            print("**Вы получили", round(rdm.randint(10, 25) / 1.5, 3), "опыта**")
                            slp(3.5)
                            if Person.xp >= Person.multiplier:
                                Person.level += 1

                                if Person.level == 2:
                                    print("\nРазблокировано достижение — 'Получите 2 уровень'!\n")
                                    slp(2)
                                    Person.ach_3 = "Выполнено!"
                                    m_write_achievements()
                                if Person.level == 10:
                                    print("\nРазблокировано достижение — 'Получите 10 уровень'!\n")
                                    slp(2)
                                    Person.ach_4 = "Выполнено!"
                                    m_write_achievements()

                                if Person.level == 30:
                                    print("\nРазблокировано достижение — 'Получите 30 уровень'!\n")
                                    slp(2)
                                    Person.ach_6 = "Выполнено!"
                                    m_write_achievements()

                                if Person.level == 40:
                                    print("\nРазблокировано достижение — 'Получите 40 уровень'!\n")
                                    slp(2)
                                    Person.ach_7 = "Выполнено!"
                                    m_write_achievements()

                                if Person.level == 50:
                                    print("\nРазблокировано достижение — 'Получите 50 уровень'!\n")
                                    slp(2)
                                    Person.ach_8 = "Выполнено!"
                                    m_write_achievements()

                                if Person.level == 60:
                                    print("\nРазблокировано достижение — 'Получите 60 уровень'!\n")
                                    slp(2)
                                    Person.ach_9 = "Выполнено!"
                                    m_write_achievements()

                                Person.xp -= Person.multiplier
                                print("")
                                print(Person.name, " получил новый уровень! (", Person.level, ")", sep='')
                                Person.hp = 18 + (Person.level + 1)
                                Person.hp_default = 18 + (Person.level + 1)
                                Person.stamina = Person.hp / 3
                                Person.stamina_default = Person.hp / 3
                                Person.multiplier = Person.level * 12
                                Person.mana = 10 + Person.level
                                Person.mana_default = 10 + Person.level

                            if Person.xp >= Person.Weapon.multiplier:
                                Person.Weapon.level_w += 1
                                print("")
                                print("Оружие ", Person.name, " получило новый уровень! (", Person.Weapon.level_w, ")",
                                      sep='')
                                Person.Weapon.power = 5 + Person.Weapon.level_w
                                Person.Weapon.power_default = 5 + Person.Weapon.level_w
                                Person.Weapon.critical = Person.Weapon.power * 1.5
                                Person.Weapon.multiplier = Person.Weapon.level_w * 9

                            m_write_save()
                            m_write_pack()
                            input("Нажмите ENTER для продолжения")
                            menu()

                        else:
                            # Настройки по умолчанию
                            Person.hp = Person.hp_default
                            Person.Weapon.power = Person.Weapon.power_default
                            Person.Weapon.critical = Person.Weapon.critical_default
                            Person.stamina = Person.stamina_default
                            Person.mana = Person.mana_default

                            Person.day += 1

                            Enemy.hp = Enemy.hp_default
                            Enemy.stamina = Enemy.stamina_default

                            m_write_save()
                            m_write_pack()
                            menu()



                elif bet == "":
                    cycle = False
                    menu()

                else:
                    print(Back.RED, Fore.BLACK)
                    print("\nВведите корректные данные!")
                    slp(1.5)


        else:
            print("\nВы не достигли 8 уровня! Арена для вас закрыта.")
            input("\nENTER - назад в меню")
            menu()

    elif choose_menu == '5':
        cls()
        print(Back.WHITE, Fore.BLACK)
        print(Person.name)
        print("\nОпыт:", Person.xp)
        print("Всего заработано монет:", Person.Stats.coins_up)
        print("Всего заработано кристаллов:", Person.Stats.crystals_up)
        print("Игровых дней проведено:", Person.day)
        print("Всего открытых сундуков:", Person.Stats.chests_open)
        input("\nНажмите ENTER для выхода в МЕНЮ")
        menu()

    elif choose_menu == '6':
        # FAQ/Обновления
        faq = 'None'
        while faq != "":
            cls()
            print(Back.CYAN, Fore.BLACK)
            print("Репозиторий игры (открытый код): https://github.com/Mifman/Offline-RPG")
            print("Руководства и обновления: https://github.com/Mifman/Offline-RPG/discussions")
            print("Разработчик: Mifman")
            print("Версия игры: 1.3")
            print("Контакт: https://vk.com/mifman")
            faq = input("\n1. Про данджи\n"
                        "2. Про рынок\n"
                        "3. Про PVP арены\n"
                        "ENTER - выход в МЕНЮ\n"
                        "   \nВаш выбор: ==>")

            if faq == "1":
                cls()
                print("\nДанджы в игре представляют собой основную механику игры. В данджах происходит\n"
                      "Набив опыта, получение ресурсов и конечно же битва с обитателями и другими\n"
                      "Агрессивно настроенными 'игроками'. Механика боя проста:\n\n"
                      "• Выбираешь первое действие (то есть что ты будешь делать в первую очередь)\n"
                      "• Выбираешь второе действие (по сути, заполняешь два слота для действия)\n"
                      "• Далее выбирает враг\n"
                      "• После выбора идёт бой, начиная с первого действия (или с первого слота)\n"
                      "• Игра идёт до тех пор, пока один из вас не погибнет")
                input("ENTER - выход в меню 'FAQ/Обновления'")

            elif faq == "2":
                cls()
                print("\nРынок представляет собой набор из различных не связанных между собой лавок с\n"
                      "Продавцами всякого. На рынке можно закупиться необходимыми зельями, кристаллами и т.д.")
                input("ENTER - выход в меню 'FAQ/Обновления'")

            elif faq == "3":
                cls()
                print("\nPVP арены — место не для слабых. Здесь нет места тем, кто захотел быстренько наживиться добром и опытом.\n"
                      "В PVP аренах можно сразиться с более сильными противниками, которые спуску давать не станут.\n"
                      "Идти туда — значит быть хотя бы 8 уровня прокачки. На кон ставится сумма монет и кто одержит победу,\n"
                      "Тот и забирает всю ставку.")
                input("ENTER - выход в меню 'FAQ/Обновления'")

        menu()


    elif choose_menu == '7':
        cls()
        print(Back.BLACK, "        ", Back.CYAN, Fore.BLACK, "ДОСТИЖЕНИЯ:")
        print(Back.WHITE, Fore.BLACK)
        print("• Пройдите всё обучение (пометка: необходимо выполнить ни разу не закрыв игру) —", Person.ach_0)
        print("• Сходите первый раз в дандж —", Person.ach_1)
        print("• Уничтожьте первого врага —", Person.ach_2)
        print("• Получите 2 уровень персонажа —", Person.ach_3)
        print("• Получите 10 уровень персонажа —", Person.ach_4)
        print("• Сходите в дандж 'Подземелье' —", Person.ach_5)
        print("• Получите 30 уровень —", Person.ach_6)
        print("• Получите 40 уровень —", Person.ach_7)
        print("• Получите 50 уровень —", Person.ach_8)
        print("• Получите 60 уровень —", Person.ach_9)
        input("\nНажмите ENTER для выхода в МЕНЮ")
        menu()

    elif choose_menu == '8' or choose_menu == 'exit':
        m_write_pack()
        m_write_save()
        m_write_achievements()
        exit()

    else:
        print(Back.RED, Fore.BLACK)
        print("\nВведите корректные данные!")
        slp(2.3)
        menu()


# Рынок
def market():
    cls()
    if start_new == True:
        Person.a_0 += 1
        if Person.a_0 > 1 and Person.a_0 < 3:
            print("\nРазблокировано достижение — 'ПРОЙДИТЕ ОБУЧЕНИЕ'!\n")
            slp(2)
            Person.ach_0 = "Выполнено!"
            m_write_achievements()

        print(Back.WHITE, Fore.BLACK)
        print('Это рынок. Здесь ты можешь приобрести необходимые тебе вещи.')
        slp(4)
        print(
            'В рынке в основном можно купить лишь те вещи, которые ты сможешь поместить в инвентарь, а именно:\n1. Зелья\n2. Сундуки')
        input('\nДля продолжения, нажми ENTER')
        slp(1.7)
        print('\nА вот, собственно, и рынок:')
        print(Back.BLACK, Fore.WHITE)
        slp(4)
        cls()

    print(Back.BLACK, Fore.WHITE)
    # Проверка условия, когда можно заново генерировать ассортимент
    if Market.edit == True:
        # Ларьки
        Market.stall_0 = rdm.choice(l_market)
        Market.stall_1 = rdm.choice(l_market)
        Market.stall_2 = rdm.choice(l_market)
        Market.stall_3 = rdm.choice(l_market)
        Market.stall_4 = rdm.choice(l_market)
        # Цены
        Market.price_0 = rdm.randint(3, 30)
        Market.price_1 = rdm.randint(3, 30)
        Market.price_2 = rdm.randint(3, 45)
        Market.price_3 = rdm.randint(5, 30)
        Market.price_4 = rdm.randint(3, 20)

    print(Back.GREEN, Fore.BLACK)
    print('  ============================')
    print(Back.CYAN, '              РЫНОК:')
    print(Back.GREEN, Fore.BLACK, '============================')
    print('Монет:', Person.coins)
    print('Кристаллов: ', Person.crystals)
    print('Зелье силы:', Person.potion_pow)
    print('Зелье здоровья:', Person.potion_heal)
    if Person.special == 'Маг':
        print('Зелье маны:', Person.potion_mana)
    print('Сундуков:', Person.pack_chest)
    print(Back.GREEN, Fore.BLACK, '============================')
    print(Back.MAGENTA, Fore.WHITE)
    print('1.', Market.stall_0, 'за', Market.price_0, 'монет\n')
    print('2.', Market.stall_1, 'за', Market.price_1, 'монет\n')
    print('3.', Market.stall_2, 'за', Market.price_2, 'монет\n')
    print('4.', Market.stall_3, 'за', Market.price_3, 'монет\n')
    print('5.', Market.stall_4, 'за', Market.price_4, 'монет\n')
    print("6. Обмен кристаллов")
    print(Back.GREEN, Fore.BLACK, '============================')

    # Работа рынка
    ####################
    def m_buy():  # l_market = ["Зелье Силы", "Зелье Здоровья", "Зелье маны", "Сундук", "Кристалл"]
        print(Back.BLACK, Fore.WHITE)
        cls()
        if market_choose == 'Зелье Силы':
            if Person.potion_pow >= 9:
                potion_more(x)
            else:
                print(Back.GREEN, Fore.BLACK, '\nПокупка совершена!')
                slp(0.8)
                Person.potion_pow += 1
                m_write_pack()
                m_write_save()
                menu()

        elif market_choose == 'Зелье Здоровья':
            if Person.potion_heal >= 9:
                potion_more(x)
            else:
                print(Back.GREEN, Fore.BLACK, '\nПокупка совершена!')
                slp(0.8)
                Person.potion_heal += 1
                m_write_pack()
                m_write_save()
                menu()

        elif market_choose == 'Зелье маны':
            if Person.special != "Маг":
                print(Back.BLACK, Fore.WHITE, "\n")
                print(Person.special, 'не может покупать зелье маны!')
                slp(3)
                market()

            else:
                if Person.potion_mana >= 9:
                    potion_more(x)
                else:
                    print(Back.GREEN, Fore.BLACK, '\nПокупка совершена!')
                    slp(0.8)
                    Person.potion_mana += 1
                    m_write_pack()
                    m_write_save()
                    menu()

        elif market_choose == 'Сундук':
            if Person.pack_chest >= 9:
                potion_more(x)
            else:
                print(Back.GREEN, Fore.BLACK, '\nПокупка совершена!')
                slp(0.8)
                Person.pack_chest += 1
                m_write_pack()
                m_write_save()
                menu()

        elif market_choose == 'Кристалл':
            if Person.crystals >= 9:
                potion_more(x)
            else:
                print(Back.GREEN, Fore.BLACK, '\nПокупка совершена!')
                slp(0.8)
                Person.crystals += 1
                m_write_save()
                menu()

    ####################

    # Варианты выбора
    market_choose = input('\nВаш выбор (exit/ENTER - выход из рынка): ==>')

    if market_choose == "exit" or market_choose == "":
        menu()

    elif market_choose == '1':
        market_choose = Market.stall_0
        if market_choose != 'Кристалл':
            # Открытие сохранения
            save_inventory = open('System/pack.txt', 'r')
            save_inventory.seek(0)

            if Person.coins >= Market.price_0:
                x = Market.price_0
                Person.coins -= x
                m_buy()
            else:
                print('Для покупки не хватает', (Market.price_0 - Person.coins), 'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

        else:
            if Person.coins >= Market.price_0:
                x = Market.price_0  # Временная переменная для проверок
                Person.coins -= x
                m_buy()
            else:
                print(Back.RED, Fore.BLACK, '\n\nДля покупки не хватает', (Market.price_0 - Person.coins), 'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

    elif market_choose == '2':
        market_choose = Market.stall_1
        if market_choose != 'Кристалл':
            # Открытие сохранения
            save_inventory = open('System/pack.txt', 'r')
            save_inventory.seek(0)

            if Person.coins >= Market.price_1:
                x = Market.price_1
                Person.coins -= x
                m_buy()
            else:
                print('Для покупки не хватает', (Market.price_1 - Person.coins), 'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

        else:
            if Person.coins >= Market.price_1:
                x = Market.price_1  # Временная переменная для проверок
                Person.coins -= x
                m_buy()
            else:
                print(Back.RED, Fore.BLACK, '\n\nДля покупки не хватает', (Market.price_1 - Person.coins), 'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

    elif market_choose == '3':
        market_choose = Market.stall_2
        if market_choose != 'Кристалл':
            # Открытие сохранения
            save_inventory = open('System/pack.txt', 'r')
            save_inventory.seek(0)

            if Person.coins >= Market.price_2:
                x = Market.price_2
                Person.coins -= x
                m_buy()
            else:
                print('Для покупки не хватает', (Market.price_2 - Person.coins), 'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

        else:
            if Person.coins >= Market.price_2:
                x = Market.price_2  # Временная переменная для проверок
                Person.coins -= x
                m_buy()
            else:
                print(Back.RED, Fore.BLACK, '\n\nДля покупки не хватает', (Market.price_2 - Person.coins), 'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

    elif market_choose == '4':
        market_choose = Market.stall_3
        if market_choose != 'Кристалл':
            # Открытие сохранения
            save_inventory = open('System/pack.txt', 'r')
            save_inventory.seek(0)

            if Person.coins >= Market.price_3:
                x = Market.price_3
                Person.coins -= x
                m_buy()
            else:
                print('Для покупки не хватает', (Market.price_3 - Person.coins), 'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

        else:
            if Person.coins >= Market.price_3:
                x = Market.price_3  # Временная переменная для проверок
                Person.coins -= x
                m_buy()
            else:
                print(Back.RED, Fore.BLACK, '\n\nДля покупки не хватает', (Market.price_3 - Person.coins), 'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

    elif market_choose == '5':
        market_choose = Market.stall_4
        if market_choose != 'Кристалл':
            # Открытие сохранения
            save_inventory = open('System/pack.txt', 'r')
            save_inventory.seek(0)

            if Person.coins >= Market.price_4:
                x = Market.price_4
                Person.coins -= x
                m_buy()
            else:
                print('Для покупки не хватает', (Market.price_4 - Person.coins), 'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

        else:
            if Person.coins >= Market.price_4:
                x = Market.price_4  # Временная переменная для проверок
                Person.coins -= x
                m_buy()
            else:
                print(Back.RED, Fore.BLACK, '\n\nДля покупки не хватает', (Market.price_4 - Person.coins), 'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

    elif market_choose == '6':
        cls()
        print(Back.CYAN, Fore.BLACK)
        print("1. Обменять", Market.price_5,"кристаллов на 1 уровень персонажа")
        crystall_choose = input("\n1 - обменять\n"
                                "ENTER - вернуться\n"
                                "Ваш выбор: ==>")
        if crystall_choose == "1":
            if Person.crystals >= Market.price_5:
                Person.level += 1
                Person.crystals -= Market.price_5
                print(Back.GREEN,Fore.BLACK)
                print("\nОбмен совершён!")
                slp(2)
                if Person.level == 2:
                    print("\nРазблокировано достижение — 'Получите 2 уровень'!\n")
                    slp(2)
                    Person.ach_3 = "Выполнено!"
                    m_write_achievements()
                if Person.level == 10:
                    print("\nРазблокировано достижение — 'Получите 10 уровень'!\n")
                    slp(2)
                    Person.ach_4 = "Выполнено!"
                    m_write_achievements()

                if Person.level == 30:
                    print("\nРазблокировано достижение — 'Получите 30 уровень'!\n")
                    slp(2)
                    Person.ach_6 = "Выполнено!"
                    m_write_achievements()

                if Person.level == 40:
                    print("\nРазблокировано достижение — 'Получите 40 уровень'!\n")
                    slp(2)
                    Person.ach_7 = "Выполнено!"
                    m_write_achievements()

                if Person.level == 50:
                    print("\nРазблокировано достижение — 'Получите 50 уровень'!\n")
                    slp(2)
                    Person.ach_8 = "Выполнено!"
                    m_write_achievements()

                if Person.level == 60:
                    print("\nРазблокировано достижение — 'Получите 60 уровень'!\n")
                    slp(2)
                    Person.ach_9 = "Выполнено!"
                    m_write_achievements()

                print("")
                print(Person.name, " получил новый уровень! (", Person.level, ")", sep='')
                Person.hp = 18 + (Person.level + 1)
                Person.hp_default = 18 + (Person.level + 1)
                Person.stamina = Person.hp / 3
                Person.stamina_default = Person.hp / 3
                Person.multiplier = Person.level * 12
                Person.mana = 10 + Person.level
                Person.mana_default = 10 + Person.level
                slp(3)
                m_write_save()
                m_write_pack()
                menu()

            else:
                print(Back.RED, Fore.BLACK)
                print("\nНе хватает кристаллов!")
                slp(2)
                market()

        else:
            market()

    else:
        print(Back.RED, Fore.BLACK)
        print("\nВведите корректные данные!")
        slp(2)
        market()


# Сама игра

# Технические переменные
# Веса для ИИ
v1 = 0  # Атака
v2 = 0  # Защита
v3 = 0  # Отдых


# Класс врагов (Имя, его уровень, урон (зависит от уровня), жизней (также зависит от уровня), выносливость, критический урон, кол-во выпадающего лута)
class Enemy:
    name = "None"
    level = 0
    damage = 1 + level
    hp = 4 + level
    hp_default = 4 + level
    stamina = hp / 2
    stamina_default = hp / 2
    critical = damage * 1.5
    loot = 0

    is_player = False
    potion_pow = 0
    potion_heal = 0

    rand_potion_en = None

# Для ИИ (предполагаемые статы здоровья)
t_hp = Person.hp  # Противника
t_hp_self = Enemy.hp  # Свои

##########################
# Виды врагов
enemy_list = ["Гоблин", "Орк", "Паук", "Кикимора",
              "Энт", "Кентавр", "Элементаль", "Тролль",
              "Циклоп", "Демон", "Тэнгу", "Горгона", "Скелет"
                                                     "Оборотень", "Лич", "Зомби", "Персонаж"]


# Порядок номеров миров (от лёгкого до самого сложного): 1-6

# Гоблин (1-5)
def goblin():
    Enemy.name = "Гоблин"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 2)
    Enemy.loot = rdm.randint(0, 1)
    Enemy.is_player = False

    Enemy.hp = 4 + Enemy.level
    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.damage = 1 + Enemy.level
    Enemy.critical = Enemy.damage * 1.5


# Орк (1-6)
def ork():
    Enemy.name = "Орк"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 4)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 2)
    Enemy.loot = rdm.randint(0, 1)
    Enemy.is_player = False

    Enemy.hp = 4 + Enemy.level
    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.critical = Enemy.damage * 1.5


# Паук (2-6)
def spider():
    Enemy.name = "Паук"
    Enemy.level = d.Dunge.difficulty + rdm.randint(1, 5)
    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

    Enemy.hp = 4 + Enemy.level + rdm.randint(1, 3)
    Enemy.loot = 0
    Enemy.is_player = False

    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.damage = 1 + Enemy.level
    Enemy.critical = Enemy.damage * 1.5


# Кикимора (1-6)
def kikimora():
    Enemy.name = "Кикимора"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 6)
    Enemy.loot = rdm.randint(0, 2)
    Enemy.is_player = False

    Enemy.hp = 4 + Enemy.level
    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.damage = 1 + Enemy.level
    Enemy.critical = Enemy.damage * 1.5


# Энт (1-6, кроме 2,4,5)
def ent():
    Enemy.name = "Энт"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.loot = rdm.randint(0, 1)
    Enemy.is_player = False

    Enemy.hp = 4 + Enemy.level
    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.damage = 1 + Enemy.level
    Enemy.critical = Enemy.damage * 1.5


# Кентавр (1-6, кроме 2,4,5)
def kentavr():
    Enemy.name = "Кентавр"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 1)
    Enemy.is_player = False

    Enemy.hp = 4 + Enemy.level
    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.damage = 1 + Enemy.level
    Enemy.critical = Enemy.damage * 1.5


# Элементаль (2-6)
def elemental():
    Enemy.name = "Элементаль"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 6)
    Enemy.loot = rdm.randint(0, 3)
    Enemy.is_player = False

    Enemy.hp = 4 + Enemy.level
    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.damage = 1 + Enemy.level
    Enemy.critical = Enemy.damage * 1.5


# Тролль (1-6)
def troll():
    Enemy.name = "Тролль"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 3)
    Enemy.is_player = False

    Enemy.hp = 4 + Enemy.level
    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.damage = 1 + Enemy.level
    Enemy.critical = Enemy.damage * 1.5


# Циклоп (3-6)
def cyklop():
    Enemy.name = "Циклоп"
    Enemy.level = d.Dunge.difficulty + rdm.randint(1, 5)

    Enemy.hp = 4 + Enemy.level + rdm.randint(1, 5)
    Enemy.damage = 1 + Enemy.level + rdm.randint(2, 4)
    Enemy.loot = rdm.randint(0, 2)
    Enemy.is_player = False

    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.critical = Enemy.damage * 1.5


# Демон (4-6)
def demon():
    Enemy.name = "Демон"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)

    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 11)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 4)
    Enemy.loot = rdm.randint(0, 2)
    Enemy.is_player = False

    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.critical = Enemy.damage * 1.5


# Тэнгу (человек-ворон) (1-6, кроме 2,4,5)
def tengu():
    Enemy.name = "Тэнгу"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.loot = rdm.randint(0, 3)
    Enemy.is_player = False

    Enemy.hp = 4 + Enemy.level
    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.damage = 1 + Enemy.level
    Enemy.critical = Enemy.damage * 1.5


# Горгона (2-6)
def gorgona():
    Enemy.name = "Горгона"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 4)
    Enemy.loot = rdm.randint(0, 1)
    Enemy.is_player = False

    Enemy.hp = 4 + Enemy.level
    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.critical = Enemy.damage * 1.5


# Скелет (2,4,5)
def skelet():
    Enemy.name = "Скелет"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 4)
    Enemy.loot = rdm.randint(0, 1)
    Enemy.is_player = False

    Enemy.hp = 4 + Enemy.level
    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.damage = 1 + Enemy.level
    Enemy.critical = Enemy.damage * 1.5


# Оборотень (1-6, кроме 4,5)
def oboroten():
    Enemy.name = "Оборотень"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)

    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 4)
    Enemy.loot = rdm.randint(0, 3)
    Enemy.is_player = False

    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.damage = 1 + Enemy.level
    Enemy.critical = Enemy.damage * 1.5


# Лич (4,5)
def lich():
    Enemy.name = "Лич"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 11)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 6)
    Enemy.loot = rdm.randint(0, 4)
    Enemy.is_player = False

    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.critical = Enemy.damage * 1.5


# Зомби (2,4,5)
def zombi():
    Enemy.name = "Зомби"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.is_player = False

    Enemy.hp = 4 + Enemy.level + rdm.randint(1, 5)
    Enemy.loot = rdm.randint(0, 1)

    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.damage = 1 + Enemy.level
    Enemy.critical = Enemy.damage * 1.5


# Персонаж (другой "игрок") (1-6)
name_list = ["Progger", "dAlEk456", "Footman", "KoLo40k", "Киргиз", "СвяТой_ТапоК",
             "DeMoN", "Lemon4ik", "MirrorX", "4EJIoВek", "Joker", "Шалтай", "NoName",
             "Chilly", "FRENK", "Фант0м", "GONZO", "ШапоКJLЯC", "Succubus", "СКАЛА",
             "dazz", "ВАШ Доктор", "Тень", "MC", "ZOrg", "Агент007", "Лб_Чипс", "Сухарик",
             "КR0ш", "ArTemK", "Vlad1337", "Kefir", "Лёха", "Сергей", "Рэйзор БезУмНыЙ",
             "КрипоНуб", "Who Touch My Spagetti?", "Blade Master", "Shadow Assassin",
             "Sir Swashalot", "Captain Waffle", "Space Cowboy", "The Bubblegum Baron",
             "Coconut Crusader"]


def player():
    Enemy.name = "Персонаж " + rdm.choice(name_list)
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.hp = 4 + Enemy.level + rdm.randint(3, 9)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(1, 3)

    Enemy.is_player = False
    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 2
    Enemy.stamina_default = Enemy.stamina
    Enemy.critical = Enemy.damage * 1.5

def player_arena():
    Enemy.name = "Персонаж " + rdm.choice(name_list)
    Enemy.level = (Person.level - rdm.randint(1,3)) + rdm.randint(0, 4)
    Enemy.hp = (Person.hp - rdm.randint(1,4)) + rdm.randint(1, 7)
    Enemy.damage = (Person.Weapon.power - rdm.randint(1,4)) + rdm.randint(1, 7)
    Enemy.loot = rdm.randint(1, 3)

    Enemy.hp_default = Enemy.hp
    Enemy.stamina = Enemy.hp_default / 3
    Enemy.stamina_default = Enemy.stamina
    Enemy.critical = Enemy.damage * 1.5

    Enemy.is_player = True
    Enemy.rand_potion_en = rdm.randint(0,1)
    if Enemy.rand_potion_en == 0:
        Enemy.potion_pow = rdm.randint(1,2)
        Enemy.potion_heal = rdm.randint(0,1)
    else:
        Enemy.potion_pow = rdm.randint(0, 1)
        Enemy.potion_heal = rdm.randint(1, 2)


##########################
### ПЕРЕМЕННЫЕ
# Виды лута
l_list = ["Монет", "Зелий Силы", "Зелий Здоровья",
          "Зелий Маны", "Сундук(-а)", "Кристалл(-ов)"]  # Лист со всеми видами лутов (вставляется в конце предложения)
l_name = None  # Название лута
l_amount = 0


##########################
# Получение лута
###########################

def get_loot(l_name, l_list, l_amount):
    for x in range(Enemy.loot):
        ######################
        ### Рандомайзер

        # Проценты выпадения предметов: Монеты - 40%, Зелья (один из видов) - 30% (по 10% на силу или ману и 20% на здоровье), Сундуки - 20%, Кристаллы - 10%
        rand_loot = rdm.randint(0, 9)
        if rand_loot <= 3:
            l_name = "Монет"
        elif rand_loot == 4:
            l_name = "Зелий Силы"

        elif rand_loot == 5:
            l_name = "Зелий Здоровья"

        elif rand_loot == 6:
            l_name = "Зелий Маны"

        elif rand_loot == 7:
            l_name = "Зелий Здоровья"

        elif rand_loot == 8 or rand_loot == 9:
            l_name = "Сундук(-а)"

        else:
            l_name = "Кристалл(-ов)"

        # Кол-во выпадения:
        rand_amount = rdm.randint(0, 1)
        if l_name == "Монет":  # Чтобы побольше было
            l_amount = rdm.randint(1, 5)
        else:
            l_amount = rdm.randint(1, 2)

        # Получение (ввод в инвентарь)

        if l_name == l_list[0]:  # coins
            Person.coins += l_amount
            Person.Stats.coins_up += l_amount

        elif l_name == l_list[1]:  # pow
            if Person.potion_pow < 9:
                Person.potion_pow += l_amount

            else:
                print('\nИнвентарь зелий силы полон!')

        elif l_name == l_list[2]:  # heal
            if Person.potion_heal < 9:
                Person.potion_heal += l_amount

            else:
                print('\nИнвентарь зелий здоровья полон!')

        elif l_name == l_list[3]:  # mana
            if Person.special == "Маг":
                if Person.potion_mana < 9:
                    Person.potion_mana += l_amount

                else:
                    print('\nИнвентарь зелий маны полон!')

            else:
                print(Person.special, 'не может брать зелье маны!')

        elif l_name == l_list[4]:  # chest
            Person.pack_chest += l_amount

        elif l_name == l_list[5]:  # crystal
            Person.crystals += l_amount
            Person.Stats.crystals_up += l_amount

        print(Back.WHITE, Fore.BLACK)
        print("\n ", Person.name, " Получает ", l_amount, " ", l_name, "!", sep='')
        slp(3.3)
        m_write_save()
        m_write_pack()


##########################

######################

def enemy_choose(this_enemy):
    while this_enemy != True:
        rand_enemy = rdm.choice(enemy_list)
        if rand_enemy == "Гоблин":
            goblin()
        elif rand_enemy == "Орк":
            ork()
        elif rand_enemy == "Паук":
            spider()
        elif rand_enemy == "Кикимора":
            kikimora()
        elif rand_enemy == "Энт":
            ent()
        elif rand_enemy == "Кентавр":
            kentavr()
        elif rand_enemy == "Элементаль":
            elemental()
        elif rand_enemy == "Тролль":
            troll()
        elif rand_enemy == "Циклоп":
            cyklop()
        elif rand_enemy == "Демон":
            demon()
        elif rand_enemy == "Тэнгу":
            tengu()
        elif rand_enemy == "Горгона":
            gorgona()
        elif rand_enemy == "Скелет":
            skelet()
        elif rand_enemy == "Оборотень":
            oboroten()
        elif rand_enemy == "Лич":
            lich()
        elif rand_enemy == "Зомби":
            zombi()
        elif rand_enemy == "Персонаж":
            player()

        # Определение данджа для выбора врага
        if d.Dunge.name == "Лес":
            for i in range(len(enemy_forest)):
                if enemy_forest[i] == rand_enemy:
                    this_enemy = True

        if d.Dunge.name == "Подземелье":
            for i in range(len(enemy_dungeon)):
                if enemy_dungeon[i] == rand_enemy:
                    this_enemy = True

        if d.Dunge.name == "Густой лес":
            for i in range(len(enemy_dense_forest)):
                if enemy_dense_forest[i] == rand_enemy:
                    this_enemy = True

        if d.Dunge.name == "Заброшенный замок":
            for i in range(len(enemy_castle)):
                if enemy_castle[i] == rand_enemy:
                    this_enemy = True

        if d.Dunge.name == "Супер-Подземелье":
            for i in range(len(enemy_super_dungeon)):
                if enemy_super_dungeon[i] == rand_enemy:
                    this_enemy = True

        if d.Dunge.name == "Изумрудный лес":
            for i in range(len(enemy_emerald_forest)):
                if enemy_emerald_forest[i] == rand_enemy:
                    this_enemy = True


# Битва
slot_fight = []  # Список выбора игрока
slot_fight_en = []  # Список выбора врага


def stats():  # Для простоты

    slot_fight = []  # Сброс
    slot_fight_en = []  # Сброс
    cls()

    # Вывод противника и статы главного героя
    print("\n")
    print(Back.RED, Fore.BLACK, "ПРОТИВНИК:")
    print(Back.WHITE, Fore.BLACK)
    print("Имя:", Enemy.name)
    print("Уровень:", Enemy.level)
    print("ХП:", Enemy.hp)
    print("Урон:", Enemy.damage)
    print("\n================\n")

    print(Back.GREEN, Fore.BLACK, "ИГРОК:\n")
    print(Back.WHITE, Fore.BLACK)
    print(Person.name, ":", sep='')
    print("Уровень:", Person.level)
    print("ХП:", Person.hp)
    print("Урон:", Person.Weapon.power)
    print("Крит:", Person.Weapon.critical)
    print("Выносливость:", Person.stamina)
    if Person.special == "Маг":
        print("Количество МАНЫ:", Person.mana)
    print("Зелий Силы:", Person.potion_pow)
    print("Зелий Здоровья:", Person.potion_heal)
    if Person.special == "Маг":
        print("Зелий Маны:", Person.potion_mana)


def reset_ai():
    # Веса для ИИ
    v1 = 0  # Атака
    v2 = 0  # Защита
    v3 = 0  # Отдых
    v4 = 0 # Пить зелье


def AI(v1, v2, v3):
    global t_hp
    global t_hp_self

    # Для ИИ (предполагаемые статы здоровья)
    t_hp = Person.hp  # Противника
    t_hp_self = Enemy.hp  # Свои
    # Проверки для расределения весов (хп у себя и врага и т.д.)
    if t_hp_self < (Enemy.hp_default / 2):
        v2 += 1
    if t_hp_self < (Enemy.hp_default / 2.5):
        v2 += rdm.randint(1,2)
        v1 += rdm.randint(0,1)

    if t_hp < (Person.hp_default / 2):
        v1 += 1
    if t_hp < (Person.hp_default / 2.5):
        v1 += rdm.randint(1,2)
        v2 += rdm.randint(0, 1)

    if t_hp <= (Person.hp_default) and t_hp > (Person.hp_default / 2):
        v1 += 1

    # slot_fight_en - слот для выбора врага
    slot_en = ["Атака", "Защита"]
    slot_en0 = ["Защита", "Отдых"]
    slot_en1 = ["Атака", "Отдых"]
    slot_en_all = ["Атака", "Защита", "Отдых"]
    choose_slot_en = False  # Для цикла
    while choose_slot_en == False:
        if Enemy.stamina < 2:
            v3 += 4

        if v3 >= 3:
            choose_slot_en = True  # Бот выбрал в предпочтение отдых, но не факт

        rand_slot = rdm.choice(slot_en)  # Рандом выбора
        if rand_slot == "Атака":
            if Enemy.stamina < 2:
                v3 += 2
            else:
                choose_slot_en = True
                v3 -= 1
        elif rand_slot == "Защита":
            if Enemy.stamina < 2:
                v3 += 2
            else:
                choose_slot_en = True
                v3 -= 1

    # Окончательный выбор
    if v1 > v2 and v3 < v1 and v3 < v2:
        slot_fight_en.append("Атака")
        Enemy.stamina -= 2

    elif v2 > v1 and v3 < v1 and v3 < v2:
        slot_fight_en.append("Защита")
        Enemy.stamina -= 2

    elif v2 == v1 and v3 < v1 and v3 < v2:
        rand_slot = rdm.choice(slot_en)  # Рандом выбора (50/50)
        slot_fight_en.append(rand_slot)
        Enemy.stamina -= 2
    elif v3 >= v2 and v3 >= v1:
        slot_fight_en.append("Отдых")
    elif v3 == v2 and v3 == v1:
        rand_slot = rdm.choice(slot_en_all)
        slot_fight_en.append(rand_slot)

        # Проверка для траты стамины
        if slot_fight_en == "Атака" or slot_fight_en == "Защита":
            Enemy.stamina -= 2

    elif v3 == v2 and v3 > v1:
        rand_slot = rdm.choice(slot_en0)
        slot_fight_en.append(rand_slot)

        # Проверка для траты стамины
        if slot_fight_en != "Отдых":
            Enemy.stamina -= 2

    elif v3 == v1 and v3 > v2:
        rand_slot = rdm.choice(slot_en1)
        slot_fight_en.append(rand_slot)

        # Проверка для траты стамины
        if slot_fight_en != "Отдых":
            Enemy.stamina -= 2

    elif v3 < v1 and v3 < v2:
        rand_slot = rdm.choice(slot_en)
        slot_fight_en.append(rand_slot)

        # Проверка для траты стамины
        if slot_fight_en == "Атака" or slot_fight_en == "Защита":
            Enemy.stamina -= 2

def AI_Player(v1, v2, v3, v4):
    # Проверки для расределения весов (хп у себя и врага)
    if t_hp_self < (Enemy.hp_default / 2):
        v2 += 1
        v4 += rdm.randint(1,2)
    if t_hp_self < (Enemy.hp_default / 2.5):
        v2 += rdm.randint(1, 2)
        v1 += rdm.randint(0, 1)
        v4 += rdm.randint(0,1)

    if t_hp < (Person.hp_default / 2):
        v1 += 1
        v4 += rdm.randint(0,1)
    if t_hp < (Person.hp_default / 2.5):
        v1 += rdm.randint(1, 2)
        v2 += rdm.randint(0, 1)

    if t_hp <= (Person.hp_default) and t_hp > (Person.hp_default / 2):
        v1 += rdm.randint(1,4)

    if Enemy.stamina < round(Enemy.stamina_default / 1.5, 3):
        v3 += 1
    if Enemy.stamina < round(Enemy.stamina_default / 2.2, 3):
        v3 += 2

    # slot_fight_en - слот для выбора врага
    slot_en = ["Атака", "Защита"]
    slot_en0 = ["Защита", "Отдых"]
    slot_en1 = ["Атака", "Отдых"]
    slot_en_all_0 = ["Атака", "Защита", "Отдых", "Пить зелье"]
    slot_en_all_1 = ["Атака", "Защита", "Отдых"]
    choose_slot_en = False  # Для цикла
    while choose_slot_en == False:
        if Enemy.stamina < 2:
            v3 += 4

        if v3 >= 3:
            choose_slot_en = True  # Бот выбрал в предпочтение отдых, но не факт

        rand_slot = rdm.choice(slot_en)  # Рандом выбора
        if rand_slot == "Атака":
            if Enemy.stamina < 2:
                v3 += 2
            else:
                choose_slot_en = True
                v3 -= 1
        elif rand_slot == "Защита":
            if Enemy.stamina < 2:
                v3 += 2
            else:
                choose_slot_en = True
                v3 -= 1

    # Окончательный выбор
    # Если получится Пить зелье
    if v4 > v1 and v4 > v2 and v4 > v3:
        Enemy.rand_potion_en = rdm.randint(0, 1)
        if Enemy.rand_potion_en == 0:
            if Enemy.potion_pow > 0:
                Enemy.potion_pow -= 1
                Enemy.rand_potion_en = "Зелье силы"
                slot_fight_en.append("Пить зелье")
                Enemy.stamina -= 1
            else:
                if Enemy.potion_heal > 0:
                    Enemy.potion_heal -= 1
                    Enemy.rand_potion_en = "Зелье здоровья"
                    slot_fight_en.append("Пить зелье")
                    Enemy.stamina -= 1

        elif Enemy.rand_potion_en == 1:
            if Enemy.potion_heal > 0:
                Enemy.potion_heal -= 1
                Enemy.rand_potion_en = "Зелье здоровья"
                slot_fight_en.append("Пить зелье")
                Enemy.stamina -= 1
            else:
                if Enemy.potion_pow > 0:
                    Enemy.potion_pow -= 1
                    Enemy.rand_potion_en = "Зелье силы"
                    slot_fight_en.append("Пить зелье")
                    Enemy.stamina -= 1

        if Enemy.potion_pow == 0 and Enemy.potion_heal == 0:
            if Enemy.stamina >= 2:
                rand_slot = rdm.choice(slot_en)
                slot_fight_en.append(rand_slot)

                # Проверка для траты стамины
                if slot_fight_en == "Атака" or slot_fight_en == "Защита":
                    Enemy.stamina -= 2
            else:
                slot_fight_en.append("Отдых")

    elif v1 > v2 and v3 <= v1 and v3 <= v2:
        slot_fight_en.append("Атака")
        Enemy.stamina -= 2

    elif v2 > v1 and v3 <= v1 and v3 <= v2:
        slot_fight_en.append("Защита")
        Enemy.stamina -= 2

    elif v2 == v1 and v3 < v1 and v3 < v2:
        rand_slot = rdm.choice(slot_en)  # Рандом выбора (50/50)
        slot_fight_en.append(rand_slot)
        Enemy.stamina -= 2
    elif v3 >= v2 and v3 >= v1:
        slot_fight_en.append("Отдых")
    elif v3 == v2 and v3 == v1:
        rand_slot = rdm.choice(slot_en_all_1)
        slot_fight_en.append(rand_slot)

        # Проверка для траты стамины
        if slot_fight_en == "Атака" or slot_fight_en == "Защита":
            Enemy.stamina -= 2

    elif v3 == v2 and v3 > v1:
        rand_slot = rdm.choice(slot_en0)
        slot_fight_en.append(rand_slot)

        # Проверка для траты стамины
        if slot_fight_en != "Отдых":
            Enemy.stamina -= 2

    elif v3 == v1 and v3 > v2:
        rand_slot = rdm.choice(slot_en1)
        slot_fight_en.append(rand_slot)

        # Проверка для траты стамины
        if slot_fight_en != "Отдых":
            Enemy.stamina -= 2

    elif v3 < v1 and v3 < v2:
        rand_slot = rdm.choice(slot_en)
        slot_fight_en.append(rand_slot)

        # Проверка для траты стамины
        if slot_fight_en == "Атака" or slot_fight_en == "Защита":
            Enemy.stamina -= 2

    else:
        rand_slot = rdm.choice(slot_en_all_0)
        slot_fight_en.append(rand_slot)

        # Проверка для траты стамины
        if slot_fight_en == "Атака" or slot_fight_en == "Защита":
            Enemy.stamina -= 2
        elif slot_fight_en == "Отдых":
            Enemy.stamina -= 0

        # Если получится Пить зелье
        else:
            Enemy.rand_potion_en = rdm.randint(0,1)
            if Enemy.rand_potion_en == 0:
                if Enemy.potion_pow > 0:
                    Enemy.potion_pow -= 1
                    Enemy.rand_potion_en = "Зелье силы"
                    slot_fight_en.append("Пить зелье")
                    Enemy.stamina -= 1
                else:
                    if Enemy.potion_heal > 0:
                        Enemy.potion_heal -= 1
                        Enemy.rand_potion_en = "Зелье здоровья"
                        slot_fight_en.append("Пить зелье")
                        Enemy.stamina -= 1

            elif Enemy.rand_potion_en == 1:
                if Enemy.potion_heal > 0:
                    Enemy.potion_heal -= 1
                    Enemy.rand_potion_en = "Зелье здоровья"
                    slot_fight_en.append("Пить зелье")
                    Enemy.stamina -= 1
                else:
                    if Enemy.potion_pow > 0:
                        Enemy.potion_pow -= 1
                        Enemy.rand_potion_en = "Зелье силы"
                        slot_fight_en.append("Пить зелье")
                        Enemy.stamina -= 1

            if Enemy.potion_pow == 0 and Enemy.potion_heal == 0:
                if Enemy.stamina >= 2:
                    rand_slot = rdm.choice(slot_en)
                    slot_fight_en.append(rand_slot)

                    # Проверка для траты стамины
                    if slot_fight_en == "Атака" or slot_fight_en == "Защита":
                        Enemy.stamina -= 2
                else:
                    slot_fight_en.append("Отдых")


def fight(v1, v2, v3, v4):
    global slot_fight
    global slot_fight_en

    use_mana1 = False  # Маг использовал увеличение шанса на кри ложь
    use_mana2 = False  # Маг использовал увеличение здоровья ложь

    # Для ИИ (предполагаемые статы здоровья)
    t_hp = Person.hp  # Противника
    t_hp_self = Enemy.hp  # Свои

    print(Back.RED, Fore.BLACK)
    slp(1)
    print("\nОбнаружен противник!")
    slp(3)

    while Enemy.hp > 0 or Person.hp > 0:
        m_write_save()
        m_write_pack()

        # Чтобы каждый раз опустошался список после всех битв
        if len(slot_fight) >= 2:
            slot_fight = []
        if len(slot_fight_en) >= 2:
            slot_fight_en = []

        # Ограничение на макс. кол-во выносливости (для персонажа игрока)
        if Person.stamina > Person.stamina_default:
            Person.stamina = Person.stamina_default

        Enemy.hp = round(Enemy.hp, 3)
        Person.hp = round(Person.hp, 3)
        Enemy.stamina = round(Enemy.stamina, 3)
        Person.stamina = round(Person.stamina, 3)

        # Если враг повержен
        if Enemy.hp <= 0 and Person.hp > 0:
            if Person.ach_2 != "Выполнено!":
                print("\nРазблокировано достижение — 'Уничтожьте первого врага'!\n")
                slp(2)
                Person.ach_2 = "Выполнено!"
                m_write_achievements()

            slp(2)
            print("\n")
            print(Back.GREEN, Fore.BLACK)
            print(Enemy.name, "повержен!")
            slp(2.3)
            if (round(Person.hp * 0.1, 3)) <= (Person.hp_default - Person.hp):
                print('Восстановлено 10% здоровья (+',round(Person.hp * 0.1, 3),")", sep='')
                Person.hp += round(Person.hp * 0.1, 3)
            slp(2.3)
            if Enemy.loot > 0:
                get_loot(l_name, l_list, l_amount)
            break

        # Если повержен персонаж игрока
        elif Person.hp <= 0:
            slp(2)
            print("\n")
            die = True
            print(Back.RED, Fore.BLACK)
            print(Person.name, "потерял сознание...")
            slp(4)
            cls()
            print(Back.WHITE, Fore.BLACK)
            print(
                "Внезапно, к вам прилетает Ангел с небес, берёт вас на руки и отводит через всю долину к вашим покоям...\n"
                "Вы просыпаетесь без единого пореза на руке в своей постели.\n"
                "К сожалению, все утерянные или потраченные вещи так и не появились, но вы живы, и это главное.")
            input("\nНажмите ENTER чтобы встать")
            Person.day += 1
            break

        # Выбирает игрок
        c = 1  # Переменная для цикла while
        while c != 3:
            stats()
            print("\n", c, " Слот", sep='')
            print("\nВарианты действий:\n"
                  "1. Атака\n"
                  "2. Защита\n"
                  "3. Пить зелье\n"
                  "4. Отдых")
            if Person.special == "Маг":
                print("5. Использовать магию")

            in_choice = input("\nВаш выбор: ==>")

            ############################
            # Атака
            if in_choice == "1":
                if Person.stamina < 2:
                    print(Back.RED, Fore.BLACK)
                    print("\nНе хватает выносливости!")
                    slp(2)

                else:
                    slot_fight.append("Атака")
                    slp(1)
                    print("\nВаш выбор: Атака")
                    slp(2)
                    Person.stamina -= 2
                    c += 1
            #############################

            # Защита
            #############################
            elif in_choice == "2":
                if Person.stamina < 2:
                    print(Back.RED, Fore.BLACK)
                    print("\nНе хватает выносливости!")
                    slp(2)

                else:
                    slot_fight.append("Защита")
                    slp(1)
                    print("\nВаш выбор: Защита")
                    slp(2)
                    Person.stamina -= 2
                    c += 1
            #############################

            # Пить зелье
            #############################
            elif in_choice == "3":
                if Person.stamina < 1:
                    print(Back.RED, Fore.BLACK)
                    print("\nНе хватает выносливости!")
                    slp(2)

                else:
                    slp(1)
                    print("\nВаш выбор: Пить зелье")
                    slp(1.9)

                    # Блок Зелий
                    ################################
                    pot = False
                    while pot == False:
                        cls()
                        print(Back.WHITE, Fore.BLACK)
                        print("\nВЫБОР ЗЕЛИЙ:\n"
                              "1. Зелье Силы (", Person.potion_pow, ")\n"
                                                                    "2. Зелье Здоровья (", Person.potion_heal, ")\n"
                                                                                                               "ENTER - выход из меню",
                              sep='')
                        if Person.special == "Маг":
                            print("3. Зелье Маны (", Person.potion_mana, ")", sep='')

                        pot_in = input("\nВаш выбор: ==>")

                        if pot_in != "1" and pot_in != "2" and pot_in != "3" and pot_in != "":
                            print(Back.RED, Fore.BLACK)
                            print("\nВведите корректные данные!")
                            slp(3)

                        elif pot_in == "1":
                            if Person.potion_pow > 0:
                                slot_fight.append("Пить зелье")
                                Person.potion_pow -= 1
                                Person.stamina -= 1
                                c += 1
                                pot = True
                                m_write_pack()
                            else:
                                print(Back.RED, Fore.BLACK)
                                print("\nУ вас нет Зелья Силы!")
                                slp(3)

                        elif pot_in == "2":
                            if Person.potion_heal > 0:
                                slot_fight.append("Пить зелье")
                                Person.potion_heal -= 1
                                Person.stamina -= 1
                                c += 1
                                pot = True
                                m_write_pack()
                            else:
                                print(Back.RED, Fore.BLACK)
                                print("\nУ вас нет Зелья Здоровья!")
                                slp(3)

                        elif pot_in == "3":
                            if Person.special != "Маг":
                                print(Back.RED, Fore.BLACK)
                                print("\nВведите корректные данные!")
                                slp(3)
                            else:
                                if Person.potion_mana > 0:
                                    slot_fight.append("Пить зелье")
                                    Person.potion_mana -= 1
                                    Person.stamina -= 1
                                    c += 1
                                    pot = True
                                    m_write_pack()

                                else:
                                    print(Back.RED, Fore.BLACK)
                                    print("\nУ вас нет Зелья Маны!")
                                    slp(3)

                        elif pot_in == "":
                            pot = True

                    ################################

            #############################

            # Отдых
            #############################
            elif in_choice == "4":
                slot_fight.append("Отдых")
                slp(1)
                print("\nВаш выбор: Отдых")
                slp(2)
                c += 1
            #############################

            # Использовать Магию
            #############################
            elif in_choice == "5":
                if Person.special != "Маг":
                    print("\nВведите корректные данные!")
                    slp(3)
                else:
                    print("1. Увеличить шанс критического удара (11 маны)\n"
                          "2. Восстановить немного здоровья (13 маны)")

                    use_mana = input("Ваш выбор: ==>")
                    if use_mana == "1":
                        if Person.mana >= 11:
                            print(Back.GREEN, Fore.BLACK)
                            Person.mana -= 11
                            use_mana1 = True
                            print("Шанс увеличен в 2 раза!")
                            slp(3)
                        else:
                            print(Back.RED, Fore.BLACK)
                            print("Не хватает маны!")
                            slp(3)
                    elif use_mana == "2":
                        if Person.mana >= 13:
                            print(Back.GREEN, Fore.BLACK)
                            Person.mana -= 13
                            use_mana1 = True
                            print("Увеличено здоровье на", Person.hp_default / 4)
                            Person.hp += Person.hp_default / 4
                            slp(3)
                        else:
                            print(Back.RED, Fore.BLACK)
                            print("Не хватает маны!")
                            slp(3)

            #############################

        slp(1.5)
        print(Back.WHITE, Fore.BLACK)
        print("Ваш выбор:", slot_fight)
        slp(3)

        # Выбор врага (Мега ИИ)

        # Выбор для 1 слота
        #########################
        reset_ai()
        if Enemy.is_player == True:
            AI_Player(v1,v2,v3,v4)
        else:
            AI(v1, v2, v3)
        #########################

        # Выбор для 2 слота
        #########################

        # Переделка предполагаемого события для корректировки
        if slot_fight_en[0] == "Атака":
            t_hp = Person.hp - Enemy.damage  # предполагаемое кол-во здоровья противника
        elif slot_fight_en[0] == "Защита":
            if Enemy.level < Person.level:
                t_hp_self = Enemy.hp - (
                        Person.Weapon.power * 0.25)  # Бот будет предполагать, что его защита провалилась
            elif Enemy.level >= Person.level:
                t_hp_self = Enemy.hp - (Person.Weapon.power * 0.1)
        elif slot_fight_en[0] == "Отдых":
            v3 -= 1

        if Enemy.is_player == True:
            AI_Player(v1, v2, v3, v4)
        else:
            AI(v1, v2, v3)
        #########################
        # После всех выборов
        for z in range(2):
            if use_mana1 == True:
                rand_hit = rdm.randint(0, 1)
                use_mana1 = False
            else:
                rand_hit = rdm.randint(0, 3)

            rand_hit_en = rdm.randint(0, 3)
            if rand_hit == 0:
                rand_hit = Person.Weapon.critical
            else:
                rand_hit = Person.Weapon.power

            if rand_hit_en == 0:
                rand_hit_en = Enemy.critical
            else:
                rand_hit_en = Enemy.damage

            print("\nВыбор противника:", slot_fight_en[z])
            print("Ваш выбор:", slot_fight[z])
            slp(2)

            # Если Атака и Атака
            if slot_fight[z] == "Атака" and slot_fight_en[z] == "Атака":
                if Person.level > Enemy.level:
                    if Person.special == 'Мечник':
                        Enemy.hp -= (round(rand_hit * 0.2, 3) + round(rand_hit * 0.1, 3))
                        print("\nВы атаковали на", round(rand_hit * 0.2, 3), ' + ', round(rand_hit * 0.1, 3), "урона")

                    else:
                        Enemy.hp -= round(rand_hit * 0.1, 3)
                        print("\nВы атаковали на", round(rand_hit * 0.1, 3), "урона")
                    slp(0.7)
                    if Person.special == 'Лучник':
                        print("По вам прошло 0 урона")

                    else:
                        Person.hp -= round(rand_hit_en * 0.1, 3)
                        print("По вам прошло", round(rand_hit_en * 0.1, 3), "урона")

                    slp(1)
                    input("\nENTER чтобы продолжить")

                elif Enemy.level > Person.level:
                    Enemy.hp -= round(rand_hit * 0.1, 3)
                    Person.hp -= round(rand_hit_en * 0.2, 3)
                    print("\nВы атаковали на", round(rand_hit * 0.1, 3), "урона")
                    slp(0.7)
                    print("По вам прошло", round(rand_hit_en * 0.2, 3), "урона")
                    slp(1)
                    input("\nENTER чтобы продолжить")

                else:
                    if Person.special == 'Мечник':
                        Enemy.hp -= (round(rand_hit * 0.2, 3) + round(rand_hit * 0.1, 3))
                        print("\nВы атаковали на", round(rand_hit * 0.2, 3), ' + ', round(rand_hit * 0.1, 3), "урона")
                    else:
                        Enemy.hp -= round(rand_hit * 0.1, 3)
                        print("\nВы атаковали на", round(rand_hit * 0.1, 3), "урона")

                    Person.hp -= round(rand_hit_en * 0.2, 3)
                    slp(0.7)
                    print("По вам прошло", round(rand_hit_en * 0.2, 3), "урона")
                    slp(1)
                    input("\nENTER чтобы продолжить")

            # Если атака и защита (атакующий: персонаж игрока)
            elif slot_fight[z] == "Атака" and slot_fight_en[z] == "Защита":
                Person.stamina -= 0.2

                rand_protect = rdm.randint(0, 3)
                rand_damage_back = rdm.randint(0, 1)
                # Возврат урона
                if rand_damage_back == 0:
                    Person.hp -= round(rand_hit * 0.05, 3)
                    print(Back.RED, Fore.BLACK, "\nВы получили урон (-", round(rand_hit * 0.05, 3), ")", sep='')
                    slp(0.7)
                    input("\nENTER чтобы продолжить")

                if rand_protect == 0:
                    if Person.level > Enemy.level:
                        # Проверка на проход удара через защиту
                        Enemy.hp -= round(rand_hit * 0.1, 3)
                        print(Back.GREEN, Fore.BLACK, "Удалось пробить защиту и атаковать на", round(rand_hit * 0.1, 3))
                        slp(0.9)
                        input("\nENTER чтобы продолжить")
                    else:
                        Enemy.hp -= round(rand_hit * 0.05, 3)
                        print(Back.GREEN, Fore.BLACK, "Удалось пробить защиту и атаковать на",
                              round(rand_hit * 0.05, 3))
                        slp(0.9)
                        input("\nENTER чтобы продолжить")

                else:
                    print("\nНе удалось пробить защиту!")
                    slp(3)
                    input("\nENTER чтобы продолжить")

            # Если атака и защита (атакующий: враг)
            elif slot_fight[z] == "Защита" and slot_fight_en[z] == "Атака":
                Enemy.stamina -= 0.2

                rand_protect = rdm.randint(0, 3)
                rand_damage_back = rdm.randint(0, 1)
                # Возврат урона
                if rand_damage_back == 0:
                    if Person.special == 'Броневик':
                        Enemy.hp -= round(rand_hit_en * 0.14, 3)
                        print(Back.RED, Fore.BLACK, "\nВраг получил урон от щита (-", round(rand_hit_en * 0.14, 3), ")", sep='')

                    else:
                        Enemy.hp -= round(rand_hit_en * 0.05, 3)
                        print(Back.RED, Fore.BLACK, "\nВраг получил урон (-", round(rand_hit_en * 0.05, 3), ")", sep='')
                    slp(0.7)
                    input("\nENTER чтобы продолжить")

                if rand_protect == 0:
                    if Person.level > Enemy.level:
                        # Проверка на проход удара через защиту
                        Person.hp -= round(rand_hit_en * 0.1, 3)
                        print(Back.GREEN, Fore.BLACK, "Врагу удалось пробить защиту и атаковать на",
                              round(rand_hit_en * 0.1, 3))
                        slp(0.9)
                        input("\nENTER чтобы продолжить")
                    else:
                        Person.hp -= round(rand_hit_en * 0.05, 3)
                        print(Back.GREEN, Fore.BLACK, "Врагу удалось пробить защиту и атаковать на",
                              round(rand_hit_en * 0.05, 3))
                        slp(0.9)
                        input("\nENTER чтобы продолжить")

                else:
                    print("\nНе удалось пробить защиту!")
                    slp(3)
                    input("\nENTER чтобы продолжить")

            # Если защита и защита
            if slot_fight[z] == "Защита" and slot_fight_en[z] == "Защита":
                print("\nВы оба решили защититься\n")
                if Person.special == 'Броневик':
                    Enemy.hp -= round(rand_hit * 0.1, 3)
                    print(Person.name,"атаковал щитом на", round(rand_hit * 0.1, 3))

                slp(1)
                input("\nENTER чтобы продолжить")

            # Если пить зелье и атака
            elif slot_fight[z] == "Пить зелье" and slot_fight_en[z] == "Атака":
                Enemy.stamina -= 2
                print("\nВаше зелье было разбито!")
                slp(1)
                print("Удалось частично уклониться от удара (-", round(rand_hit_en / 2, 3), ")")
                slp(3)
                Person.hp -= round(rand_hit_en / 2, 3)
                input("\nENTER чтобы продолжить")

            # Если пить зелье и (защита или отдых)
            elif slot_fight[z] == "Пить зелье" and (slot_fight_en[z] == "Защита" or slot_fight_en[z] == "Отдых"):
                # Для персонажа игрока
                if pot_in == "1":
                    Person.Weapon.power += round(Person.Weapon.power_default * 0.3, 3)
                    print(Back.GREEN, Fore.BLACK)
                    print("\nИспользовано Зелье Силы! (+", round(Person.Weapon.power_default * 0.3, 3), " урона)",
                          sep='')
                    slp(3.3)
                    input("\nENTER чтобы продолжить")
                    pot = True

                elif pot_in == "2":
                    Person.hp += round(Person.hp_default * 0.3, 3)
                    print(Back.GREEN, Fore.BLACK)
                    print("\nИспользовано Зелье Здоровья! (+", round(Person.hp_default * 0.3, 3), " ХП)", sep='')
                    slp(3.3)
                    input("\nENTER чтобы продолжить")
                    pot = True

                elif pot_in == "3":
                    Person.mana += round(Person.mana_default * 0.3, 3)
                    print(Back.GREEN, Fore.BLACK)
                    print("\nИспользовано Зелье Маны! (+", round(Person.mana_default * 0.3, 3), " маны)", sep='')
                    slp(3.3)
                    input("\nENTER чтобы продолжить")
                    pot = True

                # Для врага
                if slot_fight_en[z] == "Защита":
                    print("\n", Enemy.name, "решил защититься")
                    slp(4)

                elif slot_fight_en[z] == "Отдых":
                    Enemy.stamina += round(Enemy.stamina_default, 3)
                    if Enemy.stamina > Enemy.stamina_default:
                        Enemy.stamina = Enemy.stamina_default
                    print("\n", Enemy.name, "решил восстановить выносливость")
                    slp(4)

            # Если отдых и (защита или отдых)
            elif slot_fight[z] == "Отдых" and (slot_fight_en[z] == "Защита" or slot_fight_en[z] == "Отдых"):
                # Для персонажа игрока
                Person.stamina += round(Person.stamina_default * 0.4)
                if Person.stamina > Person.stamina_default:
                    print("\nВы удачно восстановили", Person.stamina - Person.stamina_default, "выносливости.")
                    Person.stamina = Person.stamina_default
                else:
                    print("\nВы удачно восстановили", round(Person.stamina_default * 0.4), "выносливости.")
                slp(2.8)

                # Для врага
                if slot_fight_en[z] == "Защита":
                    print("\n", Enemy.name, "решил защититься")
                    input("\nENTER чтобы продолжить")

                elif slot_fight_en[z] == "Отдых":
                    Enemy.stamina += round(Enemy.stamina_default, 3)
                    if Enemy.stamina > Enemy.stamina_default:
                        Enemy.stamina = Enemy.stamina_default
                    print("\n", Enemy.name, "решил восстановить выносливость")
                    input("\nENTER чтобы продолжить")

            # Если отдых и атака
            elif slot_fight[z] == "Отдых" and slot_fight_en[z] == "Атака":
                Person.stamina += round(Person.stamina_default * 0.2, 3)
                if Person.stamina > Person.stamina_default:
                    print("\nВы восстановили", Person.stamina - Person.stamina_default, "выносливости,\n"
                                                                                       "Но", Enemy.name,
                          "атаковал вас!")
                    Person.stamina = Person.stamina_default
                else:
                    print("\nВы восстановили", round(Person.stamina_default * 0.2, 3), "выносливости,\n"
                                                                                       "Но", Enemy.name,
                          "атаковал вас!")

                slp(3)
                print("-", rand_hit_en, sep='')
                input("\nENTER чтобы продолжить")
                Person.hp -= rand_hit_en

            # Если атака и отдых
            elif slot_fight[z] == "Атака" and slot_fight_en[z] == "Отдых":
                Enemy.stamina += round(Enemy.stamina_default * 0.2, 3)
                if Enemy.stamina > Enemy.stamina_default:
                    Enemy.stamina = Enemy.stamina_default
                print("\nВраг восстановил выносливость,\n"
                      "Но", Person.name, "атаковал!")
                slp(3)
                print("-", rand_hit, " урона", sep='')
                input("\nENTER чтобы продолжить")
                Enemy.hp -= rand_hit

            # Если защита и отдых
            elif slot_fight[z] == "Защита" and slot_fight_en[z] == "Отдых":
                print(Person.name, "Бесполезно защитился")
                slp(3)

                Enemy.stamina += round(Enemy.stamina_default, 3)
                if Enemy.stamina > Enemy.stamina_default:
                    Enemy.stamina = Enemy.stamina_default
                print("\n", Enemy.name, "решил восстановить выносливость")
                input("\nENTER чтобы продолжить")

            # Если атака и пить зелье (враг его пьёт)
            elif slot_fight[z] == "Атака" and slot_fight_en[z] == "Пить зелье":
                print(Back.WHITE,Fore.BLACK)
                print("\nЗелье врага разбилось, но тот успел уклониться от удара")
                slp(1.8)
                print(" -",round(rand_hit/2, 3)," урона по врагу", sep='')
                Enemy.hp -= round(rand_hit/2, 3)
                input("\nENTER чтобы продолжить")

            # Если защита и пить зелье (враг его пьёт)
            elif slot_fight[z] == "Защита" and slot_fight_en[z] == "Пить зелье":
                print(Back.WHITE, Fore.BLACK)
                print(Person.name, "Бесполезно защитился")
                slp(1)
                if Enemy.rand_potion_en == "Зелье силы":
                    Enemy.damage += round(Enemy.damage * 0.29, 3)
                    print(Enemy.name," использовал Зелье силы (+",round(Enemy.damage * 0.29, 3)," к урону)")
                    slp(2)
                    input("\nENTER чтобы продолжить")
                elif Enemy.rand_potion_en == "Зелье здоровья":
                    Enemy.hp += round(Enemy.hp_default * 0.3, 3)
                    print(Enemy.name, " использовал Зелье здоровья (+", round(Enemy.hp_default * 0.3, 3), " к здоровью)")
                    slp(2)
                    input("\nENTER чтобы продолжить")

            # Если отдых и пить зелье
            elif slot_fight[z] == "Отдых" and slot_fight_en[z] == "Пить зелье":
                # Для персонажа игрока
                Person.stamina += round(Person.stamina_default * 0.4)
                if Person.stamina > Person.stamina_default:
                    print("\nВы удачно восстановили", Person.stamina - Person.stamina_default, "выносливости.")
                    Person.stamina = Person.stamina_default
                else:
                    print("\nВы удачно восстановили", round(Person.stamina_default * 0.4), "выносливости.")
                slp(2.8)

                # Для противника
                if Enemy.rand_potion_en == "Зелье силы":
                    Enemy.damage += round(Enemy.damage * 0.29, 3)
                    print(Enemy.name," использовал Зелье силы (+",round(Enemy.damage * 0.29, 3)," к урону)")
                    slp(2)
                    input("\nENTER чтобы продолжить")
                elif Enemy.rand_potion_en == "Зелье здоровья":
                    Enemy.hp += round(Enemy.hp_default * 0.3, 3)
                    print(Enemy.name, " использовал Зелье здоровья (+", round(Enemy.hp_default * 0.3, 3), " к здоровью)")
                    slp(2)
                    input("\nENTER чтобы продолжить")

            # Если у обоих пить зелье
            elif slot_fight[z] == "Пить зелье" and slot_fight_en[z] == "Пить зелье":
                # Для персонажа игрока
                if pot_in == "1":
                    Person.Weapon.power += round(Person.Weapon.power_default * 0.3, 3)
                    print(Back.GREEN, Fore.BLACK)
                    print("\nИспользовано Зелье Силы! (+", round(Person.Weapon.power_default * 0.3, 3), " урона)",
                          sep='')
                    slp(3.3)
                    pot = True

                elif pot_in == "2":
                    Person.hp += round(Person.hp_default * 0.3, 3)
                    print(Back.GREEN, Fore.BLACK)
                    print("\nИспользовано Зелье Здоровья! (+", round(Person.hp_default * 0.3, 3), " ХП)", sep='')
                    slp(3.3)
                    input("\nENTER чтобы продолжить")
                    pot = True

                elif pot_in == "3":
                    Person.mana += round(Person.mana_default * 0.3, 3)
                    print(Back.GREEN, Fore.BLACK)
                    print("\nИспользовано Зелье Маны! (+", round(Person.mana_default * 0.3, 3), " маны)", sep='')
                    slp(3.3)
                    input("\nENTER чтобы продолжить")
                    pot = True

                    # Для противника
                    if Enemy.rand_potion_en == "Зелье силы":
                        Enemy.damage += round(Enemy.damage * 0.29, 3)
                        print(Enemy.name, " использовал Зелье силы (+", round(Enemy.damage * 0.29, 3), " к урону)")
                        slp(2)
                        input("\nENTER чтобы продолжить")
                    elif Enemy.rand_potion_en == "Зелье здоровья":
                        Enemy.hp += round(Enemy.hp_default * 0.3, 3)
                        print(Enemy.name, " использовал Зелье здоровья (+", round(Enemy.hp_default * 0.3, 3),
                              " к здоровью)")
                        slp(2)
                        input("\nENTER чтобы продолжить")
            # Для ИИ (предполагаемые статы здоровья)
            t_hp = Person.hp  # Противника
            t_hp_self = Enemy.hp  # Свои



# Вход в дандж и само путешествие
def dunge():
    # Ввод данных в класс Dunge (см dunges.py)
    if Person.current_dunge == "Лес":
        d.forest()
    elif Person.current_dunge == "Подземелье":
        d.dungeon()
    elif Person.current_dunge == "Густой лес":
        d.dense_forest()
    elif Person.current_dunge == "Заброшенный замок":
        d.castle()
    elif Person.current_dunge == "Супер-Подземелье":
        d.super_dungeon()
    else:
        d.emerald_forest()

    # Цикл, длина которого определяется длиной данджа
    for lm in range(d.Dunge.level_max):

        ######
        # Проверка на переполнение инвентаря
        if Person.potion_pow > 9:
            Person.potion_pow = 9
        elif Person.potion_heal > 9:
            Person.potion_heal = 9
        elif Person.potion_mana > 9:
            Person.potion_mana = 9
        elif Person.pack_chest > 9:
            Person.pack_chest = 9
        ######

        die = False
        if Person.hp < 0:
            die = True
            # Настройки по умолчанию
            Person.hp = Person.hp_default
            Person.Weapon.power = Person.Weapon.power_default
            Person.Weapon.critical = Person.Weapon.critical_default
            Person.stamina = Person.stamina_default
            Person.mana = Person.mana_default

            Person.day += 1

            Enemy.hp = Enemy.hp_default
            Enemy.stamina = Enemy.stamina_default
            slp(2)
            break

        enemy_choose(this_enemy)
        cls()
        print("\n\n")
        slp(1)
        print(Back.GREEN, Fore.BLACK)
        print("======================================")
        print(Back.MAGENTA, Fore.WHITE)
        print("Дандж: ", d.Dunge.name)
        print("Текущая часть данджа: ", d.Dunge.level + 1)
        print("ХП: ", Person.hp)
        print("Зелий Силы: ", Person.potion_pow)
        print("Зелий Здоровья: ", Person.potion_heal)

        if Person.special == "Маг":
            print("Зелий Маны: ", Person.potion_mana)

        print(Back.GREEN, Fore.BLACK)
        print("======================================")
        slp(4)
        print(Back.WHITE, Fore.BLACK)
        print("\nАнализ:", end='')

        for i in range(1, rdm.randint(4,10)):
            print('#', end='', flush=True)
            slp(0.6)

        slp(1)
        # Встречи
        rand_event = rdm.randint(0, 5)
        if rand_event == 0:
            slot_fight = []
            slot_fight_en = []
            reset_ai()
            fight(v1, v2, v3, v4)
            d.Dunge.level += 1

        elif rand_event == 2 or rand_event == 3 :
            slp(1.5)
            print(Back.GREEN, Fore.BLACK)
            print("\n", Person.name, "нашёл сундук! (+1 сундук в инвентарь)")

            if Person.pack_chest < 9:
                Person.pack_chest += 1

            else:
                print('\nИнвентарь сундуков полон!')

            d.Dunge.level += 1
            slp(4)
        elif rand_event == 4 or rand_event == 5 or rand_event == 1:
            slp(1.5)
            print(Back.WHITE, Fore.BLACK)
            print("\n", Person.name, "ничего не отыскал...")
            d.Dunge.level += 1
            slp(3.5)

    # После прохождения данджа

    # Настройки по умолчанию
    Person.hp = Person.hp_default
    Person.Weapon.power = Person.Weapon.power_default
    Person.Weapon.critical = Person.Weapon.critical_default
    Person.stamina = Person.stamina_default
    Person.mana = Person.mana_default

    Person.day += 1

    Enemy.hp = Enemy.hp_default
    Enemy.stamina = Enemy.stamina_default

    if die == False:
        slp(3)
        print(Back.GREEN, Fore.BLACK)
        print("\nВам удалось пройти дандж ", d.Dunge.name, "!", sep='')
        slp(2.5)
        # Начисление XP
        Person.xp += round(d.Dunge.xp, 3)
        print("**Вы получили", round(d.Dunge.xp, 3), "опыта**")
        slp(3.5)
        if Person.xp >= Person.multiplier:
            Person.level += 1

            if Person.level == 2:
                print("\nРазблокировано достижение — 'Получите 2 уровень'!\n")
                slp(2)
                Person.ach_3 = "Выполнено!"
                m_write_achievements()
            if Person.level == 10:
                print("\nРазблокировано достижение — 'Получите 10 уровень'!\n")
                slp(2)
                Person.ach_4 = "Выполнено!"
                m_write_achievements()

            if Person.level == 30:
                print("\nРазблокировано достижение — 'Получите 30 уровень'!\n")
                slp(2)
                Person.ach_6 = "Выполнено!"
                m_write_achievements()

            if Person.level == 40:
                print("\nРазблокировано достижение — 'Получите 40 уровень'!\n")
                slp(2)
                Person.ach_7 = "Выполнено!"
                m_write_achievements()

            if Person.level == 50:
                print("\nРазблокировано достижение — 'Получите 50 уровень'!\n")
                slp(2)
                Person.ach_8 = "Выполнено!"
                m_write_achievements()

            if Person.level == 60:
                print("\nРазблокировано достижение — 'Получите 60 уровень'!\n")
                slp(2)
                Person.ach_9 = "Выполнено!"
                m_write_achievements()

            Person.xp -= Person.multiplier
            print("")
            print(Person.name, " получил новый уровень! (", Person.level, ")", sep='')
            Person.hp = 18 + (Person.level + 1)
            Person.hp_default = 18 + (Person.level + 1)
            Person.stamina = Person.hp / 3
            Person.stamina_default = Person.hp / 3
            Person.multiplier = Person.level * 12
            Person.mana = 10 + Person.level
            Person.mana_default = 10 + Person.level

        if Person.xp >= Person.Weapon.multiplier:
            Person.Weapon.level_w += 1
            print("")
            print("Оружие ", Person.name, " получило новый уровень! (", Person.Weapon.level_w, ")", sep='')
            Person.Weapon.power = 5 + Person.Weapon.level_w
            Person.Weapon.power_default = 5 + Person.Weapon.level_w
            Person.Weapon.critical = Person.Weapon.power * 1.5
            Person.Weapon.multiplier = Person.Weapon.level_w * 9

        m_write_save()
        m_write_pack()
        input("Нажмите ENTER для продолжения")
        menu()

    else:
        slp(1.5)
        print(Back.RED, Fore.BLACK)
        print("\nВам не удалось пройти даднж", d.Dunge.name)
        slp(2)
        # Начисление XP
        Person.xp += round(d.Dunge.xp / 2, 3)
        print("**Вы получили", round(d.Dunge.xp / 2, 3), "опыта**")
        slp(3.5)
        if Person.xp >= Person.multiplier:
            Person.level += 1

            if Person.level == 2:
                print("\nРазблокировано достижение — 'Получите 2 уровень'!\n")
                slp(2)
                Person.ach_3 = "Выполнено!"
                m_write_achievements()
            if Person.level == 10:
                print("\nРазблокировано достижение — 'Получите 10 уровень'!\n")
                slp(2)
                Person.ach_4 = "Выполнено!"
                m_write_achievements()

            if Person.level == 30:
                print("\nРазблокировано достижение — 'Получите 30 уровень'!\n")
                slp(2)
                Person.ach_6 = "Выполнено!"
                m_write_achievements()

            if Person.level == 40:
                print("\nРазблокировано достижение — 'Получите 40 уровень'!\n")
                slp(2)
                Person.ach_7 = "Выполнено!"
                m_write_achievements()

            if Person.level == 50:
                print("\nРазблокировано достижение — 'Получите 50 уровень'!\n")
                slp(2)
                Person.ach_8 = "Выполнено!"
                m_write_achievements()

            if Person.level == 60:
                print("\nРазблокировано достижение — 'Получите 60 уровень'!\n")
                slp(2)
                Person.ach_9 = "Выполнено!"
                m_write_achievements()

            Person.xp -= Person.multiplier
            print("")
            print(Person.name, " получил новый уровень! (", Person.level, ")", sep='')
            Person.hp = 18 + (Person.level + 1)
            Person.hp_default = 18 + (Person.level + 1)
            Person.stamina = Person.hp / 3
            Person.stamina_default = Person.hp / 3
            Person.multiplier = Person.level * 12
            Person.mana = 10 + Person.level
            Person.mana_default = 10 + Person.level

        if Person.xp >= Person.Weapon.multiplier:
            Person.Weapon.level_w += 1
            print("")
            print("Оружие ", Person.name, " получило новый уровень! (", Person.Weapon.level_w, ")", sep='')
            Person.Weapon.power = 5 + Person.Weapon.level_w
            Person.Weapon.power_default = 5 + Person.Weapon.level_w
            Person.Weapon.critical = Person.Weapon.power * 1.5
            Person.Weapon.multiplier = Person.Weapon.level_w * 9
        m_write_pack()
        m_write_save()
        menu()


def boost_dunge():
    # Выбор буста в начале
    # Недоделал
    while True:
        slp(1)
        if Person.potion_heal > 0 or Person.potion_pow > 0 or (Person.potion_mana > 0 and Person.special == 'Маг'):
            print('\nВыбор буста:')
            if Person.potion_heal > 0:
                print("1. Зелье Здоровья:", Person.potion_heal)
            if Person.potion_pow > 0:
                print('2. Зелье Силы:', Person.potion_pow)
            if Person.potion_mana > 0 and Person.special == 'Маг':
                print('3. Зелье Маны:', Person.potion_mana)

            print('n - Ничего')
            boost = input('\nВаш выбор: ==>')
            if boost == '1' and Person.potion_heal > 0:
                print('Ваш выбор - Зелье Здоровья')
                slp(2)
                Person.potion_heal -= 1
                Person.hp += round(Person.hp_default * 0.3, 3)
                break

            elif boost == '2' and Person.potion_pow > 0:
                print('Ваш выбор - Зелье Силы')
                slp(2)
                Person.potion_pow -= 1
                Person.Weapon.power += round(Person.Weapon.power_default * 0.3, 3)
                break

            elif boost == '3' and Person.potion_mana > 0 and Person.special == 'Маг':
                print('Ваш выбор - Зелье Маны')
                slp(2)
                Person.potion_mana -= 1
                Person.mana += round(Person.mana_default * 0.3, 3)
                break

            elif boost == 'n' or boost == 'N':
                break

            else:
                print(Fore.BLACK, Back.RED, 'Выберите зелье из списка!')
                slp(2)

            cls()

        else:
            break
    countdown_d()

    # Второй цикл для поиска игрока-бота (уровень игрока должен быть минимум 5!)
    f = True
    while f == True:
        if Person.level > 4:
            print(Fore.BLACK, Back.WHITE)
            slp(1)
            helper = input('\nХотите поискать помощника? 0 - нет/1 - да\n   ==>')
            if helper == '0':
                f = False
                break
            elif helper == '1':
                cls()
                rand_help = rdm.randint(1,4)
                search = int(rdm.randint(50,150) / 100 * 10)
                help_search = 0
                print(Fore.BLACK, Back.WHITE)
                while help_search < 100:
                    print(Fore.BLACK, Back.WHITE)
                    print('\n\nПоиск... | {0}% |'.format(help_search))
                    help_search += search
                    slp(0.5)
                    cls()
                if rand_help == 1:
                    print(Fore.BLACK, Back.WHITE)
                    print('\nПомощник найден!')
                    slp(1)

                    if Person.coins < 20:
                        pay_help = rdm.randint(1, 5)
                    else:
                        pay_help = rdm.randint(3, 10)

                    while True:
                        print('Помощник', rdm.choice(name_list), 'требует', pay_help, 'монет.','\n\nОплатить? 0 - нет/1 - да')
                        pay_help_choice = input('\n  ==>')
                        if pay_help_choice == '0':
                            f = False
                            break
                        elif pay_help_choice == '1':
                            if pay_help <= Person.coins:
                                print(Fore.BLACK,Back.GREEN,'\nОплата произведена!')
                                Person.coins -= pay_help
                                slp(2.5)

                                # Прибавка к статам
                                rand_help_h = Person.hp_default / 4 + rdm.randint(1,4)
                                rand_help_p = Person.Weapon.power_default / 4 + rdm.randint(1,2)
                                slp(1)
                                print(Back.GREEN, Fore.BLACK,'\nHP + {0}\nСила Оружия + {1}'.format(rand_help_h,rand_help_p))
                                Person.hp += rand_help_h
                                Person.Weapon.power += rand_help_p
                                slp(1)
                                input('\nENTER для входа в дандж')
                                f = False
                                break
                            else:
                                print(Fore.WHITE,Back.RED,'\nНедостаточно монет!')
                                slp(3)
                                f = False
                                break

                else:
                    print('\nНе удалось найти помощника.')
                    slp(3)
                    f = False
                    break

# Выбор данджа
def countdown_d():
    slp(2)
    сount_down = 5
    for i in range(5):
        cls()
        print(Back.WHITE, Fore.BLACK)
        print("Вход через ", end='')
        print(сount_down)
        slp(1)
        сount_down -= 1
        cls()

    dunge()  # Вызов игры

def go_dunge():

    #####
    # Фикс бага с "дефолтным" критом
    Person.Weapon.critical = Person.Weapon.power * 1.5
    Person.Weapon.critical_default = Person.Weapon.power * 1.5
    #####

    if start_new:
        cls()
        Person.a_0 += 1
        if Person.a_0 > 1 and Person.a_0 < 3:
            print("\nРазблокировано достижение — 'ПРОЙДИТЕ ОБУЧЕНИЕ'!\n")
            slp(2)
            Person.ach_0 = "Выполнено!"
            m_write_achievements()

        print(Back.WHITE, Fore.BLACK, '\nЧто ж, мы дошли до самого интересного - до походов в данджи...')
        input('\nНажми ENTER для продолжения')
        print('\nЗдесь, по сути, происходит набив опыта и прочих плюшек. На данджах основана вся игра.')
        slp(3)
        input('\nНажми ENTER для продолжения')
        print(Fore.WHITE, Back.BLACK)
        slp(1.5)
        cls()
        print(Back.WHITE, Fore.BLACK, '\nКак играть?')
        print(
            'Игра не замысловата. Выбираешь вид данджа (открывается по мере роста уровня игрока),\n Сражаешься с врагами и другими игроками (они не совсем настоящие), и открываешь сундуки.\nОпыт за прохождение данджа тоже имеется.')
        input('\nНажми ENTER для продолжения')
        cls()
        print(Fore.WHITE, Back.BLACK)
        slp(1.5)
        print('Что ж, теперь ты полноценный игрок в OFFLINE RPG!')
        input('\nНажми ENTER для выбора данджей')
    cls()
    print(Back.GREEN, Fore.BLACK)
    print('=========OFFLINE RPG========')
    print('Опыт:', Person.xp)
    print('Уровень:', Person.level)
    print('Монет:', Person.coins)
    print('Кристаллов: ', Person.crystals)
    print("")

    print(Back.MAGENTA, Fore.WHITE)

    print("0 - Лес (1 уровень)")
    print("1 - Подземелье (10 уровень)")

    if Person.can_dunge >= 1:  # См. класс Person
        print("2 - Густой лес (30 уровень)")

    if Person.can_dunge >= 2:
        print("3 - Заброшенный замок (40 уровень)")

    if Person.can_dunge >= 3:
        print("4 - Супер-Подземелье (50 уровень)")

    if Person.can_dunge >= 4:
        print("5 - Изумрудный лес (60 уровень)")

    print("ENTER - выход")

    # Выбор данджа
    choose = input("\nВаш выбор: ==> ")

    if choose == "0":
        if Person.ach_1 == "Не выполнено":
            print("\nРазблокировано достижение — 'Сходите первый раз в дандж'!\n")
            slp(3)
            Person.ach_1 = "Выполнено!"
            m_write_achievements()
        slp(0.5)

        print(Back.WHITE, Fore.BLACK)  # Белый фон, чёрный шрифт (фон битв)
        print("\nВаш выбор: Лес")
        Person.current_dunge = "Лес"
        boost_dunge()

    elif choose == "1":
        if Person.level < 10:
            print("\nВы не достигли 10 уровня!")
            slp(3)
            cls()
            go_dunge()
        else:
            if Person.ach_5 != "Выполнено!":
                print("\nРазблокировано достижение — 'Сходите в дандж 'Подземелье''!\n")
                slp(2)
                Person.ach_5 = "Выполнено!"
                m_write_achievements()

            print(Back.WHITE, Fore.BLACK)  # Белый фон, чёрный шрифт (фон битв)
            print("\nВаш выбор: Подземелье")
            Person.current_dunge = "Подземелье"
            boost_dunge()

    elif choose == "2" and Person.level > 9:
        if Person.level < 30:
            print("\nВы не достигли 30 уровня!")
            slp(3)
            cls()
            go_dunge()
        else:
            print(Back.WHITE, Fore.BLACK)  # Белый фон, чёрный шрифт (фон битв)
            print("\nВаш выбор: Густой лес")
            Person.current_dunge = "Густой лес"
            boost_dunge()

    elif choose == "3" and Person.level > 29:
        if Person.level < 40:
            print("\nВы не достигли 40 уровня!")
            slp(3)
            cls()
            go_dunge()
        else:
            print(Back.WHITE, Fore.BLACK)  # Белый фон, чёрный шрифт (фон битв)
            print("\nВаш выбор: Заброшенный замок")
            Person.current_dunge = "Заброшенный замок"
            boost_dunge()

    elif choose == "4" and Person.level > 39:
        if Person.level < 50:
            print("\nВы не достигли 50 уровня!")
            slp(3)
            cls()
            go_dunge()
        else:
            print(Back.WHITE, Fore.BLACK)  # Белый фон, чёрный шрифт (фон битв)
            print("\nВаш выбор: Супер-Подземелье")
            Person.current_dunge = "Супер-Подземелье"
            boost_dunge()

    elif choose == "5" and Person.level > 49:
        if Person.level < 60:
            print("\nВы не достигли 60 уровня!")
            slp(3)
            cls()
            go_dunge()
        else:
            print(Back.WHITE, Fore.BLACK)  # Белый фон, чёрный шрифт (фон битв)
            print("\nВаш выбор: Изумрудный лес")
            Person.current_dunge = "Изумрудный лес"
            boost_dunge()

    elif choose == "":
        menu()

    else:
        print("\nВыберите дандж из списка!")
        slp(3)
        cls()
        go_dunge()


# Загрузка сохранения
save = open('System/save.txt', 'r')
###########
# Загрузка класса персонажа
save.seek(0)
save.readline()
Person.special = str(save.readline())
if Person.special == 'Мечник\n':
    Person.special = 'Мечник'
    Person.Weapon.critical *= 1.2
    Person.hp *= 0.9
elif Person.special == 'Лучник\n':
    Person.special = 'Лучник'
    Person.Weapon.power *= 1.12
    Person.hp *= 0.89
elif Person.special == 'Маг\n':
    Person.special = 'Маг'
    Person.hp *= 0.75
elif Person.special == 'Броневик\n':
    Person.special = 'Броневик'
    Person.hp *= 1.2
    Person.Weapon.power *= 0.8

###########
save.seek(0)  # Сброс на начало файла

# Загрузка опыта, уровня, монет и кристаллов
###########
# xp
for i in range(2):
    save.readline()
Person.xp = float(save.readline())
save.seek(0)
# level
for i in range(3):
    save.readline()
Person.level = int(save.readline())
Person.hp = 18 + (Person.level + 1)
Person.hp_default = 18 + (Person.level + 1)
Person.stamina = Person.hp / 3
Person.stamina_default = Person.hp / 3
Person.multiplier = Person.level * 12
Person.mana = 10 + Person.level
Person.mana_default = 10 + Person.level

if Person.level > 9 and Person.level < 30:
    Person.can_dunge = 1

elif Person.level > 29 and Person.level < 40:
    Person.can_dunge = 2

elif Person.level > 39 and Person.level < 50:
    Person.can_dunge = 3

elif Person.level > 49:
    Person.can_dunge = 4

save.seek(0)

# coins
for i in range(5):
    save.readline()
Person.coins = int(save.readline())
save.seek(0)
# crystals
for i in range(6):
    save.readline()
Person.crystals = int(save.readline())
save.seek(0)
###########
# Загрузка уровня оружия
for i in range(4):
    save.readline()
Person.Weapon.level_w = int(save.readline())
Person.Weapon.power = 5 + Person.Weapon.level_w
Person.Weapon.power_default = 5 + Person.Weapon.level_w
Person.Weapon.critical = Person.Weapon.power * 1.5
Person.Weapon.multiplier = Person.Weapon.level_w * 9
save.seek(0)
###########
# Загрузка дней, проведённых за игрой
###########
for i in range(7):
    save.readline()
Person.day = int(save.readline())
save.seek(0)
###########
# Загрузка названия оружия
###########
for i in range(8):
    save.readline()
Person.Weapon.name = str(save.readline())
if Person.Weapon.name == "Меч\n":
    Person.Weapon.name = "Меч"
elif Person.Weapon.name == "Лук\n":
    Person.Weapon.name = "Лук"
elif Person.Weapon.name == "Магическая трость\n":
    Person.Weapon.name = "Магическая трость"
elif Person.Weapon.name == "Щит\n":
    Person.Weapon.name = "Щит"
###########
# Загрузка статистики
###########
save.seek(0)
# заработано монет
for i in range(9):
    save.readline()
Person.Stats.coins_up = int(save.readline())

# Заработано кристаллов
save.seek(0)
for i in range(10):
    save.readline()
Person.Stats.crystals_up = int(save.readline())

# Всего открытых сундуков
save.seek(0)
for i in range(11):
    save.readline()
Person.Stats.chests_open = int(save.readline())

save.close()  # Закрытие сохранения

# Загрузка инвентаря
save_inventory = open('System/pack.txt', 'r')
###########
# Загрузка зелья силы
save_inventory.seek(0)
Person.potion_pow = int(save_inventory.read(1))
###########
# Загрузка зелья здоровья
save_inventory.seek(1)
Person.potion_heal = int(save_inventory.read(1))
###########
# Загрузка зелья маны
save_inventory.seek(2)
Person.potion_mana = int(save_inventory.read(1))
###########
# Загрузка сундуков
save_inventory.seek(3)
Person.pack_chest = int(save_inventory.read(1))
###########

# Загрузка имени
text_name = open('System/name.txt', 'r')
Person.name = str(text_name.read())
text_name.close()

cls()
if start_new == True:
    print('\nВот меню, которое ты будешь видеть при каждом заходе в игру. Пора уже привыкать...\n')
    input('\nНАЖМИ ENTER ЧТОБЫ ЕГО УВИДЕТЬ')
    cls()

# Загрузка достижений
achievements = open('System/achievements.txt', 'r')
achievements.seek(0)

# Всё сразу
Person.ach_0 = achievements.readline()
Person.ach_1 = achievements.readline()
Person.ach_2 = achievements.readline()
Person.ach_3 = achievements.readline()
Person.ach_4 = achievements.readline()
Person.ach_5 = achievements.readline()
Person.ach_6 = achievements.readline()
Person.ach_7 = achievements.readline()
Person.ach_8 = achievements.readline()
Person.ach_9 = achievements.readline()

if Person.ach_0 == "Не выполнено\n":
    Person.ach_0 = "Не выполнено"
if Person.ach_1 == "Не выполнено\n":
    Person.ach_1 = "Не выполнено"
if Person.ach_2 == "Не выполнено\n":
    Person.ach_2 = "Не выполнено"
if Person.ach_3 == "Не выполнено\n":
    Person.ach_3 = "Не выполнено"
if Person.ach_4 == "Не выполнено\n":
    Person.ach_4 = "Не выполнено"
if Person.ach_5 == "Не выполнено\n":
    Person.ach_5 = "Не выполнено"
if Person.ach_6 == "Не выполнено\n":
    Person.ach_6 = "Не выполнено"
if Person.ach_7 == "Не выполнено\n":
    Person.ach_7 = "Не выполнено"
if Person.ach_8 == "Не выполнено\n":
    Person.ach_8 = "Не выполнено"
if Person.ach_9 == "Не выполнено\n":
    Person.ach_9 = "Не выполнено"

if Person.ach_0 == "Выполнено!\n":
    Person.ach_0 = "Выполнено!"
if Person.ach_1 == "Выполнено!\n":
    Person.ach_1 = "Выполнено!"
if Person.ach_2 == "Выполнено!\n":
    Person.ach_2 = "Выполнено!"
if Person.ach_3 == "Выполнено!\n":
    Person.ach_3 = "Выполнено!"
if Person.ach_4 == "Выполнено!\n":
    Person.ach_4 = "Выполнено!"
if Person.ach_5 == "Выполнено!\n":
    Person.ach_5 = "Выполнено!"
if Person.ach_6 == "Выполнено!\n":
    Person.ach_6 = "Выполнено!"
if Person.ach_7 == "Выполнено!\n":
    Person.ach_7 = "Выполнено!"
if Person.ach_8 == "Выполнено!\n":
    Person.ach_8 = "Выполнено!"
if Person.ach_9 == "Выполнено!\n":
    Person.ach_9 = "Выполнено!"

achievements.close()

menu()
