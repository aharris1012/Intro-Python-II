# Write a class to hold player information, e.g. what room they are in
# currently.




class Player:
   
    def __init__(self, name, location, inventory=[]):
        self.name = name
        self.location = location
        self.inventory = inventory


    def __str__(self):
        
        return f"<Name: {self.name}, location: {self.location}, inventory: {self.inventory}>"

    def pickup_items(*items):
        print('Player picked up items...')
        for item in items:
            self.inventory.append(item)
            print(f'{item}') 