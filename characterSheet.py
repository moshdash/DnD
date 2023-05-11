import random
import requests

from api import API

# Ability Scores Class
class AbilityScores:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        
    def getModifier(self, score):
        return (score - 10) // 2
        
    def getStrengthModifier(self):
        return self.getModifier(self.strength)
        
    def getDexterityModifier(self):
        return self.getModifier(self.dexterity)
        
    def getConstitutionModifier(self):
        return self.getModifier(self.constitution)
        
    def getIntelligenceModifier(self):
        return self.getModifier(self.intelligence)
        
    def getWisdomModifier(self):
        return self.getModifier(self.wisdom)
        
    def getCharismaModifier(self):
        return self.getModifier(self.charisma)
    
    def generateAbilityScores():
        scores = []
        for _ in range(6):
            rolls = [random.randint(1, 6) for _ in range(4)]
            scores.append(sum(sorted(rolls)[1:]))
        return scores

# Character Class
class Character:
    def __init__(self, name, race, level, classes, alignment, strength=None, dexterity=None, constitution=None, intelligence=None, wisdom=None, charisma=None):
        self.name = name
        self.race = race
        self.level = level
        self.classes = classes
        self.alignment = alignment
        if strength is not None and dexterity is not None and constitution is not None and intelligence is not None and wisdom is not None and charisma is not None:
            self.ability_scores = AbilityScores(strength, dexterity, constitution, intelligence, wisdom, charisma)
        else:
            ability_scores = AbilityScores.generateAbilityScores()
            self.ability_scores = AbilityScores(*ability_scores)
        self.class_details = self.getClassDetails(classes)


    def getClassDetails(self, class_name):
        api = API()
        classes = api.getResources('classes')
        if class_name not in classes:
            return f"{class_name} is not a valid class."
        else:
            class_url = f"{api.apiurl}classes/{class_name.lower()}"
            r = requests.get(class_url)
            data = r.json()
            return data
        
    def rollDice(self, numDice, diceSize):
        return sum([random.randint(1, diceSize) for i in range(numDice)])
    
    def getHitDie(self):
        hit_die = {
            'Barbarian': '12',
            'Bard': '8',
            'Cleric': '8',
            'Druid': '8',
            'Fighter': '10',
            'Monk': '8',
            'Paladin': '10',
            'Ranger': '10',
            'Rogue': '8',
            'Sorcerer': '6',
            'Warlock': '8',
            'Wizard': '6'
        }
        return hit_die.get(self.classes)
        
    def getHitPoints(self):
        return self.rollDice(self.level, int(self.getHitDie())) + (self.level * int(self.ability_scores.getConstitutionModifier()))
        
    def getArmorClass(self):
        return 10 + self.ability_scores.getDexterityModifier()
        
    def getInitiative(self):
        return self.ability_scores.getDexterityModifier()
        
    def __str__(self):
        return f"{self.name} ({self.race} {self.alignment} {self.level})"