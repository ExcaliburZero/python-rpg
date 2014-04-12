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
print ("Name:   " + name)
print ("Gender: " + gender)
print ("Skill:  " + skill)
print ("Gold:   " + str(gold))
print ("---------------")
print ("Health:     " + str(health))
print ("Strength:   " + str(strength))
print ("Defense:    " + str(defense))
print ("Magic:      " + str(magic))
print ("Resistance: " + str(resistance))
print ("Luck:       " + str(luck))
print ("---------------")

#Ask to print to html file
print_to_html_file = input("Would you like to print the character sheet to an html file? (Y/N)")

if print_to_html_file == "Y" or print_to_html_file == "y" or print_to_html_file == "Yes" or print_to_html_file == "Yes":
    #Write html file for character sheet
    html_file = open("Characters/" + str(name) + "(Character Sheet).html", "w")
    html_code = [""]
    html_code.append("<html><title>" + name + "'s Character Sheet</title><link rel=\"stylesheet\" href=\"Extras/style.css\" type=\"text/css\" /><body><div id=\"holder\">")
    html_code.append("<h2>" + name + "</h2>")
    html_code.append("<table class=\"data\">")
    html_code.append("<tr><td class=\"tdone\">Name: </td><td class=\"tdone\">" + name + "</td></tr>")
    html_code.append("<tr><td>Gender: </td><td>" + gender + "</td></tr>")
    html_code.append("<tr><td>Skill: </td><td>" + skill + "</td></tr>")
    html_code.append("<tr><td>Gold: </td><td>" + str(gold) + "</td></tr>")
    html_code.append("</table>")
    html_code.append("------------------------------</br>")
    html_code.append("<table class=\"data\">")
    html_code.append("<tr><td class=\"tdone\">Health: </td><td class=\"tdone\">" + str(health) + "</td></tr>")
    html_code.append("<tr><td>Strength: </td><td>" + str(strength) + "</td></tr>")
    html_code.append("<tr><td>Defense: </td><td>" + str(defense) + "</td></tr>")
    html_code.append("<tr><td>Magic: </td><td>" + str(magic) + "</td></tr>")
    html_code.append("<tr><td>Resistance: </td><td>" + str(resistance) + "</td></tr>")
    html_code.append("<tr><td>Luck: </td><td>" + str(luck) + "</td></tr>")
    html_code.append("</table>")
    html_code.append("</div></body></html>")
    html_file.write(str.join("\n", html_code))
    print(str.join("\n", html_code))
    html_file.close()
