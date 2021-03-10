import sys
import time
import configparser
from configparser import NoOptionError, NoSectionError
print("The Ragnarok TBB Character Creator")
time.sleep(1)
print("Loading Complete")
print("Enter The Ragnarok?")
print("N/Y")
var0 = input("")
if var0 == "N":
    sys.exit()
if var0 == "Y":
    print("Welcome to The Ragnarok")
    print("Pick your worthless class")
    print("5:fighter")
    print("4:boxer")
    print("1:CatGirl")
    print("2:mage just in case you are a really shitty person you fucking degenerate")
    print("3:ranger")
    print("6:CatGirl but autistic")
    print("7:CatBoy")
    print("8:CatBoy but autistic")
    print("")
    strength = 0
    mag = 0
    char = 0
    agi = 0
varclass = int(input(""))
if varclass == 5:
    strength = 10
    mag = 3
    char = 3
    agi = 1
    print("You are a Fighter")
if varclass == 4:
    strength = 13
    mag = 0
    char = 2
    agi = 5
    print("you are a Boxer")
if varclass == 1:
    strength = 3
    mag = 3
    char = 10
    agi = 14
    print("you are a CatGirl")
if varclass == 2:
    strength = 0
    mag = 15
    char = 0
    agi = 0
    print("Whats wrong with you???")
if varclass == 3:
    strength = 4
    mag = 6
    char = 5
    agi = 12
    print("You are a Ranger! I love you.")
    print("Sowwy UwU")
if varclass == 6:
    strength = 7
    mag = 14
    char = 0
    agi = 14
    print("You are indeed, an autistic CatGirl.")
if varclass == 8:
    strength = 9
    mag = 14
    char = 0
    agi = 12
    print("You are indeed, an autistic CatBoy.")
if varclass == 7:
    strength = 5
    mag = 3
    char = 10
    agi = 12
    print("you are a CatBoy")
print("Your Strength is", strength)
print("Your Magical ability is", mag)
print("Your Charisma is", char)
print ("your agility is ", agi)
name = "no name"
if varclass == 2:
    print("What is your name")
    name = input()
if varclass != 2:
    print("what is your name hero?")
    name = input()
print("writing your data to a file!")
cb = open("playerdat.txt","w+")
cb.write(name/n)
cb.write("strength")
cb.write("mag")
cb.write("char")
cb.write("agi")
cb.close()
