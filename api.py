import requests

class API:
    def __init__(self):
        self.apiurl = "https://www.dnd5eapi.co/api/"
        self.resource_type = [
            'ability-scores', 'alignments', 'backgrounds', 'classes',
            'damage-types', 'equipment', 'equipment-categories', 'features',
            'languages', 'magic-items', 'magic-schools', 'monsters',
            'proficiencies', 'races', 'rule-sections', 'rules', 'skills',
            'spells', 'subclasses', 'subraces', 'traits', 'weapon-properties'
        ]

    def displayResourceTypes(self):
        return self.resource_type

    def getResources(self, resource_type=None, name=None):
        if not resource_type or resource_type not in self.displayResourceTypes():
            print("Please select from the below list of categories to learn")
            print("Available Categories:")
            return ', '.join(self.displayResourceTypes())
            
        baseurl = self.apiurl + resource_type
        if name is None:
            r = requests.get(baseurl)
            data = r.json()
            # Extract just the name from each result
            results = [result['name'] for result in data['results']]
            return results
        else:
            nameurl = f"{baseurl}/{name}"
            r = requests.get(nameurl)
            if r.status_code == 404:
                print(f"{name} not found in {resource_type} resources.")
                return []
            else:
                data = r.json()
                return data
