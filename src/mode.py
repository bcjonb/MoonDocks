#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmd

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

if __name__ == '__main__':
  MoonDocks().cmdloop()
