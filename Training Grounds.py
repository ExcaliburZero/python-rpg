"""
Training Grounds
"""

#Imports
import sys
import json
from datetime import datetime
from random import *

#Define function to Get Character Info
def get_character_info():
    #Get character name
    global name
    name = input("Name:")
    
    #Open character file and grab character info
    global character_file_name
    character_file_name = "Characters/" + name + ".txt"
    global info
    info = json.load(open(character_file_name))
    global gender
    global skill
    global gold
    global health
    global strength
    global defense
    global magic
    global resistance
    global luck
    name = str(info['Name'])
    gender = str(info['Gender'])
    skill = str(info['Skill'])
    gold = int(info['Gold'])
    health = int(info['Health'])
    strength = int(info['Strength'])
    defense = int(info['Defense'])
    magic = int(info['Magic'])
    resistance = int(info['Resistance'])
    luck = int(info['Luck'])

#Define function to modify stat
def stat_change(stat, mod):
    ifs = ""
    if not mod == 1:
        ifs = "s"
    stat_lowercase = stat.lower()
    info[str(stat)] = str(eval(stat_lowercase) + mod)
    print(stat + " goes up by " + str(mod) + " point" + ifs + "!")

#Set current time
now = datetime.now()

#Open time file for reading
time_file = open("Times/Training Grounds.txt", "r")

#Setting up time variables
last_time = int(time_file.read())
now_time = now.minute

#Print out last play time and current time
print("Last play was: " + str(last_time))
print("It is now: " + str(now.minute))

#Close time_file for reading
time_file.close()

#Test if five minutes have occured since last play
if now_time - last_time >= 3 or now_time - last_time < 0:
    print("Ready!")
else:
    #if less than five minutes have elapsed then gives message and ends program
    print("It has been " + str(now_time - last_time) + " minutes since you last played. Wait until it has been at least 3 minutes.")
    sys.exit()
    
get_character_info()

#Generate random number between 1 and 100
seed = randint(1,100)
print(str(seed))

#Possibility 1 ~ 0-11 ~ Increase Health 1
if seed <= 11:
    stat_change("Health", 1)
    
#Possibility 1 ~ 12-22 ~ Increase Strength 1
if seed <= 22 and seed > 11:
    stat_change("Strength", 1)
    
#Possibility 1 ~ 23-33 ~ Increase Defense 1
if seed <= 33 and seed > 22:
    stat_change("Defense", 1)
    
#Possibility 1 ~ 34-44 ~ Increase Magic 1
if seed <= 44 and seed > 33:
    stat_change("Magic", 1)
    
#Possibility 1 ~ 45-55 ~ Increase Resistance 1
if seed <= 55 and seed > 44:
    stat_change("Resistance", 1)
    
#Possibility 1 ~ 56-66 ~ Increase Luck 1
if seed <= 66 and seed > 55:
    stat_change("Luck", 1)
    
#Possibility 1 ~ 67-77 ~ Increase Gold 50
if seed <= 77 and seed > 66:
    info['Gold'] = str(gold + 50)
    print("You find 50 Gold!")
    
#Possibility 1 ~ 78-100 ~ Increase Gold 20
if seed <= 100 and seed > 77:
    info['Gold'] = str(gold + 20)
    print("You find 20 Gold!")

#Open time_file for writing
time_file = open("Times/Training Grounds.txt", "w")

#Update time
time_write = str(now.minute)
time_file.write(time_write)

#Write to character file
json.dump(info, open(character_file_name,'w'))

#Close Files
time_file.close()
