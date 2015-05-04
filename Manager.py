from collections import deque
from ConfigParser import SafeConfigParser
import pickle
import tldextract
import hashlib
import mechanize
from urllib2 import urlopen
from urlparse import urlparse
class URLManager:
  CONST_SIZE = 0
  urlList = deque()
  fileList = deque()
  urlVisitedHash = []
  domain = ""
  index = 0
  fileName =""
  def __init__(self, url):
    parser = SafeConfigParser()
    parser.read('config.ini')
    URLManager.domain = self.getDomainName(url)
    self.putURL(url)
    self.fileName = parser.get('Manager', 'fileName')
    self.CONST_SIZE = parser.get('Manager', 'list_capacity')
    self.fileList = deque(maxlen = int(self.CONST_SIZE))
    
    
  def getURL(self):
    if(len(self.urlList) > 0):
      url = self.urlList.pop()
      if( len(self.fileList) < self.CONST_SIZE):
        self.fileList.append(url)
      else:
        self.appendToFile()
      return url
    else:
      self.appendToFile()
      return "end"


  def putURL(self,url):
    #print url
    url = self.removeExtra(url)
    if(self.checkInDomain(url) and not self.alreadyParsed(url)):
      self.urlList.append(url)

      
  

  def appendToFile(self):
    foDest = open( self.fileName, "a")
    for item in self.fileList:
      foDest.write("%s\n" % item)
    self.fileList.clear()
      

  def removeFalseURL(self,url):
    self.urlList.remove(url)
    

  def removeExtra(self,url):
    o = urlparse(url)
    url = o[0] + "://" + o[1] + o[2]
    return url

  def is_html(self,url):
    # try:
    #print url
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_referer(False)
    br.set_handle_refresh(False)
    res = br.open(url)
    http_message = res.info()
    print http_message
    if 'content-type' in http_message and 'text/html' in http_message["content-type"]:
        return True
    return False
    # except (mechanize.HTTPError, mechanize.URLError):
    #   print mechanize.HTTPError

  def getDomainName(self,url):
    return tldextract.extract(url).domain

 
  def checkInDomain(self,url):
    if self.getDomainName(url) == URLManager.domain:
      return True
    else:
      return False

  def alreadyParsed(self,url):
    hashValue = hashlib.md5(url).hexdigest() 
    if hashValue in self.urlVisitedHash:
      return True
    else:
      self.urlVisitedHash.append(hashValue)
      return False
