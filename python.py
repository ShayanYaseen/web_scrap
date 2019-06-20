from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20cards'
#connecting to webpage and grabbing the page
uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()
#html parsing
page_soup=Soup(page_html, "html.parser")

filename = "save.csv"
f = open(filename, "w")
headers = "src\n"
f.write(headers)

# grab each item
containers = page_soup.findAll("div",{"class":"item-container"})

for container in containers:
    divwithinfo = container.find("div", "item-info")
    src = divwithinfo.a.img["data-src"]
    print("Source: " + src)

    f.write(src + "\n")
    
