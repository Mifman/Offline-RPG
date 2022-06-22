import random as rdm
from time import sleep as slp
from os import system # для быстрой очистки экрана

# Проверка наличия dunges.py
try:
    import dunges as d # файл dunges.py
except ModuleNotFoundError:
    print('ОШИБКА! В КОРНЕВОМ КАТАЛОГЕ НЕ НАЙДЕН ФАЙЛ "dunges.py"')
    slp(99999)

from colorama import init
from colorama import Fore, Back, Style
init()

# Технические переменные
##################
start_new = False # Изначально обучение отключено. Оно включается только в самом начале прохождения
x = 0 # Для рынка

# БОТ
v1 = 0
v2 = 0
v3 = 0

# Выбор попавшегося врага
this_enemy = False # True, если данный враг может попасться в данном дандже
enemy_forest = ["Гоблин", "Орк", "Кикимора", "Энт", "Кентавр", "Тролль", "Тэнгу", "Оборотень", "Персонаж"]
enemy_dungeon = ["Гоблин", "Орк", "Кикимора", "Тролль", "Оборотень", "Персонаж", "Паук", "Элементаль", "Горгона", "Скелет", "Зомби"]
enemy_dense_forest = ["Гоблин", "Орк", "Кикимора", "Энт", "Кентавр", "Тролль", "Тэнгу", "Оборотень", "Персонаж", "Паук", "Элементаль", "Горгона", "Циклоп"]
enemy_castle = ["Гоблин", "Орк", "Кикимора", "Тролль", "Персонаж", "Паук", "Элементаль", "Горгона", "Скелет", "Зомби", "Лич", "Демон"]
enemy_super_dungeon = ["Гоблин", "Орк", "Кикимора", "Тролль", "Персонаж", "Паук", "Элементаль", "Горгона", "Скелет", "Зомби", "Лич", "Демон"]
enemy_emerald_forest = ["Орк", "Кикимора", "Тролль", "Оборотень", "Персонаж", "Паук", "Элементаль", "Горгона", "Демон", "Циклоп", "Кентавр", "Энт", "Тэнгу"]
#enemy_list = ["Гоблин", "Орк", "Паук", "Кикимора","Энт", "Кентавр", "Элементаль", "Тролль","Циклоп", "Демон", "Тэнгу", "Горгона", "Скелет","Оборотень", "Лич", "Зомби", "Персонаж"]

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
    print('\nПРОГРАММА: Папки "System" в корневом каталоге не существует.\nПожалуйста, создайте её, и тогда у меня как у программы\nПоявится возможность создать файлы в ней. :з')
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
    xp = 0 # Опыт
    level = 1 # Уровень
    multiplier = level * 12 # Множитель уровня (именно столько нужно опыта для достижения нового уровня)
    day = 0  # Дни, проведённые за игрой (игровые, вычисляются битвами)
    can_dunge = 0 # Переменная, позволяющая ходить на другие данджи (нужна в меню выбора данджа. Она играет чисто декоративную роль)
    current_dunge = None # Переменная, определяющая в каком дандже сейчас находится игрок
    coins = 50
    crystals = 1

    # Для битв
    hp = 18 + (level + 1) # Кол-во жизней
    hp_default = 18 + (level + 1) # По умолчанию
    stamina = hp / 3 # Выносливость персонажа
    stamina_default = hp / 3 # По умолчанию
    mana = 10 + level # Если класс персонажа Маг, данная переменная играет роль, в остальном нет
    mana_default = 10 + level # По умолчанию

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
    price_0 = rdm.randint(3,30)
    price_1 = rdm.randint(3,30)
    price_2 = rdm.randint(3,45)
    price_3 = rdm.randint(5,30)
    price_4 = rdm.randint(3,20)

# Пересохраение основного "save.txt"
def m_write_save():
    save = open('System/save.txt', 'w')
    save.write('1\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n{10}'.format(Person.special,Person.xp,Person.level,Person.Weapon.level_w,Person.coins,Person.crystals,Person.day,Person.Weapon.name,Person.Stats.coins_up,Person.Stats.crystals_up,Person.Stats.chests_open))
    save.close()

# Пересохраение инвентаря игрока (pack.txt)
def m_write_pack():
    save_inventory = open('System/pack.txt', 'w')
    save_inventory.seek(0)
    save_inventory.write('{0}{1}{2}{3}'.format(Person.potion_pow, Person.potion_heal, Person.potion_mana, Person.pack_chest))
    save_inventory.close()

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

# ВНИМАНИЕ! При проверке и одновременно чтение файла, чтение сдвигается!
save = open('System/save.txt', 'r')
save.seek(0)
if save.read(1) != '0': # Суть данного if-а: Если сохранение было изменено: то ...
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
    print('\nВаше новое имя:',Person.name)
    print('\nЧтобы его изменить, пройдите по пути:\n "Корневая папка/System/name.txt"\nИ прописывайте новое, оригинальное на ваш взгляд имя :)\n\n',Back.RED,Fore.WHITE,'ВНИМАНИЕ! Настоятельно не рекомендуем удалять файлы из папки "System"!\n')
    print(Fore.WHITE,Back.BLACK)
    slp(5)
    text_name.close()
    # Выбор класса перса
    print('\n\n КЛАССЫ:\n0 - МЕЧНИК (Основное оружие: Меч)\n1 - ЛУЧНИК (Основное оружие: Лук)\n2 - МАГ (Основное оружие: Магическая трость)\n3 - БРОНЕВИК (Основное оружие: Щит)')

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

    save.writelines(['1\n', '{0}\n'.format(Person.special), '0\n','{0}\n'.format(Person.level) ,'0\n', '50\n', '1\n', '0\n', Person.Weapon.name, '\n0\n', '0\n', '0'])
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
    print('В данный момент, у тебя должно быть в карманах 50 монет и 1 кристалл.\nЭто так называемая игровая валюта, на которую можно покупать различные предметы, а также прокачивать своего персонажа.\n')
    input('ДЛЯ ПРОДОЛЖЕНИЯ НАЖМИ ENTER')
    cls()
    print('Ты, конечно, можешь прямо сейчас пойти и крушить всех направо и налево, но это вряд ли.\nВедь у тебя нет выбора, кроме как читать мои монологи и делать то, что я тебе прикажу :)\nНапример:\n')
    input('ДЛЯ ПРОДОЛЖЕНИЯ НАЖМИ ENTER')
    print('Ладно. Давай уже купим что-нибудь...\n')
    input('НАЖМИ ENTER ЧТОБЫ НАКОНЕЦ УЙТИ')
    start_new = True # По игре будет разбросаны всякие проверки на эту переменную. Это нужно исключительно в самом начале игры

# Основное меню
def menu():
    print(Back.BLACK, Fore.WHITE)
    cls()
    if start_new == True:
        print("Если возникнут вопросы, пиши в меню: 6\n")
    print(Back.GREEN, Fore.BLACK)
    print('=========OFFLINE RPG========')
    print(Back.CYAN, '    ПЕРСОНАЖ', Person.name)
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
        print('Уровень:', Person.level)
        print('Монет:', Person.coins)
        print('Кристаллов: ', Person.crystals)
        print('--------------------------')
        print('    Характеристика оружия:\n')
        print('Название:', Person.Weapon.name)
        print('Уровень:', Person.Weapon.level_w)
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
        print('Монет:', Person.coins)
        print('Кристаллов: ', Person.crystals)
        print('Зелье силы:', Person.potion_pow)
        print('Зелье здоровья:', Person.potion_heal)
        if Person.special == 'Маг':
            print('Зелье маны:', Person.potion_mana)
        print('Сундуков:',Person.pack_chest)
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
                rand_open_chest = rdm.randint(0,5)

                # Открытие сундука
                for i in range(5):
                    cls()
                    t = "."
                    print("\nОткрывается сундук", t * i, sep='')
                    slp(0.5)

                if rand_open_chest <= 3:
                    print(Back.WHITE, Fore.BLACK)
                    print("\nВ сундуке пусто...")
                    slp(3.5)
                elif rand_open_chest == 4:
                    rand_coins_amount = rdm.randint(1,4)
                    print(Back.GREEN, Fore.BLACK)
                    print("\nВ сундуке найдено",rand_coins_amount, "монет!")
                    Person.coins += rand_coins_amount
                    Person.Stats.coins_up += rand_coins_amount
                    slp(3.5)
                elif rand_open_chest == 5:
                    print(Back.GREEN, Fore.BLACK)
                    rand_potion = rdm.randint(0,2)
                    if rand_potion == 0:
                        rand_potion = "Силы"
                        Person.potion_pow += 1
                    elif rand_potion == 1:
                        rand_potion = "Здоровья"
                        Person.potion_heal += 1
                    elif rand_potion == 2:
                        if Person.special != "Маг":
                            rand_potion = "Здоровья"
                            Person.potion_heal += 1
                        else:
                            rand_potion = "Маны"
                            Person.potion_mana += 1

                    print("\nВ сундуке найдено зелье", rand_potion)
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

    elif choose == '2':
        go_dunge()

    elif choose == '3':
        market()

    elif choose == '4':
        cls()
        print("\nАрена Закрыта.")
        slp(3)
        menu()

    elif choose == '5':
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

    elif choose == '6':
        cls()
        print(Back.CYAN, Fore.BLACK)
        print("Репозиторий игры (открытый код): https://github.com/Mifman/Offline-RPG")
        print("Руководства и обновления: https://github.com/Mifman/Offline-RPG/discussions")
        print("Разработчик: Mifman")
        print("Контакт: https://vk.com/mifman")
        input("\nНажмите ENTER для выхода в МЕНЮ")
        menu()


    elif choose == '7':
        m_write_pack()
        m_write_save()

    else:
        print(Back.RED, Fore.BLACK)
        print("\nВведите коректные данные!")
        slp(2.3)
        menu()

# Рынок
def market():
    cls()
    if start_new == True:
        print(Back.WHITE, Fore.BLACK)
        print('Это рынок. Здесь ты можешь приобрести необходимые тебе вещи.')
        slp(4)
        print('В рынке в основном можно купить лишь те вещи, которые ты сможешь поместить в инвентарь, а именно:\n1. Зелья\n2. Сундуки')
        input('\nДля продолжения, нажми ENTER')
        slp(1.7)
        print('\nА вот, собственно, и рынок:')
        print(Back.BLACK,Fore.WHITE)
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
    print(Back.GREEN, Fore.BLACK,'============================')
    print(Back.MAGENTA, Fore.WHITE)
    print('1.',Market.stall_0,'за',Market.price_0,'монет\n')
    print('2.',Market.stall_1,'за',Market.price_1,'монет\n')
    print('3.',Market.stall_2,'за',Market.price_2,'монет\n')
    print('4.',Market.stall_3,'за',Market.price_3,'монет\n')
    print('5.',Market.stall_4,'за',Market.price_4,'монет\n')
    print(Back.GREEN, Fore.BLACK, '============================')



    # Работа рынка
    ####################
    def m_buy(): # l_market = ["Зелье Силы", "Зелье Здоровья", "Зелье маны", "Сундук", "Кристалл"]
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
                print(Person.special,'не может покупать зелье маны!')
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
                print('Для покупки не хватает',(Market.price_0 - Person.coins),'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

        else:
            if Person.coins >= Market.price_0:
                x = Market.price_0 # Временная переменная для проверок
                Person.coins -= x
                m_buy()
            else:
                print(Back.RED,Fore.BLACK,'\n\nДля покупки не хватает',(Market.price_0 - Person.coins),'монет!')
                print(Back.BLACK,Fore.WHITE)
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
                print('Для покупки не хватает',(Market.price_1 - Person.coins),'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

        else:
            if Person.coins >= Market.price_1:
                x = Market.price_1 # Временная переменная для проверок
                Person.coins -= x
                m_buy()
            else:
                print(Back.RED,Fore.BLACK,'\n\nДля покупки не хватает',(Market.price_1 - Person.coins),'монет!')
                print(Back.BLACK,Fore.WHITE)
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
                print('Для покупки не хватает',(Market.price_2 - Person.coins),'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

        else:
            if Person.coins >= Market.price_2:
                x = Market.price_2 # Временная переменная для проверок
                Person.coins -= x
                m_buy()
            else:
                print(Back.RED,Fore.BLACK,'\n\nДля покупки не хватает',(Market.price_2 - Person.coins),'монет!')
                print(Back.BLACK,Fore.WHITE)
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
                print('Для покупки не хватает',(Market.price_3 - Person.coins),'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

        else:
            if Person.coins >= Market.price_3:
                x = Market.price_3 # Временная переменная для проверок
                Person.coins -= x
                m_buy()
            else:
                print(Back.RED,Fore.BLACK,'\n\nДля покупки не хватает',(Market.price_3 - Person.coins),'монет!')
                print(Back.BLACK,Fore.WHITE)
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
                print('Для покупки не хватает',(Market.price_4 - Person.coins),'монет!')
                print(Back.BLACK, Fore.WHITE)
                slp(3.2)
                market()

        else:
            if Person.coins >= Market.price_4:
                x = Market.price_4 # Временная переменная для проверок
                Person.coins -= x
                m_buy()
            else:
                print(Back.RED,Fore.BLACK,'\n\nДля покупки не хватает',(Market.price_4 - Person.coins),'монет!')
                print(Back.BLACK,Fore.WHITE)
                slp(3.2)
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

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

# Орк (1-6)
def ork():
    Enemy.name = "Орк"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 4)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 2)
    Enemy.loot = rdm.randint(0, 1)

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

# Паук (2-6)
def spider():
    Enemy.name = "Паук"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 2)
    Enemy.loot = 0

# Кикимора (1-6)
def kikimora():
    Enemy.name = "Кикимора"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 6)
    Enemy.loot = rdm.randint(0, 2)

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

# Энт (1-6, кроме 2,4,5)
def ent():
    Enemy.name = "Энт"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.loot = rdm.randint(0, 1)

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

# Кентавр (1-6, кроме 2,4,5)
def kentavr():
    Enemy.name = "Кентавр"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 1)

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

# Элементаль (2-6)
def elemental():
    Enemy.name = "Элементаль"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 6)
    Enemy.loot = rdm.randint(0, 3)

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

# Тролль (1-6)
def troll():
    Enemy.name = "Тролль"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 3)

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

# Циклоп (3-6)
def cyklop():
    Enemy.name = "Циклоп"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 5)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 2)
    Enemy.loot = rdm.randint(0, 2)

# Демон (4-6)
def demon():
    Enemy.name = "Демон"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 11)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 4)
    Enemy.loot = rdm.randint(0, 2)

# Тэнгу (человек-ворон) (1-6, кроме 2,4,5)
def tengu():
    Enemy.name = "Тэнгу"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.loot = rdm.randint(0, 3)

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

# Горгона (2-6)
def gorgona():
    Enemy.name = "Горгона"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 4)
    Enemy.loot = rdm.randint(0, 1)

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

# Скелет (2,4,5)
def skelet():
    Enemy.name = "Скелет"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 1)

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

# Оборотень (1-6, кроме 4,5)
def oboroten():
    Enemy.name = "Оборотень"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 4)
    Enemy.loot = rdm.randint(0, 3)

# Лич (4,5)
def lich():
    Enemy.name = "Лич"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 11)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 6)
    Enemy.loot = rdm.randint(0, 4)

# Зомби (2,4,5)
def zombi():
    Enemy.name = "Зомби"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)

    Enemy.stamina = Enemy.stamina_default
    Enemy.hp = Enemy.hp_default

    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 1)

# Персонаж (другой "игрок") (1-6)
name_list = ["Progger", "dAlEk456", "Footman", "KoLo40k", "Киргиз", "СвяТой_ТапоК",
             "DeMoN", "Lemon4ik", "MirrorX", "4EJIoВek", "Joker", "Шалтай", "NoName",
             "Chilly", "FRENK", "Фант0м", "GONZO", "ШапоКJLЯC", "Succubus", "СКАЛА",
             "dazz", "ВАШ Доктор", "Тень", "MC", "ZOrg", "Агент007", "Лб_Чипс", "Сухарик",
             "КR0ш", "ArTemK", "Vlad1337", "Kefir", "Лёха", "Сергей", "Рэйзор БезУмНыЙ",
             "КрипоНуб", "Who Touch My Spagetti?"]
def player():
    Enemy.name = "Персонаж " + rdm.choice(name_list)
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.hp = 4 + Enemy.level + rdm.randint(3, 9)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 3)
    Enemy.stamina = Enemy.stamina_default
    Enemy.loot = rdm.randint(1, 3)

##########################
### ПЕРЕМЕННЫЕ
# Виды лута
l_list = ["Монет", "Зелий Силы", "Зелий Здоровья",
          "Зелий Маны", "Сундук(-а)", "Кристалл(-ов)"] # Лист со всеми видами лутов (вставляется в конце предложения)
l_name = None # Название лута
l_amount = 0

##########################
# Получение лута
###########################

def get_loot(l_name, l_list,l_amount):
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

        if l_name == l_list[0]: # coins
            Person.coins += l_amount
            Person.Stats.coins_up += l_amount

        elif l_name == l_list[1]: # pow
            Person.potion_pow += l_amount

        elif l_name == l_list[2]: # heal
            Person.potion_heal += l_amount

        elif l_name == l_list[3]: # mana
            if Person.special == "Маг":
                Person.potion_mana += l_amount
            else:
                print(Person.special, 'не может брать зелье маны!')

        elif l_name == l_list[4]: # chest
            Person.pack_chest += l_amount

        elif l_name == l_list[5]: # crystal
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
slot_fight = [] # Список выбора игрока
slot_fight_en = [] # Список выбора врага
def stats(): # Для простоты

    slot_fight = [] # Сброс
    slot_fight_en = [] # Сброс
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

    print(Back.GREEN,Fore.BLACK,"ИГРОК:\n")
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

# Для ИИ (предполагаемые статы здоровья)
t_hp = Person.hp # Противника
t_hp_self = Enemy.hp # Свои

def reset_ai():
    # Веса для ИИ
    v1 = 0  # Атака
    v2 = 0  # Защита
    v3 = 0  # Отдых

def AI(v1,v2,v3):
    # Проверки для расределения весов (хп у себя и врага)
    if t_hp_self < (Enemy.hp_default / 2):
        v2 += 1
    if t_hp_self < (Enemy.hp_default / 4):
        v2 += 2

    if t_hp < (Person.hp_default / 2):
        v1 += 1
    if t_hp < (Person.hp_default / 4):
        v1 += 2

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

def fight(v1,v2,v3):
    global slot_fight
    global slot_fight_en

    use_mana1 = False # Маг использовал увеличение шанса на кри ложь
    use_mana2 = False # Маг использовал увеличение здоровья ложь

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

        # Ограничение на макс. кол-во выносливости
        if Person.stamina > Person.stamina_default:
            Person.stamina = Person.stamina_default

        Enemy.hp = round(Enemy.hp, 3)
        Person.hp = round(Person.hp, 3)
        Enemy.stamina = round(Enemy.stamina, 3)
        Person.stamina = round(Person.stamina, 3)

        # Если враг повержен
        if Enemy.hp <= 0 and Person.hp > 0:
            slp(2)
            print("\n")
            print(Back.GREEN, Fore.BLACK)
            print(Enemy.name, "повержен!")
            slp(2.3)
            if Enemy.loot > 0:
                get_loot(l_name, l_list,l_amount)
            break

        # Если повержен персонаж игрока
        elif Person.hp <= 0:
            slp(2)
            print("\n")
            print(Back.RED, Fore.BLACK)
            print(Person.name, "потерял сознание...")
            slp(4)
            cls()
            print(Back.WHITE, Fore.BLACK)
            print("Внезапно, к вам прилетает Ангел с небес, берёт вас на руки и отводит через всю долину к вашим покоям...\n"
                  "Вы просыпаетесь без единого пореза на руке в своей постели.\n"
                  "К сожалению, все утерянные или потраченные вещи так и не появились, но вы живы, и это главное.")
            input("\nНажмите ENTER чтобы встать")
            break

        # Выбирает игрок
        c = 1 # Переменная для цикла while
        while c != 3:
            stats()
            print("\n",c, " Слот", sep='')
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
                        print(Back.WHITE,Fore.BLACK)
                        print("\nВЫБОР ЗЕЛИЙ:\n"
                              "1. Зелье Силы (", Person.potion_pow, ")\n"
                              "2. Зелье Здоровья (",Person.potion_heal,")\n"
                              "ENTER - выход из меню", sep='')
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
                            print(Back.RED,Fore.BLACK)
                            print("Не хватает маны!")
                            slp(3)
                    elif use_mana == "2":
                        if Person.mana >= 13:
                            print(Back.GREEN, Fore.BLACK)
                            Person.mana -= 13
                            use_mana1 = True
                            print("Увеличено здоровье на",  Person.hp_default / 4)
                            Person.hp += Person.hp_default / 4
                            slp(3)
                        else:
                            print(Back.RED,Fore.BLACK)
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
        AI(v1,v2,v3)
        #########################

        # Выбор для 2 слота
        #########################

        # Переделка предполагаемого события для корректировки
        if slot_fight_en[0] == "Атака":
            t_hp = Person.hp - Enemy.damage # предполагаемое кол-во здоровья противника
        elif slot_fight_en[0] == "Защита":
            if Enemy.level < Person.level:
                t_hp_self = Enemy.hp - (Person.Weapon.power * 0.25) # Бот будет предполагать, что его защита провалилась
            elif Enemy.level >= Person.level:
                t_hp_self = Enemy.hp - (Person.Weapon.power * 0.1)
        elif slot_fight_en[0] == "Отдых":
            v3 -= 1

        AI(v1,v2,v3)
        #########################
        # После всех выборов
        for z in range(2):
            if use_mana1 == True:
                rand_hit = rdm.randint(0,1)
                use_mana1 = False
            else:
                rand_hit = rdm.randint(0,3)

            rand_hit_en = rdm.randint(0,3)
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
                    Enemy.hp -= round(rand_hit * 0.2, 3)
                    Person.hp -= round(rand_hit_en * 0.1, 3)
                    print("\nВы атаковали на", round(rand_hit * 0.2, 3), "урона")
                    slp(0.7)
                    print("По вам прошло", round(rand_hit_en * 0.1, 3) , "урона")
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
                    Enemy.hp -= round(rand_hit * 0.2, 3)
                    Person.hp -= round(rand_hit_en * 0.2, 3)
                    print("\nВы атаковали на", round(rand_hit * 0.2, 3), "урона")
                    slp(0.7)
                    print("По вам прошло", round(rand_hit_en * 0.2, 3), "урона")
                    slp(1)
                    input("\nENTER чтобы продолжить")

            # Если атака и защита (атакующий: персонаж игрока)
            elif slot_fight[z] == "Атака" and slot_fight_en[z] == "Защита":
                Person.stamina -= 0.2

                rand_protect = rdm.randint(0,3)
                rand_damage_back = rdm.randint(0,1)
                # Возврат урона
                if rand_damage_back == 0:
                    Person.hp -= round(rand_hit * 0.05, 3)
                    print(Back.RED, Fore.BLACK, "\nВы получили урон (-",round(rand_hit * 0.05, 3),")", sep='')
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
                        print(Back.GREEN, Fore.BLACK, "Удалось пробить защиту и атаковать на", round(rand_hit * 0.05, 3))
                        slp(0.9)
                        input("\nENTER чтобы продолжить")

                else:
                    print("\nНе удалось пробить защиту!")
                    slp(3)
                    input("\nENTER чтобы продолжить")

            # Если атака и защита (атакующий: враг)
            elif slot_fight[z] == "Защита" and slot_fight_en[z] == "Атака":
                Enemy.stamina -= 0.2

                rand_protect = rdm.randint(0,3)
                rand_damage_back = rdm.randint(0,1)
                # Возврат урона
                if rand_damage_back == 0:
                    Enemy.hp -= round(rand_hit_en * 0.05, 3)
                    print(Back.RED, Fore.BLACK, "\nВраг получил урон (-",round(rand_hit_en * 0.05, 3),")", sep='')
                    slp(0.7)
                    input("\nENTER чтобы продолжить")

                if rand_protect == 0:
                    if Person.level > Enemy.level:
                        # Проверка на проход удара через защиту
                        Person.hp -= round(rand_hit_en * 0.1, 3)
                        print(Back.GREEN, Fore.BLACK, "Врагу удалось пробить защиту и атаковать на", round(rand_hit_en * 0.1, 3))
                        slp(0.9)
                        input("\nENTER чтобы продолжить")
                    else:
                        Enemy.hp -= round(rand_hit_en * 0.05, 3)
                        print(Back.GREEN, Fore.BLACK, "Врагу удалось пробить защиту и атаковать на", round(rand_hit_en * 0.05, 3))
                        slp(0.9)
                        input("\nENTER чтобы продолжить")

                else:
                    print("\nНе удалось пробить защиту!")
                    slp(3)
                    input("\nENTER чтобы продолжить")

            # Если защита и защита
            if slot_fight[z] == "Защита" and slot_fight_en[z] == "Защита":
                print("\nВы оба решили защититься")
                slp(1)
                input("\nENTER чтобы продолжить")

            # Если пить зелье и атака
            elif slot_fight[z] == "Пить зелье" and slot_fight_en[z] == "Атака":
                Enemy.stamina -= 2
                print("\nВаше зелье было разбито!")
                slp(1)
                print("Удалось частично уклониться от удара (-", round(rand_hit_en / 2, 3),")")
                slp(3)
                Person.hp -= round(rand_hit_en / 2, 3)
                input("\nENTER чтобы продолжить")

            # Если пить зелье и (защита или отдых)
            elif slot_fight[z] == "Пить зелье" and (slot_fight_en[z] == "Защита" or slot_fight_en[z] == "Отдых"):
                # Для персонажа игрока
                if pot_in == "1":
                    Person.potion_pow -= 1
                    Person.Weapon.power += round(Person.Weapon.power_default * 0.3, 3)
                    print(Back.GREEN, Fore.BLACK)
                    print("\nИспользовано Зелье Силы! (+", round(Person.Weapon.power_default * 0.3, 3), " урона)", sep='')
                    slp(3.3)
                    input("\nENTER чтобы продолжить")
                    pot = True

                elif pot_in == "2":
                    Person.potion_heal -= 1
                    Person.hp += round(Person.hp_default * 0.3, 3)
                    print(Back.GREEN, Fore.BLACK)
                    print("\nИспользовано Зелье Здоровья! (+", round(Person.hp_default * 0.3, 3), " ХП)", sep='')
                    slp(3.3)
                    input("\nENTER чтобы продолжить")
                    pot = True

                elif pot_in == "3":
                    Person.potion_mana -= 1
                    Person.mana += round(Person.mana_default * 0.3, 3)
                    print(Back.GREEN, Fore.BLACK)
                    print("\nИспользовано Зелье Маны! (+", round(Person.mana_default * 0.3, 3), " маны)", sep='')
                    slp(3.3)
                    input("\nENTER чтобы продолжить")
                    pot = True

                # Для врага
                if slot_fight_en[z] == "Защита":
                    print("\n",Enemy.name, "решил защититься")
                    slp(4)

                elif slot_fight_en[z] == "Отдых":
                    Enemy.stamina += round(Enemy.stamina_default, 3)
                    print("\n", Enemy.name, "решил восстановить выносливость")
                    slp(4)

            # Если отдых и (защита или отдых)
            elif slot_fight[z] == "Отдых" and (slot_fight_en[z] == "Защита" or slot_fight_en[z] == "Отдых"):
                # Для персонажа игрока
                Person.stamina += round(Person.stamina_default * 0.4)
                print("\nВы удачно восстановили", round(Person.stamina_default * 0.4), "выносливости.")
                slp(2.8)
                input("\nENTER чтобы продолжить")

                # Для врага
                if slot_fight_en[z] == "Защита":
                    print("\n", Enemy.name, "решил защититься")
                    slp(4)

                elif slot_fight_en[z] == "Отдых":
                    Enemy.stamina += round(Enemy.stamina_default, 3)
                    print("\n", Enemy.name, "решил восстановить выносливость")
                    slp(4)

            # Если отдых и атака
            elif slot_fight[z] == "Отдых" and slot_fight_en[z] == "Атака":
                Person.stamina += round(Person.stamina_default * 0.2, 3)
                print("\nВы восстановили", round(Person.stamina_default * 0.2, 3), "выносливости,\n"
                                                                    "Но", Enemy.name, "атаковал вас!")
                slp(3)
                print("-",rand_hit_en, sep='')
                input("\nENTER чтобы продолжить")
                Person.hp -= rand_hit_en

            # Если атака и отдых
            elif slot_fight[z] == "Атака" and slot_fight_en[z] == "Отдых":
                Enemy.stamina += round(Enemy.stamina_default * 0.2, 3)
                print("\nВраг восстановил выносливость,\n"
                                                        "Но", Person.name, "атаковал!")
                slp(3)
                input("\nENTER чтобы продолжить")
                Enemy.hp -= rand_hit

            # Если защита и отдых
            elif slot_fight[z] == "Защита" and slot_fight_en[z] == "Отдых":
                print(Person.name,"Бесполезно защитился")
                slp(2)
                input("\nENTER чтобы продолжить")

                Enemy.stamina += round(Enemy.stamina_default, 3)
                print("\n", Enemy.name, "решил восстановить выносливость")
                slp(3)



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
        for i in range(10):
            print("#", end='')
            slp(0.6)
        slp(1)
        # Встречи
        rand_event = rdm.randint(0,3)
        if rand_event == 0 or rand_event == 1:
            slot_fight = []
            slot_fight_en = []
            reset_ai()
            fight(v1,v2,v3)
            d.Dunge.level += 1

        elif rand_event == 2:
            slp(1.5)
            print(Back.GREEN,Fore.BLACK)
            print("\n", Person.name, "нашёл сундук! (+1 сундук в инвентарь)")
            Person.pack_chest += 1
            d.Dunge.level += 1
            slp(4)
        elif rand_event == 3:
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

    slp(3)
    print(Back.GREEN, Fore.BLACK)
    print("\nВам удалось пройти дандж ", d.Dunge.name,"!", sep='')
    slp(2.5)
    # Начисление XP
    Person.xp += round(d.Dunge.xp, 3)
    print("**Вы получили", round(d.Dunge.xp, 3), "опыта**")
    slp(3.5)
    if Person.xp >= Person.multiplier:
        Person.level += 1
        Person.xp -= Person.multiplier
        print("")
        print(Person.name, " получил новый уровень! (",Person.level,")", sep='')

    if Person.xp >= Person.Weapon.multiplier:
        Person.Weapon.level_w += 1
        print("")
        print("Оружие ", Person.name, " получило новый уровень! (", Person.Weapon.level_w, ")", sep='')

    m_write_save()
    m_write_pack()
    input("Нажмите ENTER для продолжения")
    menu()


# Выбор данджа
def go_dunge():
    if start_new:
        cls()
        print(Back.WHITE,Fore.BLACK,'\nЧто ж, мы дошли до самого интересного - до походов в данджи...')
        input('\nНажми ENTER для продолжения')
        print('\nЗдесь, по сути, происходит набив опыта и прочих плюшек. На данджах основана вся игра.')
        slp(3)
        input('\nНажми ENTER для продолжения')
        print(Fore.WHITE, Back.BLACK)
        slp(1.5)
        cls()
        print(Back.WHITE,Fore.BLACK,'\nКак играть?')
        print('Игра не замысловата. Выбираешь вид данджа (открывается по мере роста уровня игрока),\n Сражаешься с врагами и другими игроками (они не совсем настоящие), и открываешь сундуки.\nОпыт за прохождение данджа тоже имеется.')
        input('\nНажми ENTER для продолжения')
        cls()
        print(Fore.WHITE, Back.BLACK)
        slp(1.5)
        print('Что ж, теперь ты полноценный игрок в OFFLINE RPG!')
        input('\nНажми ENTER для выбора данджей')
    # Недоделал
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

    if Person.can_dunge >= 1: # См. класс Person
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
        slp(0.5)
        print(Back.WHITE, Fore.BLACK) # Белый фон, чёрный шрифт (фон битв)
        print("\nВаш выбор: Лес")
        Person.current_dunge = "Лес"

    elif choose == "1":
        if Person.level < 10:
            print("\nВы не достигли 10 уровня!")
            slp(3)
            cls()
            go_dunge()
        else:
            print(Back.WHITE, Fore.BLACK)  # Белый фон, чёрный шрифт (фон битв)
            print("\nВаш выбор: Подземелье")
            Person.current_dunge = "Подземелье"

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

    elif choose == "":
        menu()

    else:
        print("\nВыберите дандж из списка!")
        slp(3)
        cls()
        go_dunge()


    slp(2)
    сountdown = 5
    for i in range(5):
        cls()
        print(Back.WHITE, Fore.BLACK)
        print("Вход через ", end='')
        print(сountdown)
        slp(1)
        сountdown -= 1
        cls()

    dunge() # Вызов игры


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
save.seek(0) # Сброс на начало файла

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
Person.Weapon.multiplier = Person.Weapon.level_w * 9
save.seek(0)
###########
# Загрузка дней, проведённых за игрой
###########
for i in range(6):
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

save.close() # Закрытие сохранения

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

menu()