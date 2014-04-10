"""
Character Sheet
"""

#Imports
import json

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

get_character_info()

#Print character info
print ("---------------")
print ("Name:   " + str(name))
print ("Gender: " + str(gender))
print ("Skill:  " + str(skill))
print ("Gold:   " + str(gold))
print ("---------------")
print ("Health:     " + str(health))
print ("Strength:   " + str(strength))
print ("Defense:    " + str(defense))
print ("Magic:      " + str(magic))
print ("Resistance: " + str(resistance))
print ("Luck:       " + str(luck))
print ("---------------")
