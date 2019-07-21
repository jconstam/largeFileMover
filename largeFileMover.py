import os

from modules.FileData import FileData as FileData

if __name__ == '__main__':
    data = FileData( )
    data.findFiles( './' )
    data.sort( )
    data.writeFile( './test.json' )

    exit( 0 )