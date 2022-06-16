import random as rdm
import dunges as d # файл dunges.py

# Класс врагов (Имя, его уровень, урон (зависит от уровня), жизней (также зависит от уровня), критический урон, кол-во выпадающего лута)
class Enemy:
    name = "None"
    level = 0
    damage = 1 + level
    hp = 4 + level
    critical = damage * 1.5
    loot = 0

##########################
# Виды врагов

# Гоблин
def goblin():
    Enemy.name = "Гоблин"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 2)
    Enemy.loot = rdm.randint(0,1)

# Орк
def ork():
    Enemy.name = "Орк"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 4)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 2)
    Enemy.loot = rdm.randint(0, 1)

# Паук
def spider():
    Enemy.name = "Паук"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 2)
    Enemy.loot = 0

# Кикимора
def kikimora():
    Enemy.name = "Кикимора"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 6)
    Enemy.loot = rdm.randint(0, 2)

# Энт
def ent():
    Enemy.name = "Кикимора"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.loot = rdm.randint(0, 1)

# Кентавр
def kentavr():
    Enemy.name = "Кентавр"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 1)

# Элементаль
def elemental():
    Enemy.name = "Элементаль"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 6)
    Enemy.loot = rdm.randint(0, 3)

# Тролль
def troll():
    Enemy.name = "Тролль"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 3)

# Циклоп
def cyklop():
    Enemy.name = "Циклоп"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 5)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 2)
    Enemy.loot = rdm.randint(0, 2)

# Демон
def demon():
    Enemy.name = "Демон"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 11)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 4)
    Enemy.loot = rdm.randint(0, 2)

# Тэнгу (человек-ворон)
def tengu():
    Enemy.name = "Тэнгу"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.loot = rdm.randint(0, 3)

# Горгона
def gorgona():
    Enemy.name = "Горгона"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 4)
    Enemy.loot = rdm.randint(0, 1)

# Скелет
def skelet():
    Enemy.name = "Скелет"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 1)

# Оборотень
def oboroten():
    Enemy.name = "Оборотень"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 4)
    Enemy.loot = rdm.randint(0, 3)

# Лич
def lich():
    Enemy.name = "Лич"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 5)
    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 11)
    Enemy.damage = 1 + Enemy.level + rdm.randint(0, 6)
    Enemy.loot = rdm.randint(0, 4)

# Зомби
def zombi():
    Enemy.name = "Скелет"
    Enemy.level = d.Dunge.difficulty + rdm.randint(0, 3)
    Enemy.hp = 4 + Enemy.level + rdm.randint(0, 3)
    Enemy.loot = rdm.randint(0, 1)

##########################