#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmd
import os
# import shelve

class MDManager(cmd.Cmd, object):

  # Colorize
  purple='\033[95m'
  gray='\033[1;30m'
  nc='\033[0m'

  dbCache = []
  dbDir = './db/'
  prompt = '''{gray}Moondocks Manager: {purple}{db}{nc}
❯ '''.format(purple=purple, gray=gray, nc=nc, db=None)

  def __init__(self):
    cmd.Cmd.__init__(self)
    self.ruler = '-'
    self.intro = '''

    Welcome to the MoonDocks Database Manager (MDdb)

    MDdb Commands:
    - {purple}open{nc}:   Opens a database
    - {purple}close{nc}:  Closes the current database
    - {purple}list{nc}:   Lists available databases
    - {purple}create{nc}: Creates a new database
    - {purple}show{nc}:   Show the contents of a database
    - {purple}insert{nc}: Insert's data into the database
    - {purple}help{nc}:   Get help for a command

    *Note: Use tab to autocomplete commands.

    '''.format(purple=MDManager.purple, nc=MDManager.nc)

  ## Database commands

  ## Core commands

  def updatedbCache():
    '''Update the list of available db'''
    MDManager.dbCache = []
    for dirname, dirnames, filenames in os.walk(MDManager.dbPath):
      for filename in filenames:
        MDManager.dbCache.append(filename)

  def opendb():
    """Open a database"""


  def listdb():
    """List db"""
    _index = 0
    for dirname, dirnames, filenames in os.walk(MDManager.dbPath):
      print('└── ' + os.path.basename(dirname))
      for filename in filenames:
        print('   └── '
              + '\033[95m'
              + os.path.join(filename)
              + '\033[0m'
              )
        _index += 1
      print('''
Available database(s): {0}{1}{2} '''.format('\033[95m', _index, '\033[0m'))

  def do_exit(self, args):
    '''Exit MoonDocks db Manager'''
    return -1

  def do_EOF(self, args):
    '''Exit on system EOF character'''
    return self.do_exit(args)

  def do_shell(self, args):
    '''Pass command to the system shell when the line begins with `!`'''
    os.system(args)

  def do_help(self, args):
    '''Get help for commands
        `help` or `?` with no arguments prints a list of commands
        `help «command»` or `? «command»` gives help on «command»
    '''
    cmd.Cmd.do_help(self, args)

  #################################################
  # Override Cmd object methods
  #################################################

  def precmd(self, line):
    """Pre command processing"""
    MDManager.updatedbCache()
    return line

  def postcmd(self, stop, line):
    '''Post command processing'''
    print('') # adds an empty space
    print('current db: ' + MDManager.database)
    MDManager.prompt = 'MoonDocks Manager: {0}{1}{2} ❯ '.format(
          '\033[95m', MDManager.currentDB(), '\033[0m')
    return stop

  def preloop(self):
    '''Initialization before prompting user for commands.'''
    cmd.Cmd.preloop(self)
    self._hist    = []
    self._locals  = {}
    self._globals = {}

  def postloop(self):
    '''Do any necessary cleanup.'''
    cmd.Cmd.postloop(self)
    os.system('clear')
    print('Closing MoonDocks db Manager...')


if __name__ == '__main__':
  os.system('clear')
  mdmanager = MDManager()
  mdmanager.cmdloop()
