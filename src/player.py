# Player class

import random

class Player(object):
    """ A MoonDocks Player """
    AFFILIATIONS = ["Alorean Empire", "United Rebel Alliance"]
    SPECIES = ["Alorean", "Crilac", "Flian", "Cyborg", "Droid"]

    def __init__(self):
        self.name = ""
        self.affiliation = ""
        self.species = ""
        self.rank = 0

    def __str__(self):
        toStr = self.name + ":\nAffiliation: " + self.affiliation + "\nSpecies: " + self.species + "\nRank: " + str(self.rank)
        return toStr

    def setName(self):
        usrName = input("\nWhat is your name?: ")
        self.name = usrName

    def setAffiliation(self):
        aff = """
        ---------------------------------------------------------------------
        | Affiliations:
        |
        | 1) {0}
        | 2) {1}
        ---------------------------------------------------------------------
        """.format(self.AFFILIATIONS[0], self.AFFILIATIONS[1])
        print(aff)
        choice = input("Where do your loyalties lie? Enter Number: ")
        self.affiliation = self.AFFILIATIONS[int(choice) - 1]

    def setSpecies(self):
        if self.affiliation == self.AFFILIATIONS[0]:
            spec = """
        ---------------------------------------------------------------------
        | Species of the Alorean Empire:
        |
        | 1) {0} (Human species)
        | 2) {1} (Reptilian species)
        | 3) {2} (Insectoid slave species)
        | 4) {3} (Reanimated empiric cyborgs)
        | 5) {4} (Mastered AI offspring of the cyborgs)
        | 6) I believe in fate, have destiny choose.
        ---------------------------------------------------------------------
            """.format(self.SPECIES[0], self.SPECIES[1], self.SPECIES[2], self.SPECIES[3], self.SPECIES[4])
            print(spec)
            choice = input("What Species where you born into? Enter Number: ")
            if int(choice) < 6:
                self.species = self.SPECIES[int(choice)-1]
            else:
                n = random.randrange(5)
                if n == 0:
                    self.species = self.SPECIES[int(n)]
                else:
                    self.species = self.SPECIES[int(n)-1]
        else:
            spec = """
        ---------------------------------------------------------------------
        | Species of the United Rebel Alliance:
        |
        | 1) {} (Human species)
        | 2) {} (Insectoid slave species)
        | 3) {} (Reanimated empiric cyborgs)
        | 4) I believe in fate, have destiny choose.
        ---------------------------------------------------------------------
            """.format(self.SPECIES[0], self.SPECIES[2], self.SPECIES[3])
            print(spec)
            choice = input("What Species where you born into? Enter Number: ")
            if int(choice) == 1:
                self.species = self.SPECIES[int(choice)-1]
            elif int(choice) <= 3:
                self.species = self.SPECIES[int(choice)]
            else:
                n = random.randrange(3)
                if int(n) == 1:
                    self.species = self.SPECIES[int(n)-1]
                elif int(n) <= 3:
                    self.species = self.SPECIES[int(n)]

class Game(object):
    def display_instruct(self):
        """Display Game Instructions"""
        main = True

        splash = """
            ----------------------------------------------------------------------
            |MoonDocks: Fall of Illusions.                                       |
            |The journey of Revolutionaries who don't know their true importance.|
            |Join them in bringing freedom across the known galaxy.              |
            ----------------------------------------------------------------------
        """
        menu = """
            ----------------------------------------------------------------------
            | MAIN MENU:                                                         |
            | ---------                                                          |
            |                                                                    |
            | 1) Start New Game.                                                 |
            | 2) Load Game.                                                      |
            | 3) Read Help.                                                      |
            | 4) Quit.                                                           |
            ----------------------------------------------------------------------
        """
        print(splash)
        while main:
            print(menu)
            choice = int(input("What would you like to do?: "))
            if choice == 1:
                player = Player()
                player.setName()
                player.setAffiliation()
                player.setSpecies()
                print(player.__str__())
                main = False
            elif choice == 2:
                print("Sorry, no players saved.")
            elif choice == 3:
                print("Help coming soon.")
            elif choice == 4:
                quit()

def createPlayer():
    print("\t\tWelcome to Create Player")
    name = input("What is your Name?: ")
    print("Hello " + name + "\n")
    affiliation = input("What Affiliation would you like to join?: ")
    species = input("\nAnd what species are you?: ")
    final_player = Player(name, affiliation, species)
    print(final_player.__str__() + " Created.")

game = Game()
game.display_instruct()
input("\n\nPress Enter to exit")
