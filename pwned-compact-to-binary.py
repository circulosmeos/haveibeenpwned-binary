#!/usr/bin/env python3
#
# compact haveibeenpwned.com password hashes db
# from ASCII to binary form.
#
# v1.0 by circulosmeos, Jan 2018
# https://github.com/circulosmeos/haveibeenpwned-binary
# licensed under GPLv3 or higher
#

import sys, re, os
import subprocess

input_files = [ 'pwned-passwords-1.0.txt.7z', 
                'pwned-passwords-update-1.txt.7z', 
                'pwned-passwords-update-2.txt.7z' 
                ]

hash_lenght = 20; # in bytes

PATH_TO_7z = '/usr/bin/7z' # for linux
#PATH_TO_7z = r'c:\Program Files\7-Zip\7z.exe' # for Windows

def compact_data(file):
    i=0
    output_file = re.sub( r'\.txt\.7z$', '.bin', file )
    print (output_file)
    if not os.path.exists(output_file):
            output_file = open( output_file, "w+b" )
    else:
        exit( "Error: output file already exist: %s\nAborted\n"%output_file )

    proc = subprocess.Popen( [PATH_TO_7z, 'e', '-so', file ], stdout=subprocess.PIPE )
    for line in proc.stdout:
        if ( len(line) < hash_lenght ): break
        i=i+1
        if (i%1000000==0): print (".", end='')
        sys.stdout.flush()
        output_line = bytes.fromhex( "%s"%line[0:-2].decode('ansi') )
        output_file.write( bytearray(output_line) )


for file in input_files:
    compact_data( file )

