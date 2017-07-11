#!/bin/python

# Robert Toomey May 2017
# Class for building 'something'
# until I figure where best to put it
import buildtools as b

class Builder:
  """ Build a individual package such as 'netcdf' """
  def __init__(self, key):
    self.key = key
  def clean(self):
    """ Clean up.  For example, Third party removes the uncompressed folder. """
    pass 
  def copy(self, t):
    """ Copy self to destination """
    pass
  def unzip(self):
    """ Do any unpacking needed.  Third party libraries are typically compressed """
    pass
  def build(self, t, c, m):
    """ Run all build commands. target, config/autogen options, make options """
    pass
  def showkey(self):
    """ Debug show our passed in key.  Third party uses this as the main name """
    print("The key is "+self.key)
  def getKey(self):
    """ Get the key for this builder """
    return self.key
  def checkRequirements(self):
    """ return false if requirements not met """
    return True
  def makeInstall(self, makeflags):
    """ Do the stock make and make install in a build """
    b.run("make "+makeflags)
    b.run("make install")

class BuilderGroup:
  """ Build a logical group of packages, such as hydro or third party or severe """
  def __init__(self):
    self.myBuilders = []
    self.myBuild = True
  def setBuild(self, flag):
    """ Set if we want to build or not """
    self.myBuild = flag
  def getBuild(self):
    """ Get if we want to build or not """
    return self.myBuild
  def removeBuilder(self, key):
    """ Remove builder with given key name """
    newlist = []
    for build in self.myBuilders:
       aKey = build.getKey()
       if (aKey == key):
         #print "Removing builder " +key + " from builder list"
         pass
       else:
         newlist.append(build)
    self.myBuilders = newlist

  def listBuilders(self):
    """ List all builder keys """
    for build in self.myBuilders:
      print "Builder: "+build.getKey()
  def checkRequirements(self):
    """ Check requirements for this builder. """
    req = True
    for build in self.myBuilders:
       req = req & build.checkRequirements()
    return req
  def checkout(self, target, password):
    pass
  def build(self, target):
    pass
