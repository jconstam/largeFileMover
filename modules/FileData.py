import os
import hashlib

class FileInfo:
    def __init__( self, filePath, fileSize = '', fileMD5 = None ):
        self.filePath = filePath

        if fileSize:
            self.fileSize = fileSize
        else:
            self.fileSize = os.path.getsize( filePath )

        if fileMD5:
            self.fileMD5 = fileMD5
        else:
            self.fileMD5 = hashlib.md5( open( filePath, 'rb' ).read( ) )

    def __repr__( self ):
        return '{0} - {1} - {2}'.format( self.filePath, self.fileSize, self.fileMD5.hexdigest( ) )

class FileData:
    def __init__( self ):
        self.fileList = []

    def findFiles( self, path ):
        fileList = []
        for root, dirs, files in os.walk( os.path.abspath( path ) ):
            for file in files:
                filePath = os.path.abspath( os.path.join( root, file ) )
                if not '/.' in filePath:
                    self.fileList.append( FileInfo( filePath ) )

    def sort( self ):
        self.fileList.sort( key=lambda file:file.fileSize, reverse=True )

    def __repr__( self ):
        output = ''
        for file in self.fileList:
            output += file
        return output
