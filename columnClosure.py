from bs4 import BeautifulSoup

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


def countSpecialCharacterInUrl(characters):
    def nested(ScrappedPageStruct):
        total = 0
        for character in characters:
            total+= ScrappedPageStruct.url.count(character)
        return total
    return nested