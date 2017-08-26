import os,sys
from xml.dom.minidom import parse,Text
class DIYDom():
    def __init__(self,path):
        self.path = path
        self.dom = self.toDOM(path)

    def toDOM(self,path):
        if os.path.isfile(path):
            return parse(path)
        return False

    def getNode(self,uri,createFloag = False):
        if uri[0] == "/":
            uri = uri[1:]
        if uri[-1] == "/":
            uri = uri[:-1]

        path = uri.split("/")
        node = self.dom
        existFlag = False

        for p in path:
            for n in node.childNodes:
                if n.nodeName == p:
                    node = n
                    existFlag = True
                    break

            
