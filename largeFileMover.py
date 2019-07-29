#!/usr/bin/python

import os
import argparse

from modules.FileData import FileData as FileData

def parseArgs( ):
    parser = argparse.ArgumentParser( )
    parser.add_argument( '-r', '--rootPath', required=True, help='Root path to search for files' )
    return parser.parse_args( )

if __name__ == '__main__':
    if not os.path.exists( './testing' ):
        os.makedirs( './testing' )
    
    args = parseArgs( )

    data = FileData( )
    data.findFiles( args.rootPath )
    data.writeFile( './testing/test.json' )

    exit( 0 )