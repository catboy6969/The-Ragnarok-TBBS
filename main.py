import sys
import time
import os

def Launch():
    while True:
        try:
            os.system('cls||clear')
            print('Normal boot [1]')
            print('Other [2] (WIP)')
            print('Quit [3]')
            een = int(input(''))
            if een == 1:
                print('')
                preLoad()
            if een == 2:
                pass
            if een == 3:
                sys.exit()
        except ValueError:
            Launch()

def preLoad():
    while True:
        try:
            save = open('data.txt', 'r')
            save.close()
            print("The Ragnarok TBBS")
            cc()
        except (IndexError, FileNotFoundError):
            save = open("data.txt", "w+")
            save.write('0\n0\n0\n0\n0\n0')
            save.close()
            preLoad()

def pronounFetch():
    vars = saveRead()
    gender = vars[1]
    if gender == 1:
        pronoun = ('he', 'him', 'his')
    if gender == 2:
        pronoun = ('she', 'her', 'her')
    return pronoun

def raceFetch():
    save = saveRead()
    race = int(save[2])
    if race == 0:
        race_str = "Human"
    if race == 1:
        race_str = "Beast"
    if race == 2:
        race_str = "Goblin"
    if race == 3:
        race_str = "Kobold"
    if race == 4:
        race_str = "Ork"
    return race_str

##Variable Writer
def Writer(linen, varn):
    save = open("data.txt", "r")
    line = save.readlines()
    line[linen] = varn
    save = open("data.txt", "w+")
    save.writelines(line)
    save.close()
    return

def saveRead():
    save = open('data.txt', 'r')
    lines = save.readlines()
    name = lines[0]
    gender = int(lines[1])
    race = lines[2]
    save.close()
    return name, gender, race

##Character Creator
def cc():
    print("It is time to create your character")
    print("What is your name, Hero?")
    name_str = input("")
    name = name_str + '\n'
    varn = name
    linen = 0
    Writer(linen, varn)
    os.system('cls||clear')
    print(name_str, 'is the name of the Hero. You may save or destroy the land of Ragnarok as you choose.')
    time.sleep(2)
    os.system('cls||clear')
    print("Choose your gender")
    print("1:Male")
    print("2:Female")
    gender = int(input(""))
    if gender == 1:
        varn = '1\n'
    if gender == 2:
        varn = '2\n'
    linen = 1
    Writer(linen, varn)
    os.system('cls||clear')
    print("Choose your race.")
    print("1:Human")
    print("2:Beast Person")
    print("3:Goblin")
    print("4:Kobold")
    print("5:Ork")
    racer = int(input(""))
    race = 0
    if racer == 1:
        race = '0\n'
    if racer == 2:
        br()
    if racer == 3:
        race = '2\n'
    if racer == 4:
        race = '3\n'
    if racer == 5:
        race = '4\n'
    os.system('cls||clear')
    linen = 2
    varn = race
    Writer(linen, str(varn))
    race_str = raceFetch()
    print("So it is, that", name_str, "is a", race_str, end="")
    print('.')
    time.sleep(2)
    os.system('cls||clear')
    sys.exit()

##The beast Race Race Chooser
def br():
    pronoun = pronounFetch()
    print('As the Hero is a beast person,', pronoun[0], "will need to know what kind of Beast", pronoun[0], "is.")
    print('\nOPTION [1]')
    print('OPTION [2]')
    print('OPTION [3]')
    print('OPTION [4]')
    print('QUIT [5]')
    br_inp = int(input('')) ##TODO WORK HERE
    if br_inp == 1:
        pass
    if br_inp == 2:
        pass
    if br_inp == 3:
        pass
    if br_inp == 4:
        pass
    if br_inp == 5:
        sys.exit()

Launch()
