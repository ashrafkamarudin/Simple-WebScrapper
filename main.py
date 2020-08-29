
import re, requests, csv, array
from bs4 import BeautifulSoup

class Crawler:

    scrappedItems = []

    def setUrlToCrawl(self, list):
        self.urls = list

    def crawl(self):
        for url in self.urls:
            request=requests.get(url)
            self.scrappedItems.append(ScrappedPageStruct(
                url = url,
                content = request.content
            ))

class ScrappedPageStruct:
    url = ""
    domain = ""
    content = ""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.setDomainFromUrl()

    def setDomainFromUrl(self):
        temp = self.url
        temp=temp.replace('http://www.', '')
        temp=temp.replace('https://www.', '')
        temp=temp.replace('http://', '')
        temp=temp.replace('https://', '')

        domain= re.split(r"\b/", temp, 1)
        self.domain = domain[0]

class File:

    column_closure = {} # Dictionary
    contents = [] # String
    currentContent = 0 # int

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def setContents(self, contents):
        self.contents = contents

    def appendColumn(self, columnName, closure):
        self.column_closure[columnName] = closure

    def write(self):
        columns = self.column_closure.keys()
        rowOfValues  = []

        for content in self.contents:
            values = []
            for column in columns:
                values.append(self.column_closure[column](content))
            rowOfValues.append(values)

        with open(self.name, mode='w') as file:
            pl_writer = csv.writer(file)
            pl_writer.writerow(list(columns))

            print(list(columns))

            for values in rowOfValues:
                print(list(values))
                pl_writer.writerow(list(values))

crawler = Crawler()
crawler.setUrlToCrawl([
    "http://www.everyoneweb.com/zamzam12345/", 
    "http://www.everyoneweb.com/zamzam12345/"
])

crawler.crawl()

def firstColumn():
    def nested(ScrappedPageStruct):
        return ScrappedPageStruct.url
    return nested

def calc(column):
    def nested(ScrappedPageStruct):
        content_bs = BeautifulSoup(ScrappedPageStruct.content, 'html.parser').prettify()
        return content_bs.count("escape(")
    return nested

def urlLenght():
    def nested(ScrappedPageStruct):
        length=len(ScrappedPageStruct.url)
        if length < 54:
            statusLength ="benign"
        else:
            statusLength ="malicious"

        return statusLength
    return nested

def ipAddress():
    def nested(ScrappedPageStruct):
        domain = ScrappedPageStruct.domain
        ip=list(range(1,257))
        cds=domain.count(".")

        if cds == 3:
            ip1= re.split(r"\.", domain, 1)
            ip2= re.split(r"\.", ip1[1], 1)
            ip3= re.split(r"\.", ip2[1], 1)

            try:
                if int(ip1[0]) in ip:
                    if int(ip2[0]) in ip:
                        if int(ip3[0]) in ip:
                            if int(ip3[1]) in ip:
                                ipAddress="found"
                                ipStatus="malicious"
                            else:
                                ipAddress = "not found"
                                ipStatus = "benign"
                        else:
                            ipAddress = "not found"
                            ipStatus = "benign"
                    else:
                        ipAddress = "not found"
                        ipStatus = "benign"
                else:
                    ipAddress = "not found"
                    ipStatus = "benign"

            except:
                ipAddress = "not found"
                ipStatus = "benign"

        else:
            ipAddress = "not found"
            ipStatus = "benign"
        
        return "%s. Url is %s"%(ipAddress, ipStatus)
    return nested

firstColumn     = firstColumn()
calcEscape      = calc("escape(")
calcUnescape    = calc("unescape(")
urlLenght       = urlLenght()
ipAddress       = ipAddress()

file = File(name = "test.csv")
file.setContents(crawler.scrappedItems)

# First Column
file.appendColumn("URLLLLLLL", firstColumn)

#1 Count on Script
file.appendColumn("escape()", calcEscape)
file.appendColumn("unescape()", calcUnescape)

#2 URL Length
file.appendColumn("The length of url", urlLenght)

#3 IP Address
file.appendColumn("IP Address", ipAddress)

#4 Special Characters


file.write()