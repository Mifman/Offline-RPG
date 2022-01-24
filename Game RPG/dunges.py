import random as rdm

# Основной класс (Имя, текущая часть данджа, максимальный порог данджа, кол-во уровня за прохождение, сложность данджа)
class Dunge:
    name = "None"
    level = 0
    level_max = 0
    xp = 0
    difficulty = 0

# Лес
def forest():
    Dunge.name = "Лес"
    Dunge.level_max = rdm.randint(1,3)
    Dunge.xp = rdm.randint(5,10) / 100
    Dunge.difficulty = rdm.randint(0,1)

# Подземелье
def dungeon():
    Dunge.name = "Подземелье"
    Dunge.level_max = rdm.randint(2,4)
    Dunge.xp = rdm.randint(8,18) / 100
    Dunge.difficulty = rdm.randint(2,3)

# Густой лес
def dense_forest():
    Dunge.name = "Густой лес"
    Dunge.level_max = rdm.randint(3,5)
    Dunge.xp = rdm.randint(10, 20) / 100
    Dunge.difficulty = rdm.randint(4,5)

# Заброшенный замок
def castle():
    Dunge.name = "Заброшенный замок"
    Dunge.level_max = rdm.randint(4,7)
    Dunge.xp = rdm.randint(18, 28) / 100
    Dunge.difficulty = rdm.randint(6,7)

# Супер-Подземелье
def super_dungeon():
    Dunge.name = "Супер-Подземелье"
    Dunge.level_max = rdm.randint(5,7)
    Dunge.xp = rdm.randint(25, 31) / 100
    Dunge.difficulty = rdm.randint(8,9)

# Изумрудный лес
def emerald_forest():
    Dunge.name = "Изумрудный лес"
    Dunge.level_max = rdm.randint(4,6)
    Dunge.xp = rdm.randint(30, 37) / 100
    Dunge.difficulty = 10