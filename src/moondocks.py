#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmd
from player import *
import os
from os import walk

class MoonDocks(cmd.Cmd):
  """MoonDocks"""

  def __init__(self):
    cmd.Cmd.__init__(self)
    # TODO: add custom banners
    self.prompt = 'What would you like to do? '
    self.intro = """

Game start

    """

  ################################################
  # Player Commands
  # - NORTH:
  # - SOUTH:
  # - EAST:
  # - WEST:
  ################################################

  ################################################
  # Core Game Commands
  # - EXIT:    Exits the game to the main menu.
  # - RESTART: Restarts the game.
  # - SAVE:    Saves the current game state.
  ################################################

  def do_exit(self, line):
    """Exits game to the main menu"""
    os.system('cls')
    os.system('clear')
    return True

  def do_restart(self, line):
    """docstring for do_restart"""
    print('Are you sure? This cannot be undone [y/n]: ')
    print('Restarting the game…')
    # TODO: Make restart actually do something…

  def do_save(self, line):
      Game.saveGame(self)
      print("Game Save.")

  def postloop(self):
    print("Exiting to main menu")

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
                Game.player = self.player
                print(self.player.__str__())
                main = False
            elif choice == 2:
                if not os.path.exists("savedGames/"):
                    print("Sorry, no players saved.")
                else:
                    print("savedGames exists:\n")
                    f = []
                    for (dirpath, dirnames, filenames) in walk("savedGames/"):
                        f.extend(filenames)
                        break
                    print(f)
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
    def saveGame(self):
        if not os.path.exists("savedGames/"):
            os.makedirs("savedGames/")
        path = "savedGames/" + str(Game.player.name) + ".txt"
        saveFile = open(path, "w+")
        saveFile.write(Game.player.saveString())
        saveFile.close()

if __name__ == '__main__':
  # Start the main menu
  game = Game()
  game.display_instruct()
  # Start gameloop
  MoonDocks().cmdloop()
  # Display Main Menu
  game.display_instruct()
  # Do final cleanup if necesarry
  input("\n\nPress Enter to exit")
