import random as rdm
from time import sleep as slp
import dunges as d # файл dunges.py
from RPG import Person as g # файл RPG.py
from RPG import m_write_save as save # файл RPG.py
from RPG import m_write_pack as pack # файл RPG.py
from os import system

from colorama import init
from colorama import Fore, Back, Style
init()

# Технические переменные
# Веса для ИИ
v1 = 0  # Атака
v2 = 0  # Защита
v3 = 0  # Отдых

def cls():
    print(Fore.WHITE, Back.BLACK)
    system('CLS')

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
    Enemy.name = "Персонаж: " + rdm.choice(name_list)
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.hp = 4 + Enemy.level + rdm.randint(3, 9)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(1, 3)

##########################
### ПЕРЕМЕННЫЕ
# Виды лута
l_list = ["Монет", "Зелий Силы", "Зелий Здоровья",
          "Зелий Маны", "Сундук(-а)", "Кристалл(-ов)"] # Лист со всеми видами лутов (вставляется в конце предложения)
l_name = None # Название лута
l_amount = 0

def get_loot():
    if l_name == l_list[0]: # coins
        g.Person.coins += l_amount

    elif l_name == l_list[1]: # pow
        g.Person.potion_pow += l_amount

    elif l_name == l_list[2]: # heal
        g.Person.potion_heal += l_amount

    elif l_name == l_list[3]: # mana
        if g.Person.special == "Маг":
            g.Person.potion_mana += l_amount
        else:
            print(g.Person.special, 'не может брать зелье маны!')

    elif l_name == l_list[4]: # chest
        g.Person.pack_chest += l_amount

    elif l_name == l_list[5]: # crystal
        g.Person.crystals += l_amount

    print(Back.WHITE, Fore.BLACK)
    print("\n ", g.Person.name, " Получает ", l_amount, " ", l_name, "!", sep='')
    slp(3.3)
    save()
    pack()


##########################

##########################
# Получение лута
def set_loot():
    ######################
    ### Рандомайзер

    # Проценты выпадения предметов: Монеты - 40%, Зелья (один из видов) - 30% (по 10% на силу или ману и 20% на здоровье), Сундуки - 20%, Кристаллы - 10%
    rand_loot = rdm.randint(0,9)
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
    rand_amount = rdm.randint(0,1)
    if l_name == "Монет": # Чтобы побольше было
        l_amount = rdm.randint(1, 5)
    else:
        l_amount = rdm.randint(1, 2)

    ######################

# Выбор попавшегося врага
this_enemy = False # True, если данный враг может попасться в данном дандже
enemy_forest = ["Гоблин", "Орк", "Кикимора", "Энт", "Кентавр", "Тролль", "Тэнгу", "Оборотень", "Персонаж"]
enemy_dungeon = ["Гоблин", "Орк", "Кикимора", "Тролль", "Оборотень", "Персонаж", "Паук", "Элементаль", "Горгона", "Скелет", "Зомби"]
enemy_dense_forest = ["Гоблин", "Орк", "Кикимора", "Энт", "Кентавр", "Тролль", "Тэнгу", "Оборотень", "Персонаж", "Паук", "Элементаль", "Горгона", "Циклоп"]
enemy_castle = ["Гоблин", "Орк", "Кикимора", "Тролль", "Оборотень", "Персонаж", "Паук", "Элементаль", "Горгона", "Скелет", "Зомби", "Лич", "Демон"]
enemy_super_dungeon = ["Гоблин", "Орк", "Кикимора", "Тролль", "Оборотень", "Персонаж", "Паук", "Элементаль", "Горгона", "Скелет", "Зомби", "Лич", "Демон"]
enemy_emerald_forest = ["Гоблин", "Орк", "Кикимора", "Тролль", "Оборотень", "Персонаж", "Паук", "Элементаль", "Горгона", "Демон"]
#enemy_list = ["Гоблин", "Орк", "Паук", "Кикимора","Энт", "Кентавр", "Элементаль", "Тролль","Циклоп", "Демон", "Тэнгу", "Горгона", "Скелет","Оборотень", "Лич", "Зомби", "Персонаж"]
def enemy_choose():
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
    print("\n================")

    print(g.name, ":", sep='')
    print("Уровень:", g.level)
    print("ХП:", g.hp)
    print("Урон:", g.Weapon.power)
    print("Крит:", g.Weapon.critical)
    print("Выносливость:", g.stamina)
    print("Зелий Силы:", g.potion_pow)
    print("Зелий Здоровья:", g.potion_heal)
    if g.special == "Маг":
        print("Зелий Маны:", g.potion_mana)

# Для ИИ (предполагаемы статы здоровья)
t_hp = g.hp # Противника
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

    if t_hp < (g.hp_default / 2):
        v1 += 1
    if t_hp < (g.hp_default / 4):
        v1 += 2

    # slot_fight_en - слот для выбора врага
    slot_en = ["Атака", "Защита"]
    choose_slot_en = False  # Для цикла
    while choose_slot_en == False:
        if Enemy.stamina < (Enemy.stamina_default / 2):
            v3 += 2

        if v3 >= 3:
            choose_slot_en = True  # Бот однозначно выбрал отдых (а что же ещё блин!)

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
    if v1 > v2:
        slot_fight_en.append("Атака")

    elif v2 > v1:
        slot_fight_en.append("Защита")

    elif v2 == v1:
        rand_slot = rdm.choice(slot_en)  # Рандом выбора (50/50)
        slot_fight_en.append(rand_slot)
    elif v3 >= v2 and v3 >= v1:
        slot_fight_en.append("Отдых")

def fight():
    save()
    pack()
    print(Back.RED, Fore.BLACK)
    enemy_choose()
    slp(1)
    print("Обнаружен противник!")
    slp(3)

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

        in_choice = input("\nВаш выбор: ==>")

        # Атака
        if in_choice == "1":
            if g.stamina < 2:
                print(Back.RED, Fore.BLACK)
                print("\nНе хватает выносливости!")
                slp(2)

            else:
                slot_fight.append("Атака")
                slp(1)
                print("\nВаш выбор: Атака")
                slp(2)
                c += 1
        #############################

        # Защита
        #############################
        elif in_choice == "2":
            if g.stamina < 2:
                print(Back.RED, Fore.BLACK)
                print("\nНе хватает выносливости!")
                slp(2)

            slot_fight.append("Защита")
            slp(1)
            print("\nВаш выбор: Защита")
            slp(2)
            c += 1
        #############################

        # Пить зелье
        #############################
        elif in_choice == "3":
            if g.stamina < 1:
                print(Back.RED, Fore.BLACK)
                print("\nНе хватает выносливости!")
                slp(2)

            slot_fight.append("Пить зелье")
            slp(1)
            print("\nВаш выбор: Пить зелье")
            slp(1.9)
            c += 1
            # Блок Зелий
            ################################
            pot = False
            while pot == False:
                cls()
                print("\nВыбор зелий:\n"
                      "1. Зелье Силы (", g.potion_pow, ")\n"
                      "2. Зелье Здоровья (",g.potion_heal,")\n", sep='')
                if g.special == "Маг":
                    print("3. Зелье Маны (", g.potion_mana, ")", sep='')

                pot_in = input("\nВаш выбор: ==>")
                if pot_in == "1":
                    if g.potion_pow > 0:
                        g.potion_pow -= 1
                        g.Weapon.power += (g.Weapon.power_default * 0.3)
                        print(Back.GREEN, Fore.BLACK)
                        print("\nИспользовано Зелье Силы! (+",g.Weapon.power_default * 0.3," урона)", sep='')
                        slp(3.3)
                        pot = True

                    else:
                        print(Back.RED, Fore.BLACK)
                        print("\nУ вас нет Зелья Силы!")
                        slp(3)
                elif pot_in == "2":
                    if g.potion_heal > 0:
                        g.potion_heal -= 1
                        g.hp += (g.hp_default * 0.3)
                        print(Back.GREEN, Fore.BLACK)
                        print("\nИспользовано Зелье Здоровья! (+",g.hp_default * 0.3," ХП)", sep='')
                        slp(3.3)
                        pot = True

                    else:
                        print(Back.RED, Fore.BLACK)
                        print("\nУ вас нет Зелья Здоровья!")
                        slp(3)
                elif pot_in == "3":
                    if g.special != "Маг":
                        print(Back.RED, Fore.BLACK)
                        print("\nВведите корректные данные!")
                        slp(3)
                    else:
                        if g.potion_mana > 0:
                            g.potion_mana -= 1
                            g.mana += (g.mana_default * 0.3)
                            print(Back.GREEN, Fore.BLACK)
                            print("\nИспользовано Зелье Маны! (+", g.mana_default * 0.3, " маны)", sep='')
                            slp(3.3)
                            pot = True

                        else:
                            print(Back.RED, Fore.BLACK)
                            print("\nУ вас нет Зелья Маны!")
                            slp(3)

                else:
                    print(Back.RED, Fore.BLACK)
                    print("Введите корректные данные!")
                    slp(3)
            ################################

        #############################

        # Отдых
        #############################
        elif in_choice == "4":
            slot_fight.append("Отдых")
            slp(1)
            print("\nВаш выбор: Отдых")
            slp(2)
        #############################

    slp(1.5)
    print(Back.WHITE, Fore.BLACK)
    print("Ваш выбор:", slot_fight)
    slp(3)

    # Выбор врага (Мега ИИ)

    # Выбор для 1 слота
    #########################
    reset_ai()
    AI()
    #########################

    # Выбор для 2 слота
    #########################
    if slot_fight_en[0] == "Атака":
        t_hp = g.hp - Enemy.damage # предполагаемое кол-во здоровья противника
    elif slot_fight_en[0] == "Защита":
        if Enemy.level < g.level:
            t_hp_self = Enemy.hp - (g.Weapon.power * 0.25) # Бот будет предполагать, что его защита провалилась
        elif Enemy.level >= g.level:
            t_hp_self = Enemy.hp - (g.Weapon.power * 0.1)

    AI()
    #########################
    # Недоделал