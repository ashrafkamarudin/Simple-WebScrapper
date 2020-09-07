
import re, requests, numpy, threading

class Scrapper:
    scrappedItems = []

    def __init__(self, urls):
        self.urls = urls
        self.splittedUrls = numpy.array_split(numpy.array(urls), 5)
        print(self.splittedUrls)
        self.work()

    def scrap(self, urls, worker):
        failedUrls = []
        for url in self.urls:
            print ("Worker #", worker, " scrapping url ", url)
            try:
                request=requests.get(url)
            except Exception as e:
                failedUrls.append(url)

            self.scrappedItems.append(ScrappedPageStruct(
                url = url,
                status_code = request.status_code,
                content = request.content
            ))
        self.failedUrls = failedUrls

    def work(self):
        threads = []
        for i in range(5):
            t = threading.Thread(
                target=self.scrap, 
                args=(self.splittedUrls[i], i)
            )
            threads.append(t)
            t.start()
                

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