
import re, requests
from classes.progresss import Progress

class Scrapper:
    scrappedItems = []

    def __init__(self, urls):
        self.urls = urls
        self.progress = Progress(len(urls))
        self.scrap()

    def scrap(self):
        failedUrls = []
        for url in self.urls:
            self.progress.cont()
            try:
                request=requests.get(url)
                self.progress.print(" Scrapped :min url out of :max")
            except Exception as e:
                failedUrls.append(url)
                self.progress.print(" Skipped " + url)

            self.scrappedItems.append(ScrappedPageStruct(
                url = url,
                status_code = request.status_code,
                content = request.content
            ))
        self.failedUrls = failedUrls
                

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