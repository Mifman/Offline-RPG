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

start_new = False # Изначально обучение отключено. Оно включается только в самом начале прохождения

# Быстрая очистка экрана
def cls():
    system('CLS')
    print(Fore.WHITE, Back.BLACK)

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
        power = 5
        critical = power * 1.5

    name = None
    special = None
    xp = 0 # Опыт
    level = 1 # Уровень
    multiplier = level * 12 # Множитель уровня (именно столько нужно опыта для достижения нового уровня)
    day = 0  # Дни, проведённые за игрой (игровые, вычисляются битвами)
    coins = 500
    crystals = 1
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




l_market = ["Зелье Силы", "Зелье Здоровья", "Зелье маны", "Сундук", "Кристаллы"]

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
    print('\nЧтобы его изменить, пройдите по пути:\n "Корневая папка/System/name.txt"\nИ прописывайте новое, оригинальное на ваш взгляд имя :)\n\nВНИМАНИЕ! Настоятельно не рекомендуем удалять файл name.txt\n')
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
        Market.price_0 = rdm.randint(3,30)
        Market.price_1 = rdm.randint(3,30)
        Market.price_2 = rdm.randint(3,30)
        Market.price_3 = rdm.randint(3,30)
        Market.price_4 = rdm.randint(3,30)

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
        print(Back.RED, Fore.WHITE, '\nВы не можете хранить больше 9-ти зелий/сундуков одного вида!')
        slp(3)
        market()

    # Пересохраение основного "save.txt"
    def m_write_save():
        save = open('System/save.txt', 'w')
        save.write('1\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}'.format(Person.special,Person.xp,Person.Weapon.level,Person.coins,Person.crystals,Person.day,Person.Weapon.name))
        save.close()

    # Пересохраение инвентаря игрока (pack.txt)
    def m_write_pack():
        save_inventory = open('System/pack.txt', 'w')
        save_inventory.seek(0)
        save_inventory.write('{0}{1}{2}{3}'.format(Person.potion_pow, Person.potion_heal, Person.potion_mana, Person.pack_chest))
        save_inventory.close()

    def m_buy(): # l_market = ["Зелье Силы", "Зелье Здоровья", "Зелье маны", "Сундук", "Кристаллы"]
        cls()
        if market_choose == 'Зелье Силы':
            print(Back.BLACK, Fore.WHITE)
            print(Back.GREEN, Fore.BLACK, '\nПокупка совершена!')
            slp(0.8)
            Person.potion_pow += 1
            m_write_pack()
            m_write_save()
            menu()

        elif market_choose == 'Зелье Здоровья':
            print(Back.BLACK, Fore.WHITE)
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
                print(Back.BLACK, Fore.WHITE)
                print(Back.GREEN, Fore.BLACK, '\nПокупка совершена!')
                slp(0.8)
                Person.potion_mana += 1
                m_write_pack()
                m_write_save()
                menu()

        elif market_choose == 'Сундук':
            print(Back.GREEN, Fore.BLACK, '\nПокупка совершена!')
            print(Back.BLACK, Fore.WHITE)
            slp(0.8)
            Person.pack_chest += 1
            m_write_pack()
            m_write_save()
            menu()

        elif market_choose == 'Кристаллы':
            print(Back.GREEN, Fore.BLACK, '\nПокупка совершена!')
            print(Back.BLACK,Fore.WHITE)
            slp(0.8)
            Person.crystals += 1
            m_write_save()
            menu()

    ####################


    # Недоделал
    # Варианты выбора
    market_choose = input('\nВаш выбор (exit/ENTER - выход из рынка): ==>')
    if market_choose == "exit" or market_choose == "":
        menu()
    elif market_choose == '1':
        market_choose = Market.stall_0
        if market_choose != 'Кристаллы':
            save_inventory = open('System/pack.txt', 'r')
            save_inventory.seek(0)

            if Person.coins >= Market.price_0:
                if int(save_inventory.read(1)) > 9:
                    save_inventory.close()
                    potion_more()
                else:
                    Person.coins -= Market.price_0
                    m_buy()
            else:
                print('Для покупки не хватает',(Market.price_0 - Person.coins),'монет!')

        else:
            if Person.coins >= Market.price_0:
                Person.coins -= Market.price_0
                m_buy()
            else:
                print('Для покупки не хватает',(Market.price_0 - Person.coins),'монет!')




# Недоделал
# Сама игра
def go_dunge():
    if start_new:
        cls()
        print('\nЧто ж, мы дошли до самого интересного - до походов в данджи...')
        input('\nНажми ENTER для продолжения')
        # Недоделал



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
for i in range(7):
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




