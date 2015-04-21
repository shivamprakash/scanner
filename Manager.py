import tldextract

class URLManager:
  urlList = []
  domain = ""
  index = 0
  def __init__(self, url):
    self.urlList.append(url)
    URLManager.domain = self.getDomainName(url)
    
  def getURL(self):
    if(self.index < len(self.urlList)):
      url = self.urlList[self.index]
      self.index += 1
      return url
    else:
      return "end"


  def putURL(self,url):
    if(self.checkInDomain(url)):
      self.urlList.append(url)  
    
    
  def getDomainName(self,url):
    return tldextract.extract(url).domain

  @staticmethod
  def checkInDomain(url):
    if url == URLManager.domain:
      return True
    else:
      return False

    