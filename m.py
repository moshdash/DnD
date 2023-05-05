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
        baseurl = self.apiurl + "ability-scores"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
            
    
    def getAlignments(self, name = None):
        baseurl = self.apiurl + "alignments"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getBackgrounds(self, name = None):
        baseurl = self.apiurl + "backgrounds"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getClasses(self, name = None):
        baseurl = self.apiurl + "classes"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getDamageTypes(self, name = None):
        baseurl = self.apiurl + "damage-type"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getEquipment(self, name = None):
        baseurl = self.apiurl + "equipment"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getEquipmentCategories(self, name = None):
        baseurl = self.apiurl + "equipment-categories"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data

    def getFeats(self, name = None):
        baseurl = self.apiurl + "feats"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getFeatures(self, name = None):
        baseurl = self.apiurl + "features"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getLanguages(self, name = None):
        baseurl = self.apiurl + "languages"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getMagicItems(self, name = None):
        baseurl = self.apiurl + "magic-items"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getMagicSchools(self, name = None):
        baseurl = self.apiurl + "magic-schools"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
        
    def getMonsters(self, name = None):
        baseurl = self.apiurl + "monsters"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getProficiencies(self, name = None):
        baseurl = self.apiurl + "proficiencies"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data

    def getRaces(self, name = None):
        baseurl = self.apiurl + "races"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getRuleSections(self, name = None):
        baseurl = self.apiurl + "rule-sections"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getRules(self, name = None):
        baseurl = self.apiurl + "rules"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getSkills(self, name = None):
        baseurl = self.apiurl + "skills"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getSpells(self, name = None):
        baseurl = self.apiurl + "spells"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data

    def getSubclasses(self, name = None):
        baseurl = self.apiurl + "subclasses"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getSubraces(self, name = None):
        baseurl = self.apiurl + "subraces"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getTraits(self, name = None):
        baseurl = self.apiurl + "Traits"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
    
    def getWeaponProperties(self, name = None):
        baseurl = self.apiurl + "weapon-properties"
        if name == None:
            print(baseurl)
            r = requests.get(baseurl)
            data =r.json()
            return data
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            print(nameurl)
            return data
dnd = DND()

pp(dnd.getSkills("stealth"))
