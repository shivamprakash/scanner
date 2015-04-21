from Manager import URLManager
obj = URLManager("http://stackoverflow.com/questions/9626535/get-domain-name-from-url")

obj.putURL("http://127.0.0.1:5000/user/register")
print obj.getURL()
print obj.getURL()