import os
import six
import sys

from modules.FileData import FileData as FileData

if __name__ == '__main__':
    six.print_( 'Python version: {0}'.format( sys.version ) )

    data = FileData( )
    data.findFiles( './' )
    data.sort( )
    six.print_( data.fileList )

    exit( 0 )