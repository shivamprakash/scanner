import tldextract
import hashlib
from urllib2 import urlopen
class URLManager:
  urlList = []
  urlVisitedHash = []
  domain = ""
  index = 0
  def __init__(self, url):
    URLManager.domain = self.getDomainName(url)
    self.putURL(url)
    
  def getURL(self):
    if(self.index < len(self.urlList) -1):
      url = self.urlList[self.index + 1]
      self.index += 1
      return url
    else:
      return "end"


  def putURL(self,url):
    if(self.checkInDomain(url) and not self.alreadyParsed(url)):
      self.urlList.append(url)  
    
 
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
