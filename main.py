from classes.scrapper import Scrapper, ScrappedPageStruct
from classes.file import File
from columnClosure import *

# Configurations 
urls = [ # URL to be scrapped
    "http://www.everyoneweb.com/zamzam12345/", 
    "http://www.pos-kupang.com/",
    "http://www.rupor.info",
    "http://sunlux.net/company/about.html"
]

# File for result to be written to.
file = File(name = "test.csv")

#
# Specify Column Name and Fuction to be used for that particular column
#

# First Column
file.appendColumn("URL", firstColumn())

#1 Count on Script
file.appendColumn("escape()"            , calc("escape("))
file.appendColumn("unescape()"          , calc("unescape("))
file.appendColumn("eval()"              , calc("eval("))
file.appendColumn("search()"            , calc("search("))
file.appendColumn("charAt()"            , calc("charAt("))
file.appendColumn("charCodeAt()"        , calc("charCodeAt("))
file.appendColumn("Concat()"            , calc("Concat("))
file.appendColumn("indexOf()"           , calc("indexOf("))
file.appendColumn("substring()"         , calc("substring("))
file.appendColumn("replace()"           , calc("replace("))
file.appendColumn("Split()"             , calc("Split("))
file.appendColumn("toString()"          , calc("toString("))
file.appendColumn("document.write()"    , calc("document.write("))
file.appendColumn("Window.location()"   , calc("Window.location("))
file.appendColumn("Document.cookie"     , calc("Document.cookie"))
file.appendColumn("fromCharCode()"      , calc("fromCharCode("))
file.appendColumn("exec()"              , calc("exec("))
file.appendColumn("setInterval()"       , calc("setInterval("))
file.appendColumn("setTimeout()"        , calc("setTimeout("))
file.appendColumn("<iframe>"            , calc("<iframe"))
file.appendColumn("<a>"                 , calc("<a"))
file.appendColumn("onload()"            , calc("onload("))
file.appendColumn("onerror"             , calc("onerror"))
file.appendColumn("onunload"            , calc("onunload"))
file.appendColumn("onmouseover"         , calc("onmouseover"))
file.appendColumn("onbeforeunload"      , calc("onbeforeunload"))
file.appendColumn("addEventListener()"  , calc("addEventListener("))
file.appendColumn("attachEvent()"       , calc("attachEvent("))
file.appendColumn("dispatchEvent()"     , calc("dispatchEvent("))

#2 URL Length
file.appendColumn("URL Length", urlLenght())

#3 IP Address
file.appendColumn("IP Address", ipAddress())

#4 Special Characters
file.appendColumn("Special Character Count", countSpecialCharacterInUrl(["?", "-", "_", "=", "%"]))

#5 Commenting Style
file.appendColumn("commenting style", commentStyle())

# Begin Operation
# Begin Scrapping
scrapper = Scrapper(urls)

# Set Scrapped Result to File Content
file.setContents(scrapper.scrappedItems)

# Write To File
print("Writing to file ...")
file.write()
print("Operation finished")