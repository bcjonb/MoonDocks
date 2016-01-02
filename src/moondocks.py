#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmd
from player import *

class MoonDocks(cmd.Cmd):
  """MoonDocks"""

  def __init__(self):
    cmd.Cmd.__init__(self)
    self.intro = """

Game start

    """

  def do_exit(self, line):
    return True

  def postloop(self):
    print("Thanks for playing!")

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
                print("Sorry, no players saved.")
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

if __name__ == '__main__':
  game = Game()
  game.display_instruct()
  # Stop mr. Brauns FUCK YOU loop
  # game.levelUp()
  # Start gameloop
  MoonDocks().cmdloop()
  input("\n\nPress Enter to exit")