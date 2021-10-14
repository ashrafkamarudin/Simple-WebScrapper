import re
import requests
from bs4 import BeautifulSoup

def firstColumn():
    def nested(ScrappedPageStruct):
        return ScrappedPageStruct.url
    return nested

def calc(column):
    def nested(ScrappedPageStruct):
        content_bs = BeautifulSoup(ScrappedPageStruct.content, 'html.parser').prettify()
        return content_bs.count(column)
    return nested

def getUrlLenght():
    def nested(ScrappedPageStruct):
        return len(ScrappedPageStruct.url)
    return nested

def urlLenghtStatus():
    def nested(ScrappedPageStruct):
        lenght = getUrlLenght()(ScrappedPageStruct)
        status = ''

        if lenght < 54: status = 'benign'
        elif lenght >= 54 and lenght <= 75: status = 'suspicious'
        else: status = 'malicious'

        return status 
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

def specialCharacterExist(characters):
    def nested(ScrappedPageStruct):
        return 'exist' if countSpecialCharacterInUrl(characters)(ScrappedPageStruct) > 0 else 'not exist'
    return nested

def countSpecialCharacterInUrl(characters):
    def nested(ScrappedPageStruct):
        total = 0
        for character in characters:
            total+= ScrappedPageStruct.url.count(character)
        return total
    return nested

def commentStyle():
    def nested(ScrappedPageStruct):
        content_bs = BeautifulSoup(ScrappedPageStruct.content, 'html.parser').prettify()
        if ScrappedPageStruct.status_code == 200:
            
            match_cs = re.search(r'//-->', content_bs)
            if match_cs:
                commentStatus="malicious"
            else:
                commentStatus = "benign"

            return commentStatus
    return nested

def IPExistInUrl():
    def nested(ScrappedPageStruct):
        status = ''
        if (re.search(r'http://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/.*', ScrappedPageStruct.url)):
            status = 'malicious'
        else:
            status = 'benign'
        
        return status
    return nested;

def existenceSubDomains():
    def nested(ScrappedPageStruct):
        status = 'benign'
        if ScrappedPageStruct.url.count(".") >= 3: status = 'malicious'

        return status
    return nested;

def AliasSymbolExistInUrl():
    def nested(ScrappedPageStruct):
        status = 'legitimate'
        if ScrappedPageStruct.url.count(".") >= 1: status = 'phishing'

        return status
    return nested;

def getDomainAge(url):
    request = requests.get("https://input.payapi.io/v1/api/fraud/domain/age/" + url)

    if hasattr(request, 'result'): return request.result 
    else: return None

def AgeOfDomainStatus():
    def nested(ScrappedPageStruct):
        status = 'phishing'
        age = getDomainAge(ScrappedPageStruct.domain)
        if age != None and age > 365: status = 'legitimate'

        return status
    return nested;

def urlRedirectedUsing(char):
    def nested(ScrappedPageStruct):
        firstOccurance = ScrappedPageStruct.url.find(char)
        secondOccurance = ScrappedPageStruct.url.find(char, firstOccurance+1)
        
        return 'Phishing' if (secondOccurance > 7) else 'Legitimate'
    return nested;