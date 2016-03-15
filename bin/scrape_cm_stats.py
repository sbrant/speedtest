from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://192.168.100.1/cmSignalData.htm")
bsObj = BeautifulSoup(html.read(), 'html.parser')
# print(bsObj("center"))

for sibling in bsObj.find("table").tr.next_siblings:
    print(sibling)
