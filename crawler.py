# import re
# from array import array
import mechanize
from urllib2 import HTTPError
from Manager import URLManager
# from bs4 import BeautifulSoup as BS

urlList = []
br = mechanize.Browser()
obj = URLManager("http://stackoverflow.com/")
# Browser options
# Ignore robots.txt. Do not do this without thought and consideration.
br.set_handle_robots(False)

# Don't add Referer (sic) header
br.set_handle_referer(False)

# Don't handle Refresh re directions
br.set_handle_refresh(False)


def printForms():
    for form in br.forms():
        print "Form name: %s" % form.name
        # print form
        for control in form.controls:
            print "Type = %s" % control.type
            print "Name = %s" % control.name
        print "\n"

def crawlUrls():
    for link in br.links():
        #print link
        if not link.url.startswith("http"):
            if link.url != '/' and link.url != '#':
                obj.putURL(link.url)
                #print link
                urlList.append(link.url)
            # res = br.open(link.url)
            # http_message = res.info()
            # if http_message.maintype == 'text':
            #     print br.response().read()
    

def crawlNewPages(objccr):
    for url in urlList:
        try:
            br.open(url)
            # res = br.open(url)
            # http_message = res.info()
            # if http_message.maintype == 'text':
            # print br.response().read()
            # crawlUrls()
            printForms()
        except HTTPError, e:
            print "Error code", e.code

def init():
    
    
    curr_url = obj.getURL()
    while (curr_url != "end"):
        print curr_url
        br.open(curr_url)
        crawlUrls()
        print curr_url
        curr_url = obj.getURL()
        

    #printForms()


# response = br.response().read()
# Getting the response in beautifulsoup
# soup = BS(response)

# print urlList
# myList = sorted(set(urlList))
# print myList

# for product in soup.find_all('a'):
#     #printing product name and url
#     print "Product Name : %s" % product.get('href')
#     print "======================="


init()
#crawlNewPages()
