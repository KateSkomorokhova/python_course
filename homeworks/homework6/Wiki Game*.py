import re
import requests
from lxml import etree

# url1 = "https://en.wikipedia.org/wiki/Coregonus_lavaretus"
# url2 = "https://en.wikipedia.org/wiki/Freshwater_whitefish"
url1 = "https://en.wikipedia.org/wiki/Gone_Maggie_Gone"
url2 = "https://en.wikipedia.org/wiki/Theia_(planet)"
new_link = "https://en.wikipedia.org"

def find_link(url1, url2, count):
    data = requests.get(url1).text
    parser = etree.HTMLParser()
    tree = etree.fromstring(data, parser)

    for element in tree.iter("a"):
        b = str(element.get('href'))
        f = re.findall("^/wiki/(.+)", b)
        if re.findall("^/wiki/(.+)", b) != []:
            url_new = new_link+"/wiki/"+f[0]
            if url_new == url2:
                print(url1)
                print(url_new)
                print(url2)
                print()

            else:
                count += 1
                if count != 3:
                    return find_link(url_new, url2, count)

count = 0
find_link(url1, url2, count)