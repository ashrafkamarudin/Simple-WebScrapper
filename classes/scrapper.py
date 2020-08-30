
import re, requests

class Scrapper:
    scrappedItems = []

    def __init__(self, urls):
        self.urls = urls
        self.scrap()

    def scrap(self):
        for url in self.urls:
            request=requests.get(url)
            self.scrappedItems.append(ScrappedPageStruct(
                url = url,
                status_code = request.status_code,
                content = request.content
            ))

class ScrappedPageStruct:
    url         = ""
    domain      = ""
    content     = ""
    status_code = ""

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