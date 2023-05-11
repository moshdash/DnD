from api import API
from characterSheet import AbilityScores, Character
import random

# create an instance of the API class
api = API()

# get the available resources from the API
classes = api.getResources('classes')
races = api.getResources('races')


# randomly select a class from the available classes
class_select = api.getResources('classes', name=classes[random.randint(0, len(classes)-1)].lower())
class_name = class_select['name']

# randomly select a race from the availble races
race_select = api.getResources('races', name=races[random.randint(0, len(races)-1)].lower())
race_name = race_select['name']

abilityScores = AbilityScores.generateAbilityScores()

# create a character instance with the selected class
char = Character(name='John', race=race_name, level=1, classes=class_name, alignment='neutral')

# print the character's name, race, alignment, and level
#print(f"You rolled for your Ability Scores")
print(f"Name: {char.name}")
print(f"Race: {char.race}")
print(f"Alignment: {char.alignment}")
print(f"Level: {char.level}")

# print the character's class and hit points
print(f"Class: {char.classes}")
print(f"Hit Points: {char.getHitPoints()}")

# print the character's ability scores and modifiers
print(f"Strength: {char.ability_scores.strength} ({char.ability_scores.getStrengthModifier()})")
print(f"Dexterity: {char.ability_scores.dexterity} ({char.ability_scores.getDexterityModifier()})")
print(f"Constitution: {char.ability_scores.constitution} ({char.ability_scores.getConstitutionModifier()})")
print(f"Intelligence: {char.ability_scores.intelligence} ({char.ability_scores.getIntelligenceModifier()})")
print(f"Wisdom: {char.ability_scores.wisdom} ({char.ability_scores.getWisdomModifier()})")
print(f"Charisma: {char.ability_scores.charisma} ({char.ability_scores.getCharismaModifier()})")

# print the character's armor class and initiative
print(f"Armor Class: {char.getArmorClass()}")
print(f"Initiative: {char.getInitiative()}") 
