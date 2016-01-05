#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmd
import os
import shelve

class MDManager(cmd.Cmd, object):

  baseDir = './'
  dbPath = baseDir + 'db'
  dbList = []
  currentDB = None
  database = None
  mdPrompt = 'MoonDocks db Manager: %s ❯ ' % (currentDB)
  prompt = mdPrompt

  def __init__(self):
    cmd.Cmd.__init__(self)
    self.ruler = '-'
    self.intro = '''

    Welcome to the MoonDocks Database Manager (MDdb)

    MDdb Commands:
    - {purple}open{nc}:   Opens a database
    - {purple}close{nc}:  Closes the current database
    - {purple}list{nc}:   Lists available databases
    - {purple}switch{nc}: Switches to a new database
    - {purple}show{nc}:   Show the contents of a database
    - {purple}help{nc}:   Get help for a command

    *Note: Use tab to autocomplete commands.

    '''.format(purple='\033[95m', nc='\033[0m')

  ## Database commands

  def do_open(self, args):
    '''Opens a database'''

    if not MDManager.closeDB():
      return
    elif (args == '' or args == ' '):
      opendb = input('\nWhich database would you like to open?: ')
      if opendb != '' or opendb != ' ':
        MDManager.currentDB = opendb
      return
    else:
      print(' Opening db: %s ' % (args))
      MDManager.currentDB = args

  def do_close(self, args):
    '''Close the current database'''
    MDManager.closeDB()

  def do_list(self, args):
    '''Show available databases'''
    print('Listing databases:')
    index = 0
    for dirname, dirnames, filenames in os.walk(MDManager.dbPath):
      # print path to all subdirectories first.
      # for subdirname in dirnames:
      #   print(os.path.join(dirname, subdirname))

      # print path to all filenames.
      print('└── ' + os.path.basename(dirname))
      for filename in filenames:
        print('   └── '
              + '\033[95m'
              + os.path.join(filename)
              + '\033[0m'
              )
        index += 1
      print('''
Available database(s): {0}{1}{2} '''.format('\033[95m', index, '\033[0m'))
      MDManager.updatedbList()

  def do_show(self, args):
    """Show the contents of a database"""
    print('Yeahp, it\'s in here')

  ## Core commands

  def updatedbList():
    '''Update the list of available db'''
    MDManager.dbList = []
    for dirname, dirnames, filenames in os.walk(MDManager.dbPath):
      for filename in filenames:
        MDManager.dbList.append(filename)

  def closeDB():
    '''Close an open database'''
    if MDManager.currentDB is not None:
      print(' The database: %s is open. ' % (MDManager.currentDB))
      # Prompt before closing
      askClose = input('\nWould you like to close it now? [y/n]: ').lower()
      if askClose == 'y':
        print('Closing the database...')
        # TODO: shelve close db
        MDManager.currentDB = None
        # db closed
        return True
      else:
        # db open
        return False
    else:
      # No db open
      return True

  def do_exit(self, args):
    '''Exit MoonDocks db Manager'''
    if MDManager.closeDB():
      return -1
    return

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

  def postcmd(self, stop, line):
    '''Post command processing'''
    print('') # adds an empty space
    MDManager.prompt = 'MoonDocks db Manager: %s ❯ ' % (MDManager.currentDB)
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
    print('Closing MoonDocks db Manager...')


if __name__ == '__main__':
  os.system('clear')
  mdmanager = MDManager()
  mdmanager.cmdloop()
