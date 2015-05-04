from Form import URL

url = "http://adamdoupe.com//blog/archives"
urlObj = URL(url)
forms = urlObj.getForms()
for form in forms:
  print form.getName()
  for elem in form.getElements():
    print elem["Name"]
    print elem["Type"]
