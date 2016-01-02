# Player class

import random
import os

os.system('cls')
os.system('clear')

class Player(object):
    """ A MoonDocks Player """
    AFFILIATIONS = ["Alorean Empire", "United Rebel Alliance"]
    SPECIES = ["Alorean", "Crilac", "Flian", "Cyborg", "Droid"]

    RANKSCIVILION = ["Civilian", "Known", "Popular", "Famous", "Reknowned",
                     "Trusted", "Emporer's Servent", "Emperor's Consort",
                     "Emporer's Concubine", "Emperor's Main Concubine"]
    RANKSMILITARY = ["Crewman", "Petty Officer", "Chief Petty Officer",
                     "Master Chief Petty Officer", "Chief Warrent Officer",
                     "Ensign", "Lieutenant", "Lieutenant Commander",
                     "Commander", "Captian"]
    RANKSREBELS = ["Crewman", "Petty Officer", "Chief Petty Officer",
                    "Master Chief Petty Officer", "Chief Warrent Officer",
                    "Ensign", "Lieutenant", "Lieutenant Commander",
                    "Commander", "Captian"]
    #RANKSREBELS = ["Private", "Corporal", "Sergeant", "Sergeant Major",
                    #"Chief Warrent Officer",  "Lieutenant", "Captain",
                    #"Major", "Lieutenant Colonel", "Colonel", "General"]

    def __init__(self):
        self.name = ""
        self.affiliation = ""
        self.species = ""
        self.rank = "Unknown"
        self.exp = 0

    def __str__(self):
        toStr = "Player Name:" + self.name + "\nAffiliation: " + self.affiliation + "\nSpecies: " + self.species + "\nRank: " + str(self.rank)
        return toStr

    def setName(self):
        usrName = input("\nWhat is your name?: ")
        self.name = usrName

    def setAffiliation(self):
        aff = """
        ---------------------------------------------------------------------
        | Affiliations:
        |
        | 1) {}
        | 2) {}
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
        | 1) {} (Human species)
        | 2) {} (Reptilian species)
        | 3) {} (Insectoid slave species)
        | 4) {} (Reanimated empiric cyborgs)
        | 5) {} (Mastered AI offspring of the cyborgs)
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
    def rankUp(self):
        exp = self.exp
        #==================================================Level 0
        if exp < 100:
            self.rank = "Unknown"
        #==================================================Level 1
        if exp > 100 and exp < 250:
            if self.affiliation == self.AFFILIATIONS[0]:
                if self. species == self.SPECIES[2]:
                    self.rank = self.RANKSCIVILION[0]
                else:
                    self.rank = self.RANKSMILITARY[0]
            if self.affiliation == self.AFFILIATIONS[1]:
                self.rank = self.RANKSREBELS[0]
        #==================================================Level 2
        elif exp > 250 and exp < 625:
            if self.affiliation == self.AFFILIATIONS[0]:
                if self. species == self.SPECIES[2]:
                    self.rank = self.RANKSCIVILION[1] #Change
                else:
                    self.rank = self.RANKSMILITARY[1] #Change
            if self.affiliation == self.AFFILIATIONS[1]:
                self.rank = self.RANKSREBELS[1] #Change
        #==================================================Level 3
        elif exp > 625 and exp < 1550:
            if self.affiliation == self.AFFILIATIONS[0]:
                if self. species == self.SPECIES[2]:
                    self.rank = self.RANKSCIVILION[2] #Change
                else:
                    self.rank = self.RANKSMILITARY[2] #Change
            if self.affiliation == self.AFFILIATIONS[1]:
                self.rank = self.RANKSREBELS[2] #Change
        #==================================================Level 4
        elif exp > 1550 and exp < 3875:
            if self.affiliation == self.AFFILIATIONS[0]:
                if self. species == self.SPECIES[2]:
                    self.rank = self.RANKSCIVILION[3] #Change
                else:
                    self.rank = self.RANKSMILITARY[3] #Change
            if self.affiliation == self.AFFILIATIONS[1]:
                self.rank = self.RANKSREBELS[3] #Change
        #==================================================Level 5
        elif exp > 3875 and exp < 9700:
            if self.affiliation == self.AFFILIATIONS[0]:
                if self. species == self.SPECIES[2]:
                    self.rank = self.RANKSCIVILION[4] #Change
                else:
                    self.rank = self.RANKSMILITARY[4] #Change
            if self.affiliation == self.AFFILIATIONS[1]:
                self.rank = self.RANKSREBELS[4] #Change
        #==================================================Level 6
        elif exp > 9700 and exp < 24250:
            if self.affiliation == self.AFFILIATIONS[0]:
                if self. species == self.SPECIES[2]:
                    self.rank = self.RANKSCIVILION[5] #Change
                else:
                    self.rank = self.RANKSMILITARY[5] #Change
            if self.affiliation == self.AFFILIATIONS[1]:
                self.rank = self.RANKSREBELS[5] #Change
        #==================================================Level 7
        elif exp > 24250 and exp < 60625:
            if self.affiliation == self.AFFILIATIONS[0]:
                if self. species == self.SPECIES[2]:
                    self.rank = self.RANKSCIVILION[6] #Change
                else:
                    self.rank = self.RANKSMILITARY[6] #Change
            if self.affiliation == self.AFFILIATIONS[1]:
                self.rank = self.RANKSREBELS[6] #Change
        #==================================================Level 8
        elif exp > 60625 and exp < 151550:
            if self.affiliation == self.AFFILIATIONS[0]:
                if self. species == self.SPECIES[2]:
                    self.rank = self.RANKSCIVILION[7] #Change
                else:
                    self.rank = self.RANKSMILITARY[7] #Change
            if self.affiliation == self.AFFILIATIONS[1]:
                self.rank = self.RANKSREBELS[7] #Change
        #==================================================Level 9
        elif exp > 151550 and exp < 378875:
            if self.affiliation == self.AFFILIATIONS[0]:
                if self. species == self.SPECIES[2]:
                    self.rank = self.RANKSCIVILION[8] #Change
                else:
                    self.rank = self.RANKSMILITARY[8] #Change
            if self.affiliation == self.AFFILIATIONS[1]:
                self.rank = self.RANKSREBELS[8] #Change
        #==================================================Level 10
        elif exp > 378875 and exp <= 1000000:
            if self.affiliation == self.AFFILIATIONS[0]:
                if self. species == self.SPECIES[2]:
                    self.rank = self.RANKSCIVILION[9] #Change
                else:
                    self.rank = self.RANKSMILITARY[9] #Change
            if self.affiliation == self.AFFILIATIONS[1]:
                self.rank = self.RANKSREBELS[9] #Change
        #==========================================================
    def setExp(self):
        value = input("\nSet exp to?: Enter Value between 0 and 1000000: ")
        self.exp = int(value)

class Game(object):
    player = None
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
                self.player = Player()
                self.player.setName()
                self.player.setAffiliation()
                self.player.setSpecies()
                print(self.player.__str__())
                main = False
            elif choice == 2:
                print(
                """
                ----------------------------
                | Sorry, no players saved. |
                ----------------------------
                """
                )
            elif choice == 3:
                print("Help coming soon.")
            elif choice == 4:
                quit()
    def levelUp(self):
        main = True
        while main:
            self.player.setExp()
            self.player.rankUp()
            print("\n"+ self.player.__str__())
            if self.player.exp >1000000:
                main = False


game = Game()
game.display_instruct()
game.levelUp()


input("\n\nPress Enter to exit")
