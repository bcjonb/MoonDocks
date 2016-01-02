#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmd

class MoonDocks(cmd.Cmd):
  """MoonDocks"""
  state = 0
  prompt = 'Type help  or start to get started> '

  # def __init__(self):
  #   cmd.Cmd.__init__(self)

  def do_start(self, line):
    """Hello there!"""
    print('Hello')
    MoonDocks.state = 1

  def postcmd(self, stop, line):
    # Following should read from the global var but python
    # is a fucking asshole.
    userPrompt = '> ' if MoonDocks.state == 0 else 'What would you like to do? '
    MoonDocks.prompt = userPrompt
    return stop

  def do_exit(self, line):
    return True

  def postloop(self):
    print("Thanks for playing!")

if __name__ == '__main__':
  MoonDocks().cmdloop()
