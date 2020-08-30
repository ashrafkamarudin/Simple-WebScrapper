from classes.scrapper import Scrapper, ScrappedPageStruct
from classes.file import File
from columnClosure import *

scrapper = Scrapper([
    "http://www.everyoneweb.com/zamzam12345/", 
    "http://www.rupor.info"
])
scrapper.scrap()

file = File(name = "test.csv")
file.setContents(scrapper.scrappedItems)

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
file.appendColumn("fromCharCode()"       , calc("fromCharCode("))
file.appendColumn("exec()"              , calc("exec("))
file.appendColumn("setInterval()"       , calc("setInterval("))
file.appendColumn("setTimeout()"        , calc("setTimeout("))
file.appendColumn("<iframe>"             , calc("<iframe"))
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

# Write To File
file.write()