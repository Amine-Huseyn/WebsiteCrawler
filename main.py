import requests
from bs4 import BeautifulSoup

target_url = "#someurl"
foundlinks=[]

def makerequests(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def crawl(url):
    links = makerequests(url)
    for link in links.find_all("a"):
        foundlink = link.get("href")
        if foundlink :

            if "#" in foundlink:
                foundlink = foundlink.split("#")[0]
            if target_url in foundlink and foundlink not in foundlinks:
                foundlinks.append(foundlink)
                print(foundlink)
                #recursive
                crawl(foundlink)


#html parsing
crawl(target_url)











