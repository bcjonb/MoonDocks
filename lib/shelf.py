#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import shelve

#####################################
# Console stuff; ignore
#####################################
parser = argparse.ArgumentParser()
parser.add_argument('-w', '--write', help='Writes data to disk',
                    action='store_true',
                    default=False)
parser.add_argument('-r', '--read', help='Reads data from disk',
                    action='store_true',
                    default=False)
args = parser.parse_args()

#####################################
# This creates or opens the
# 'game.db' file.
#####################################
playerDB = shelve.open('db/player.db')

if args.write: # ignore this
  print('WRITING!') # this
  #####################################
  # This writs to the db file.
  #####################################
  try:
    playerDB['profile1'] = {
      'name' : 'Brandon',
      'affiliation' : 'Alorean Empire',
      'species': 'Alorean'
    }
  finally:
    playerDB.close()
if args.read: # this...
  print('READING!') # and this
  #####################################
  # This reads from the db file.
  #####################################
  try:
    player = playerDB['profile1']
  finally:
    playerDB.close()
  print(player)
