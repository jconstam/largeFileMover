import os
import sys
import json
import hashlib
import operator

class FileInfo:
    def __init__( self, filePath, fileSize = '', fileMD5 = '' ):
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

    def getData( self ):
        return { 'path': self.path, 'size': self.size, 'md5': self.md5 }

class FileData:
    def __init__( self ):
        self.fileList = {}
        self.fileExtensions = [ '.mkv', '.mp4', '.avi', '.ts', '.m4v', '.wmv', '.mpg', '.sfv', '.srr', '.rmvb' ]

    def findFiles( self, path ):
        print 'Searching for files in {0}'.format( path )
        self.fileList = {}
        for root, dirs, files in os.walk( os.path.abspath( path ) ):
            for file in files:
                filePath = os.path.abspath( os.path.join( root, file ) )
                fileName, fileExtension = os.path.splitext( filePath )
                if not '/.' in filePath and fileExtension in self.fileExtensions:
                    file = FileInfo( filePath )
                    print '\tFound file {0} with size {1}'.format( file.path, file.size )
                    self.fileList[ file.md5 ] = file

    def sort( self ):
        return sorted( self.fileList.values( ), key=operator.attrgetter( 'size' ), reverse=True )

    def compare( self, other ):
        both = {}
        thisOnly = {}
        otherOnly = {}
        for file in self.fileList.values( ):
            if file.md5 in self.fileList.keys( ) and file.md5 in other.fileList.keys( ):
                both[ file.md5 ] = file
            elif file.md5 in self.fileList.keys( ):
                thisOnly[ file.md5 ] = file
        for file in other.fileList.values( ):
            if not file.md5 in otherOnly:
                otherOnly[ file.md5 ] = file

        return ( both, thisOnly, otherOnly )


    def writeFile( self, filePath ):
        fileData = {}
        for file in self.fileList.values( ):
            fileData[ file.md5 ] = file.getData( )

        with open( filePath, 'w' ) as f:
            json.dump( fileData, f, indent=4 )

    def __repr__( self ):
        output = ''
        for file in self.fileList:
            output += file
        return output
