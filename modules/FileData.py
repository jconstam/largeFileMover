import os
import six
import sys
import json
import hashlib

class FileInfo:
    def __init__( self, filePath, fileSize = '', fileMD5 = None ):
        self.path = filePath

        if fileSize:
            self.size = fileSize
        else:
            self.size = os.path.getsize( filePath )

        if fileMD5:
            self.md5 = fileMD5
        else:
            self.md5 = hashlib.md5( open( filePath, 'rb' ).read( ) ).hexdigest( )
    
    def addToJSONData( self, jsonData ):
        jsonData[ self.md5 ] = {
            'path': self.path,
            'size': self.size
        }

    def __repr__( self ):
        return '{0} - {1} - {2}'.format( self.path, self.size, self.md5 )

class FileData:
    def __init__( self ):
        self.fileList = []

    def findFiles( self, path ):
        six.print_( 'Searching for files in {0}'.format( path ) )
        fileList = []
        for root, dirs, files in os.walk( os.path.abspath( path ) ):
            for file in files:
                filePath = os.path.abspath( os.path.join( root, file ) )
                if not '/.' in filePath:
                    file = FileInfo( filePath )
                    six.print_( '\tFound file {0} with size {1}'.format( file.path, file.size ) )
                    self.fileList.append( file )

    def sort( self ):
        self.fileList.sort( key=lambda file:file.size, reverse=True )

    def writeFile( self, filePath ):
        fileData = {}
        for file in self.fileList:
            file.addToJSONData( fileData )
        
        with open( filePath, 'w' ) as f:
            json.dump( fileData, f, indent=4 )

    def __repr__( self ):
        output = ''
        for file in self.fileList:
            output += file
        return output
