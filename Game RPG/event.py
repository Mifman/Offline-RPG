import random as rdm
from time import sleep as slp
import dunges as d # файл dunges.py
from RPG import Person as g # файл RPG.py

from colorama import init
from colorama import Fore, Back, Style
init()

# Класс врагов (Имя, его уровень, урон (зависит от уровня), жизней (также зависит от уровня), выносливость, критический урон, кол-во выпадающего лута)
class Enemy:
    name = "None"
    level = 0
    damage = 1 + level
    hp = 4 + level
    stamina = hp / 2
    critical = damage * 1.5
    loot = 0


##########################
# Виды врагов
# Порядок номеров миров (от лёгкого до самого сложного): 1-6

# Гоблин (1-5)
def goblin():
    Enemy.name = "Гоблин"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 2)
    Enemy.loot = rdm.randint(0, 1)

# Орк (1-6)
def ork():
    Enemy.name = "Орк"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 4)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 2)
    Enemy.loot = rdm.randint(0, 1)

# Паук (2-6)
def spider():
    Enemy.name = "Паук"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 2)
    Enemy.loot = 0

# Кикимора (1-6)
def kikimora():
    Enemy.name = "Кикимора"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 6)
    Enemy.loot = rdm.randint(0, 2)

# Энт (1-6, кроме 2,4,5)
def ent():
    Enemy.name = "Энт"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.loot = rdm.randint(0, 1)

# Кентавр (1-6, кроме 2,4,5)
def kentavr():
    Enemy.name = "Кентавр"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 1)

# Элементаль (2-6)
def elemental():
    Enemy.name = "Элементаль"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 6)
    Enemy.loot = rdm.randint(0, 3)

# Тролль (1-6)
def troll():
    Enemy.name = "Тролль"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 3)

# Циклоп (3-6)
def cyklop():
    Enemy.name = "Циклоп"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 5)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 2)
    Enemy.loot = rdm.randint(0, 2)

# Демон (4-6)
def demon():
    Enemy.name = "Демон"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 11)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 4)
    Enemy.loot = rdm.randint(0, 2)

# Тэнгу (человек-ворон) (1-6, кроме 2,4,5)
def tengu():
    Enemy.name = "Тэнгу"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.loot = rdm.randint(0, 3)

# Горгона (2-6)
def gorgona():
    Enemy.name = "Горгона"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 4)
    Enemy.loot = rdm.randint(0, 1)

# Скелет (2,4,5)
def skelet():
    Enemy.name = "Скелет"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 1)

# Оборотень (1-6, кроме 4,5)
def oboroten():
    Enemy.name = "Оборотень"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 4)
    Enemy.loot = rdm.randint(0, 3)

# Лич (4,5)
def lich():
    Enemy.name = "Лич"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 11)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 6)
    Enemy.loot = rdm.randint(0, 4)

# Зомби (2,4,5)
def zombi():
    Enemy.name = "Зомби"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 1)

# Персонаж (другой "игрок") (1-6)
name_list = ["Progger", "dAlEk456", "Footman", "KoLo40k", "Киргиз", "СвяТой_ТапоК", "DeMoN", "Lemon4ik", "MirrorX", "4EJIoВek", "Joker", "Шалтай", "NoName", "Chilly", "FRENK", "Фант0м", "GONZO", "ШапоКJLЯC", "Succubus", "СКАЛА", "dazz", "ВАШ Доктор", "Тень", "MC", "ZOrg", "Агент007", "Лб_Чипс", "Сухарик", "КR0ш", "ArTemK", "Vlad1337", "Kefir", "Лёха", "Сергей", "Рэйзор БезУмНыЙ", "КрипоНуб", "Who Touch My Spagetti?"]
def player():
    Enemy.name = "Персонаж: " + rdm.choice(name_list)
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.hp = 4 + Enemy.level + rdm.randint(3, 9)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 3)

##########################
### ПЕРЕМЕННЫЕ
# Виды лута
l_list = ["Монет", "Зелий Силы", "Зелий Здоровья", "Зелий Маны", "Сундук(-а)", "Кристалл(-ов)"] # Лист со всеми видами лутов (вставляется в конце предложения)
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

# Битва
def fight():
    print(Back.RED, Fore.BLACK)