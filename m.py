#https://www.dnd5eapi.co/docs/#overview

import requests
import json
from pprint import pprint as pp

class DND:
    #Base API URL
    def __init__(self):
        self.apiurl = "https://www.dnd5eapi.co/api/"

    #Functions to search specific categories within the API
    def getAbilityScores(self, name = None):
        #Appends category to base URL
        baseurl = self.apiurl + "ability-scores"
        #If statement to change results to return everything, or information about a specific result
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            #Produces just a list of the results without extra information
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
            
    
    def getAlignments(self, name = None):
        baseurl = self.apiurl + "alignments"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getBackgrounds(self, name = None):
        baseurl = self.apiurl + "backgrounds"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getClasses(self, name = None):
        baseurl = self.apiurl + "classes"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getDamageTypes(self, name = None):
        baseurl = self.apiurl + "damage-type"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getEquipment(self, name = None):
        baseurl = self.apiurl + "equipment"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getEquipmentCategories(self, name = None):
        baseurl = self.apiurl + "equipment-categories"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data

    def getFeats(self, name = None):
        baseurl = self.apiurl + "feats"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getFeatures(self, name = None):
        baseurl = self.apiurl + "features"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getLanguages(self, name = None):
        baseurl = self.apiurl + "languages"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getMagicItems(self, name = None):
        baseurl = self.apiurl + "magic-items"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getMagicSchools(self, name = None):
        baseurl = self.apiurl + "magic-schools"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
        
    def getMonsters(self, name = None):
        baseurl = self.apiurl + "monsters"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getProficiencies(self, name = None):
        baseurl = self.apiurl + "proficiencies"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data

    def getRaces(self, name = None):
        baseurl = self.apiurl + "races"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getRuleSections(self, name = None):
        baseurl = self.apiurl + "rule-sections"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getRules(self, name = None):
        baseurl = self.apiurl + "rules"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getSkills(self, name = None):
        baseurl = self.apiurl + "skills"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getSpells(self, name = None):
        baseurl = self.apiurl + "spells"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data

    def getSubclasses(self, name = None):
        baseurl = self.apiurl + "subclasses"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getSubraces(self, name = None):
        baseurl = self.apiurl + "subraces"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getTraits(self, name = None):
        baseurl = self.apiurl + "traits"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
    
    def getWeaponProperties(self, name = None):
        baseurl = self.apiurl + "weapon-properties"
        if name == None:
            r = requests.get(baseurl)
            data =r.json()
            results = data['results']
            return results
        else:
            nameurl = (f"{baseurl}/{name}")
            r = requests.get(nameurl)
            data =r.json()
            return data
dnd = DND()

pp(dnd.getAbilityScores('cha'))
