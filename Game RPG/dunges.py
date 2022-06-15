import random as rdm

# Основной класс Подземелья (Имя, текущая часть данджа, максимальный порог данджа, кол-во уровня за прохождение, сложность данджа)
class Dunge:
    name = "None"
    level = 0
    level_max = 0
    xp = 0
    difficulty = 0

# Класс врагов
class Enemy:
    name = "None"
    level = 0
    damage = 2 + level
    hp = 0
    critical = damage * 1.5

# Лес
def forest():
    Dunge.name = "Лес"
    Dunge.level_max = rdm.randint(3,5)
    Dunge.xp = rdm.randint(5,10) / 1.5
    Dunge.difficulty = rdm.randint(0,1)

# Подземелье
def dungeon():
    Dunge.name = "Подземелье"
    Dunge.level_max = rdm.randint(3,7)
    Dunge.xp = rdm.randint(8,18) / 1.5
    Dunge.difficulty = rdm.randint(2,3)

# Густой лес
def dense_forest():
    Dunge.name = "Густой лес"
    Dunge.level_max = rdm.randint(5,9)
    Dunge.xp = rdm.randint(10, 20) / 1.5
    Dunge.difficulty = rdm.randint(4,5)

# Заброшенный замок
def castle():
    Dunge.name = "Заброшенный замок"
    Dunge.level_max = rdm.randint(5,11)
    Dunge.xp = rdm.randint(18, 28) / 1.5
    Dunge.difficulty = rdm.randint(6,7)

# Супер-Подземелье
def super_dungeon():
    Dunge.name = "Супер-Подземелье"
    Dunge.level_max = rdm.randint(7,14)
    Dunge.xp = rdm.randint(25, 31) / 1.5
    Dunge.difficulty = rdm.randint(8,9)

# Изумрудный лес
def emerald_forest():
    Dunge.name = "Изумрудный лес"
    Dunge.level_max = rdm.randint(8,17)
    Dunge.xp = rdm.randint(30, 37) / 1.5
    Dunge.difficulty = 10