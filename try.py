from Manager import URLManager
obj = URLManager("http://stackoverflow.com/questions/9626535/get-domain-name-from-url")

obj.putURL("http://stackoverflow.com/questions/9849641/the-best-way-to-check-duplicated-url-in-python")
print obj.getURL()
print obj.getURL()