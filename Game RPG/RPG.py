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
        level = 0
        power = 5 + level
        critical = power * 1.5

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
    hp = 20 # Кол-во жизней
    hp_multiplier = hp + (level + 1) # Столько будет hp После повышения уровня
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
    price_0 = rdm.randint(3,50)
    price_1 = rdm.randint(3,30)
    price_2 = rdm.randint(3,45)
    price_3 = rdm.randint(5,30)
    price_4 = rdm.randint(3,35)

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

    save.writelines(['1\n', '{0}\n'.format(Person.special), '0\n','{0}\n'.format(Person.level) ,'0\n', '500\n', '1\n', '0\n', Person.Weapon.name])
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
        print('Уровень:', Person.level)
        print('Монет:', Person.coins)
        print('Кристаллов: ', Person.crystals)
        print('--------------------------')
        print('    Характеристика оружия:\n')
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
        choose = input('НАЖМИТЕ ENTER ЧТОБЫ ВЫЙТИ В МЕНЮ')
        print(Back.RESET, Fore.RESET)
        menu()

    elif choose == '2':
        go_dunge()

    elif choose == '3':
        market()

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
        Market.price_0 = rdm.randint(3, 50)
        Market.price_1 = rdm.randint(3, 30)
        Market.price_2 = rdm.randint(3, 45)
        Market.price_3 = rdm.randint(5, 30)
        Market.price_4 = rdm.randint(3, 35)

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
    def potion_more():
        print(Back.RED, Fore.WHITE, '\nВы не можете хранить больше 9-ти зелий/сундуков/кристаллов одного вида!')
        slp(3)
        market()

    # Пересохраение основного "save.txt"
    def m_write_save():
        save = open('System/save.txt', 'w')
        save.write('1\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\{7}'.format(Person.special,Person.xp,Person.level,Person.Weapon.level,Person.coins,Person.crystals,Person.day,Person.Weapon.name))
        save.close()

    # Пересохраение инвентаря игрока (pack.txt)
    def m_write_pack():
        save_inventory = open('System/pack.txt', 'w')
        save_inventory.seek(0)
        save_inventory.write('{0}{1}{2}{3}'.format(Person.potion_pow, Person.potion_heal, Person.potion_mana, Person.pack_chest))
        save_inventory.close()

    def m_buy(): # l_market = ["Зелье Силы", "Зелье Здоровья", "Зелье маны", "Сундук", "Кристалл"]
        global x

        print(Back.BLACK, Fore.WHITE)
        cls()
        if market_choose == 'Зелье Силы':
            if Person.potion_pow >= 9:
                print('\n\nВы не можете хранить больше 9-ти зелий одного вида!')
                Person.coins += x
                x = 0
                input('\nНАЖМИТЕ ENTER, ЧТОБЫ ПРОДОЛЖИТЬ')
                market()
            else:
                print(Back.GREEN, Fore.BLACK, '\nПокупка совершена!')
                slp(0.8)
                Person.potion_pow += 1
                m_write_pack()
                m_write_save()
                menu()

        elif market_choose == 'Зелье Здоровья':
            if Person.potion_heal >= 9:
                print('\n\nВы не можете хранить больше 9-ти зелий одного вида!')
                Person.coins += x
                x = 0
                input('\nНАЖМИТЕ ENTER, ЧТОБЫ ПРОДОЛЖИТЬ')
                market()
            else:
                print(Back.GREEN, Fore.BLACK, '\nПокупка совершена!')
                slp(0.8)
                Person.potion_heal += 1
                m_write_pack()
                m_write_save()
                menu()

        elif market_choose == 'Зелье маны':
            if Person.special != "Маг":
                print(Back.BLACK, Fore.WHITE)
                print(Person.special,'не может покупать зелье маны!')
                slp(3)
                market()

            else:
                if Person.potion_mana >= 9:
                    print('\n\nВы не можете хранить больше 9-ти зелий одного вида!')
                    Person.coins += x
                    x = 0
                    input('\nНАЖМИТЕ ENTER, ЧТОБЫ ПРОДОЛЖИТЬ')
                    market()
                else:
                    print(Back.GREEN, Fore.BLACK, '\nПокупка совершена!')
                    slp(0.8)
                    Person.potion_mana += 1
                    m_write_pack()
                    m_write_save()
                    menu()

        elif market_choose == 'Сундук':
            if Person.pack_chest >= 9:
                print('\n\nВы не можете хранить больше 9-ти зелий одного вида!')
                Person.coins += x
                x = 0
                input('\nНАЖМИТЕ ENTER, ЧТОБЫ ПРОДОЛЖИТЬ')
                market()
            else:
                print(Back.GREEN, Fore.BLACK, '\nПокупка совершена!')
                slp(0.8)
                Person.pack_chest += 1
                m_write_pack()
                m_write_save()
                menu()

        elif market_choose == 'Кристалл':
            if Person.crystals >= 9:
                print('\n\nВы не можете хранить больше 9-ти зелий одного вида!')
                Person.coins += x
                x = 0
                input('\nНАЖМИТЕ ENTER, ЧТОБЫ ПРОДОЛЖИТЬ')
                market()
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




# Недоделал
# Сама игра

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


    for lm in range(d.Dunge.level_max): # Цикл, длина которого определяется длиной данджа
        print("\n\n")
        slp(1)
        print(Back.GREEN, Fore.BLACK)
        print("======================================")
        print(Back.MAGENTA, Fore.WHITE)
        print("Дандж: ", d.Dunge.name)
        print("Текущая часть данджа: ", d.Dunge.level)
        print("ХП: ", Person.hp)
        print("Зельей Силы: ", Person.potion_pow)
        print("Зельей Здоровья: ", Person.potion_heal)

        if Person.special == "Маг":
            print("Зельей Маны: ", Person.potion_mana)

        print(Back.GREEN, Fore.BLACK)
        print("======================================")
        slp(4)
        print(Back.WHITE, Fore.BLACK)
        print("\nАнализ:", end='')
        for i in range(10):
            print("#", end='')
            slp(0.6)
        slp(1)

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
        print('Что ж, теперь ты полноценный игрок в OFFLINE RPG.')
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

    # Выбор данджа
    choose = input("Ваш выбор: ==> ")

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
elif Person.special == 'Лучник\n':
    Person.special = 'Лучник'
elif Person.special == 'Маг\n':
    Person.special = 'Маг'
elif Person.special == 'Броневик\n':
    Person.special = 'Броневик'

###########
save.seek(0) # Сброс на начало файла

# Загрузка опыта, уровня, монет и кристаллов
###########
# xp
for i in range(2):
    save.readline()
Person.xp = int(save.readline())
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
Person.Weapon.level = int(save.readline())
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




