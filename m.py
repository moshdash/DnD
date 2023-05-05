#https://www.dnd5eapi.co/docs/#overview

import requests
import json
from pprint import pprint as pp

url = "https://www.dnd5eapi.co/api/ability-scores"
r = requests.get(url)
data = r.json()

class DND:
    def __init__(self):
        self.apiurl = "https://www.dnd5eapi.co/api/"

    def getAbilityScores(self, name = None):
        baseurl = self.apiurl + "ability-scores/"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = baseurl + name
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
            
        
    
    def getAlignments(self):
        url = self.apiurl + "alignments"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getBackgrounnds(self):
        url = self.apiurl + "backgrounds"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getClasses(self):
        url = self.apiurl + "classes"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getDamageTypes(self):
        url = self.apiurl + "damage-types"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getEquipment(self):
        url = self.apiurl + "equipment"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getEquipmentCategories(self):
        url = self.apiurl + "equipment-categories"
        r = requests.get(url)
        data =r.json()
        return data

    def getFeats(self):
        url = self.apiurl + "feats"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getFeatures(self):
        url = self.apiurl + "features"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getLanguages(self):
        url = self.apiurl + "languages"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getMagicItems(self):
        url = self.apiurl + "magic-items"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getMagicSchools(self):
        url = self.apiurl + "magic-schools"
        r = requests.get(url)
        data =r.json()
        return data
        
    def getMonsters(self):
        url = self.apiurl + "monsters"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getProficiencies(self):
        url = self.apiurl + "proficiencies"
        r = requests.get(url)
        data =r.json()
        return data

    def getRaces(self):
        url = self.apiurl + "races"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getRuleSections(self):
        url = self.apiurl + "rule-sections"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getRules(self):
        url = self.apiurl + "rules"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getSkills(self):
        url = self.apiurl + "skills"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getSpells(self):
        url = self.apiurl + "spells"
        r = requests.get(url)
        data =r.json()
        return data

    def getSubclasses(self):
        url = self.apiurl + "subclasses"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getSubraces(self):
        url = self.apiurl + "subraces"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getTraits(self):
        url = self.apiurl + "Traits"
        r = requests.get(url)
        data =r.json()
        return data
    
    def getWeaponProperties(self):
        url = self.apiurl + "weapon-properties"
        r = requests.get(url)
        data =r.json()
        return data
dnd = DND()

pp(dnd.getAbilityScores("cha"))
