# import re
# from array import array
import mechanize
from urllib2 import HTTPError
from Manager import URLManager
import urlparse
from urllib2 import HTTPError
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')
base_url = parser.get('Crawler', 'base_url')
br = mechanize.Browser()
obj = URLManager(base_url)
br.set_handle_robots(False)
br.set_handle_referer(False)
br.set_handle_refresh(False)

def is_absolute(url):
    return bool(urlparse.urlparse(url).netloc)

def crawlUrls():
    for link in br.links():
        #print link
        if link.url != '/' and not link.url.startswith("#") and not link.url.startswith("mailto"):
            if not is_absolute(link.url):
                obj.putURL(base_url + link.url)
            else:
                obj.putURL(link.url)
                

def is_html(res):
    http_message = res.info()
    if 'content-type' in http_message and 'text/html' in http_message["content-type"]:
        return True
    return False


def main():
    curr_url = obj.getURL()
    while curr_url != "end":
        print curr_url
        try:
            res = br.open(curr_url)
            if is_html(res):
                crawlUrls()
            curr_url = obj.getURL()
        except (mechanize.HTTPError, mechanize.URLError):
            obj.removeFalseURL(curr_url)
            curr_url = obj.getURL()

if __name__ == "__main__":
    main()
