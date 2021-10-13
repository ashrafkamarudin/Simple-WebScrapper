
import re, requests, numpy, threading
from src import log, progresss
from urllib3.util.retry import Retry
from requests.packages.urllib3.exceptions import InsecureRequestWarning

Progress = progresss.Progress
requests.adapters.DEFAULT_RETRIES = 1
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Scrapper:
    scrappedItems = []
    threadCount = 5
    sess = ""
    timeout = "none"

    def __init__(self, urls, timeout):
        self.urls = urls
        self.progress = Progress(len(urls))
        self.sess = requests.Session()
        self.timeout = timeout

    def setThreadCount(self, count):
        self.threadCount = count

    def scrap(self, urls, worker):
        failedUrls = []
        for url in urls:
            # print ("Worker #", worker, " scrapping url ", url)
            try:
                request=self.sess.get(url,verify=False, timeout=self.timeout)

                self.scrappedItems.append(ScrappedPageStruct(
                    url = url,
                    status_code = request.status_code,
                    content = request.content
                ))
            except requests.exceptions.RequestException as e:
                log.addLog(e)
                failedUrls.append(url)
                # print(str(e))
            self.progress.cont()
            self.progress.print()

        self.failedUrls = failedUrls

    def setConnectionPool(self, count):
        retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[ 500, 502, 503, 504 ],
                raise_on_status=False)

        print(count)
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=200, 
            pool_maxsize=200,
            max_retries=retries,
            pool_block=True
        )
        self.sess.mount('', adapter)

    def work(self):
        threads = []

        if str(self.threadCount) == "max":
            self.threadCount = len(self.urls)
        else:
            if int(self.threadCount) > len(self.urls):
                self.threadCount = len(self.urls)

        self.setConnectionPool(self.threadCount)
        self.splittedUrls = numpy.array_split(numpy.array(self.urls), self.threadCount)
        print("Worker count ", self.threadCount)
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