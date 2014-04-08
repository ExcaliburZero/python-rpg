"""
Forest Training
"""

#Imports
import sys
import json
from datetime import datetime
from random import *

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
    
#Get character name
name = input("Name:")

#Open character file and grab character info
character_file_name = "Characters/" + name + ".txt"
info = json.load(open(character_file_name))
health = int(info['Health'])
strength = int(info['Strength'])

#Increase health
info['Health'] = str(health + 1)

#Generate random number between 1 and 100
seed = randint(1,100)
print(str(seed))

#Possibility 1 ~ 0-33 ~ Increase Health 2
if seed <= 33:
    info['Health'] = str(health + 2)
    print("Health goes up two points!")

#Possibility 2 ~ 34-65  ~ Increase Health 1 and Strength 1
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
