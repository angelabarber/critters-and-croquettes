from datetime import date


class Anaconda:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.slithering = True
        self.food = food
        self.date_added = date.today()
    
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
