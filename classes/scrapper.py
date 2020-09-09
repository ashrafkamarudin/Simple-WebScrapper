
import re, requests, numpy, threading
from classes.progresss import Progress

class Scrapper:
    scrappedItems = []
    threadCount = 5

    def __init__(self, urls):
        self.urls = urls
        self.progress = Progress(len(urls))

    def setThreadCount(self, count):
        self.threadCount = count

    def scrap(self, urls, worker):
        failedUrls = []
        for url in urls:
            # print ("Worker #", worker, " scrapping url ", url)
            self.progress.cont()
            try:
                request=requests.get(url)
                self.progress.print(" Scrapped :min url out of :max")

                self.scrappedItems.append(ScrappedPageStruct(
                    url = url,
                    status_code = request.status_code,
                    content = request.content
                ))
            except Exception as e:
                failedUrls.append(url)
                self.progress.print(" Skipped " + url)

        self.failedUrls = failedUrls

    def work(self):
        threads = []
        self.splittedUrls = numpy.array_split(numpy.array(self.urls), self.threadCount)
        print("thread count ", self.threadCount)
        for i in range(self.threadCount):
            t = threading.Thread(
                target=self.scrap, 
                args=(self.splittedUrls[i], i)
            )
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()
                

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