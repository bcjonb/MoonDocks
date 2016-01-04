#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmd
from player import *
import os, traceback
import shelve

class MoonDocks(cmd.Cmd):
  """MoonDocks"""

  def __init__(self):
    cmd.Cmd.__init__(self)
    self.prompt = 'What would you like to do? '
    self.intro = """

Game start

    """
  ############################################
  # Ingame Commands
  # - NORTH:
  # - SOUTH:
  # - EAST:
  # - WEST:
  ############################################

  ############################################
  # Core Commands
  # - EXIT:
  # - RESTART:
  # - SAVE:
  ############################################

  def do_exit(self, line):
    """Exits game to main menu"""
    return True

  def do_restart(self, line):
    """docstring for do_restart"""
    print('Restarting the game…')
    print('Are you sure? [y/n]: ')
    # TODO: Make restart actually do something…

  def do_save(self, line):
    MainMenu.saveGame(self)
    print("Game Saved.")

  ############################################
  # Cmd Module stuff
  ############################################

  def postloop(self):
    print("Exiting to main menu")

class MainMenu(object):
  player = None

  def displayMenu(self):
    """Display Game Menu"""
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
        MainMenu.player = self.player
        print(self.player.__str__())
        main = False
      elif choice == 2:
        # Check if db exists
        if (not os.path.exists('db/') or
          not os.path.isfile('db/player.db')):
          print("Sorry, no players saved.")
        else:
          print("Loading saved game:\n")
          # TODO: Load game data
      elif choice == 3:
        print("Help coming soon.")
      elif choice == 4:
        quit()

  def levelUp(self):
    main = True
    while main:
      self.player.setExp()
      self.player.rankUp()
      print("\n" + self.player.__str__())
      if self.player.exp > 1000000:
        main = False

  def saveGame(self):
    if not os.path.exists("db/"):
      try:
        os.makedirs("db/")
      except Exception:
        print('Exception:')
        print('-'*60)
        print(traceback.print_exc(file=sys.stdout))
        print('-'*60)
      else:
        pass # sucessfully created db dir. TODO: log to debug

    playerDB = shelve.open('db/player.db')
    try:
      playerDB['profile1'] = {
        'name' : MainMenu.player.name,
        'affiliation' : MainMenu.player.affiliation,
        'rank' : MainMenu.player.rank,
        'exp' : MainMenu.player.exp,
      }
    except Exception:
      print('Exception:')
      print('-'*60)
      print(traceback.print_exc(file=sys.stdout))
      print('-'*60)
    finally:
      playerDB.close()

if __name__ == '__main__':
  mm = MainMenu()
  mm.displayMenu()
  # Save player before game start
  mm.saveGame()
  # Start gameloop
  MoonDocks().cmdloop()
  # Display Main Menu
  mm.displayMenu()
  # do final cleanup if necessary
  input("\n\nPress Enter to exit")
