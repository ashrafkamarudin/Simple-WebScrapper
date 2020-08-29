from classes.scrapper import Scrapper, ScrappedPageStruct
from classes.file import File
from columnClosure import *

scrapper = Scrapper([
    "http://www.everyoneweb.com/zamzam12345/", 
    "http://www.everyoneweb.com/zamzam12345/"
])
scrapper.scrap()

# Register Closure
firstColumn     = firstColumn()
calcEscape      = calc("escape(")
calcUnescape    = calc("unescape(")
urlLenght       = urlLenght()
ipAddress       = ipAddress()
sc              = countSpecialCharacterInUrl(["?", "-", "_", "=", "%"])

file = File(name = "test.csv")
file.setContents(scrapper.scrappedItems)

# First Column
file.appendColumn("URL", firstColumn)

#1 Count on Script
file.appendColumn("escape()", calcEscape)
file.appendColumn("unescape()", calcUnescape)

#2 URL Length
file.appendColumn("The length of url", urlLenght)

#3 IP Address
file.appendColumn("IP Address", ipAddress)

#4 Special Characters
file.appendColumn("Special Character Count", sc)

# Write To File
file.write()