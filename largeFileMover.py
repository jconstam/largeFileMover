import os

from modules.FileData import FileData as FileData

if __name__ == '__main__':
    if not os.path.exists( './testing' ):
        os.makedirs( './testing' )

    data = FileData( )
    data.findFiles( './' )
    data.sort( )
    data.writeFile( './testing/test.json' )

    exit( 0 )