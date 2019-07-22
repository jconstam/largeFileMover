import os
import sys
import json
import hashlib

class FileInfo:
    def __init__( self, filePath, fileSize = '', fileMD5 = None ):
        self.hashSize = 1024 * 1024
        self.path = filePath

        if fileSize:
            self.size = fileSize
        else:
            self.size = os.path.getsize( filePath )

        if fileMD5:
            self.md5 = fileMD5
        else:
            self.md5 = hashlib.md5( open( filePath, 'rb' ).read( self.hashSize ) ).hexdigest( )
    
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
        self.fileExtensions = [ '.mkv', '.mp4', '.avi', '.ts', '.m4v', '.wmv', '.mpg', '.sfv', '.srr', '.rmvb' ]

    def findFiles( self, path ):
        print 'Searching for files in {0}'.format( path )
        fileList = []
        for root, dirs, files in os.walk( os.path.abspath( path ) ):
            for file in files:
                filePath = os.path.abspath( os.path.join( root, file ) )
                fileName, fileExtension = os.path.splitext( filePath )
                if not '/.' in filePath and fileExtension in self.fileExtensions:
                    file = FileInfo( filePath )
                    print '\tFound file {0} with size {1}'.format( file.path, file.size )
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
