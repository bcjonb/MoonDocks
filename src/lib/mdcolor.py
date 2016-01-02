#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MDColorize():
  def __init__(self):
    self.mdgray='\033[1;30m'
    self.mdpurple = '\033[95m'
    self.mdblue = '\033[94m'
    self.mdgreen = '\033[92m'
    self.mdyellow = '\033[93m'
    self.mdred = '\033[91m'
    self.mdENDC = '\033[0m'
    # BOLD = '\033[1m'
    # UNDERLINE = '\033[4m'

  def gray(self, msg):
    return self.mdgray + msg + self.mdENDC

  def purple(self, msg):
    return self.mdpurple + msg + self.mdENDC

  def blue(self, msg):
    return self.mdblue + msg + self.mdENDC

  def green(self, msg):
    return self.mdgreen + msg + self.mdENDC

  def yellow(self, msg):
    return self.mdyellow + msg + self.mdENDC

  def red(self, msg):
    return self.mdred + msg + self.mdENDC

mdcolorize = MDColorize()
print(mdcolorize.gray('hello'))
