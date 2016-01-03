#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import argparse
import shelve
import sys
 
#################################
# Console stuff, ignore
#################################
parser = argparse.ArgumentParser()
parser.add_argument('-w', '--write', help='Writes data to disk',
                    action='store_true',
                    default=False)
parser.add_argument('-r', '--read', help='Reads data from disk',
                    action='store_true',
                    default=False)
args = parser.parse_args()
 
#################################
# This writes/opens a db file.
# *note: the .db postfix is added
# automatically.
#################################
s = shelve.open('test_shelf')
 
if args.write: # ignore this
  print('WRITING!') # this
  #################################
  # This writs to the db file.
  #################################
  try:
    s['key1'] = { 'name' : 'Brandon', 'race' : 'human' }
  finally:
    s.close()
if args.read: # this...
  print('READING!') # and this
  #################################
  # This reads from the db file.
  #################################
  try:
    existing = s['key1']
  finally:
    s.close()
  print(existing)
