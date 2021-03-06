"""
Forest Training
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

#Set current time
now = datetime.now()

#Open time file for reading
time_file = open("Times/Forest Training.txt", "r")

#Setting up time variables
last_time = int(time_file.read())
now_time = now.minute

#Print out last play time and current time
print("Last play was: " + str(last_time))
print("It is now: " + str(now.minute))

#Close time_file for reading
time_file.close()

#Test if five minutes have occured since last play
if now_time - last_time >= 5 or now_time - last_time < 0:
    print("Ready!")
else:
    #if less than five minutes have elapsed then gives message and ends program
    print("It has been " + str(now_time - last_time) + " minutes since you last played. Wait until it has been at least 5 minutes.")
    sys.exit()
    
get_character_info()

#Generate random number between 1 and 100
seed = randint(1,100)
print(str(seed))

#Possibility 1 ~ 0-33 ~ Increase Health 2
if seed <= 33:
    info['Health'] = str(health + 2)
    print("Health goes up two points!")

#Possibility 2 ~ 34-65 ~ Increase Health 1 and Strength 1
if seed > 33 and seed < 66:
    info['Health'] = str(health + 1)
    info['Strength'] = str(strength + 1)
    print("Health and Strength both go up one point!")

#Possibility 3 ~ 66-100 ~ Increase Strength 2
if seed >= 66:
    info['Strength'] = str(strength + 2)
    print("Strength goes up two points!")

#Open time_file for writing
time_file = open("Times/Forest Training.txt", "w")

#Update time
time_write = str(now.minute)
time_file.write(time_write)

#Write to character file
json.dump(info, open(character_file_name,'w'))

#Close Files
time_file.close()
