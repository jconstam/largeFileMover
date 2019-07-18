import os
import six
import sys

def getLargestFiles( path, count ):
    fileList = []
    for root, dirs, files in os.walk( os.path.abspath( path ) ):
        for file in files:
            fileName = os.path.abspath( os.path.join( root, file ) )
            if not '/.' in fileName:
                fileSize = os.path.getsize( fileName )
                fileList.append( ( fileName, fileSize ) )

    fileList.sort( key=lambda filename: filename[ 1 ], reverse=True )

    return fileList[:count]

if __name__ == '__main__':
    six.print_( 'Python version: {0}'.format( sys.version ) )

    six.print_( getLargestFiles( './', 10 ) )

exit( 0 )