# Player class

class Player(object):
    """ A MoonDocks Player """
    AFFILIATION = ["Empire", "Alliance"]
    SPECIES = ["Human", "Crilac", "Flian", "Cyborg", "Droid"]

    def __init__(self, name, affiliation, species):
        self.name = name
        self.affiliation = affiliation
        self.species = species
        self.rank = 0

    def __str__(self):
        toStr = self.name + ":\nAffiliation: " + self.affiliation + "\nSpecies: " + self.species + "\nRank: " + str(self.rank)
        return toStr

    def setName(value):
        self.name = value

    def setAffiliation(value):
        self.affiliation = value

def display_instruct():
    """Display Game Instructions"""
    print(
    """
        ----------------------------------------------------------------------
        |MoonDocks: Fall of Illusions.                                       |
        |The journey of Revolutionaries who don't know their true importance.|
        |Join them in bringing freedom across the known galaxy.              |
        ----------------------------------------------------------------------
    """
    )
    input("To begin Enter 'begin journey' in the console.")

def createPlayer():
    print("\t\tWelcome to Create Player")
    name = input("What is your Name?: ")
    print("Hello " + name + "\n")
    affiliation = input("What Affiliation would you like to join?: ")
    species = input("\nAnd what species are you?: ")
    final_player = Player(name, affiliation, species)
    print(final_player.__str__() + " Created.")

#display_instruct()
#createPlayer()
player = Player("Jon", "A", "human")
print(player.__str__())
input("\n\nPress Enter to exit")
