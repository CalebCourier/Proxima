#__author__ = 'Caleb'
import os
def getPath(relPath):
    dir = os.path.dirname(__file__)
    return dir + relPath
