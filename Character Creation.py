"""
Character Creation Program
"""

#Import JSON
import json

#Print intro
print("Here you will create the initial file for your character.\n-------")

#Gather Variables
name = input("Name:")

#Check that a name is entered
while name == "":
    print("No name entered. Make sure that you input a name.\n-------")
    name = input("Name:")

#Get gender
gender = input("Gender:")

#Check that gender is valid
while gender != "Male" and gender != "Female" and gender != "Ungendered":
    print("Invalid gender. Make sure the first letter is capitalized.\n-------")
    gender = input("Gender:")

#Get skill
print("-------\nYou can choose between these options:")
print("Swordplay\nBlacksmithing\nMagic\nAlchemy\nGambling\n-------")
skill = input("Which of those is your character most skilled at?")

#Check skill
while not (skill == "Swordplay" or skill == "Blacksmithing" or skill == "Magic" or skill == "Alchemy" or skill == "Gambling"):
    print ("-------\nInvalid input. Make sure that you capitalize the first letter.")
    print("-------\nYou can choose between these options:")
    print("Swordplay\nBlacksmithing\nMagic\nAlchemy\nGambling\n-------")
    skill = input("Which of those is your character most skilled at?")

#Set stats
health = "20"

#Set strength
if skill == "Swordplay":
    strength = "8"
else:
    strength = "5"

#Set defense
if skill == "Blacksmithing":
    defense = "8"
else:
    defense = "5"

#Set magic
if skill == "Magic":
    magic = "8"
else:
    magic = "5"

#Set resistance
if skill == "Alchemy":
    resistance = "8"
else:
    resistance = "5"

#Set luck
if skill == "Gambling":
    luck = "8"
else:
    luck = "5"

#Ready character file
character_file_name = "Characters/" + name + ".txt"

#Open and Write to character file
info = {"Name": name, "Gender": gender, "Skill": skill, "Gold": 500, "Health": health, "Strength": strength, "Defense": defense, "Magic": magic, "Resistance": resistance, "Luck": luck}
json.dump(info, open(character_file_name,'w'))

#Close character file
#character_file.close()
