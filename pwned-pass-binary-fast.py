#!/usr/bin/env python2
#
# Search in haveibeenpwned.com hashes password db.
# Based on https://gist.github.com/alexanderzobnin/09db0c9f74754d32d3c2538d4d6a3b0d
# but using binary files instead of plain text files:
#   See pwned-compact-to-binary.py to convert ASCII password files to binary form.
#
# Adapted to be used as a cmdline command: 
#   returns 0 when password is found/compromised, 1 otherwise.
# Plain text password is provided as parameter
#
# v1.0 by circulosmeos, Jan 2018
# https://github.com/circulosmeos/haveibeenpwned-binary
# licensed under GPLv3 or higher
#

import os
import hashlib
import sys

pwned_passwords_files = [
  "pwned-passwords-update-1.bin",
  "pwned-passwords-update-2.bin",
  "pwned-passwords-1.0.bin"
]

HASH_LENGTH = 20; # in bytes

VERBOSE = 0 # 0: silent mode; 1, 2: print verbose

def getFileSize(filename):
  return os.path.getsize(filename)

def searchForPass(password):
  pass_hash = hashlib.sha1(password).hexdigest().upper()
  if (VERBOSE>0): print("\nSearching for SHA1 hash: %s" % pass_hash)
  for password_file in pwned_passwords_files:
    if (VERBOSE>0): print("Searching in: %s" % password_file)

    try:
        filesize = getFileSize(password_file)
    except:
        if (VERBOSE>0): print( "File not found: %s" % password_file )
        return 1
    number_of_hashes = filesize / HASH_LENGTH
    if (VERBOSE>1): print("File size is: %s bytes, hash length is %s bytes, number of hashes is %s" % (filesize, HASH_LENGTH, number_of_hashes))
    pos_from = 0
    pos_to = number_of_hashes

    with open(password_file, "rb") as file:
      while True:
        current_pos = int ((pos_to + pos_from) / 2)

        file.seek(current_pos * HASH_LENGTH)
        pwned_hash = file.read( HASH_LENGTH ).encode('hex').upper()
        if (VERBOSE>1): print("Go to %s hash position #%s" % (pwned_hash, current_pos))

        if pwned_hash == pass_hash:
          if (VERBOSE>0): print("Found: '%s' as %s" % (password, pwned_hash))
          return 0

        if abs(pos_to - pos_from) < 1:
          break

        if pwned_hash < pass_hash:
          pos_from = current_pos
          if abs(pos_to - pos_from) <= 1:
            pos_from = pos_to
        else:
          pos_to = current_pos
          if abs(pos_to - pos_from) <= 1:
            pos_to = pos_from

  if (VERBOSE>0): print("Not found, all clear!")
  return 1

if ( len(sys.argv[1])>0 ):
  exit ( # cmdline return value: 0 TRUE (password compromised), 1 FALSE (password not compromised)
    searchForPass( sys.argv[1] ) 
    )
