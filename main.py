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
calcEval        = calc("eval(")
calcSearch      = calc("search(")
calcCharAt      = calc("charAt(")
calcCharCodeAt  = calc("charCodeAt(")
calcConcat      = calc("Concat(")
calcIndexOf     = calc("indexOf(")
calcSubstring   = calc("substring(")
calcReplace     = calc("replace(")
calcSplit       = calc("Split(")
urlLenght       = urlLenght()
ipAddress       = ipAddress()
sc              = countSpecialCharacterInUrl(["?", "-", "_", "=", "%"])

# To Do ..
# calc("toString(", "toString()")
# calc("document.write(", "document.write()")
# calc("Window.location(", "Window.location()")
# calc("Document.cookie", "Document.cookie")
# calc("fromCharCode(", "fromCharCode()")
# calc("exec(", "exec()")
# calc("setInterval(", "setInterval()")
# calc("setTimeout(", "setTimeout()")
# calc("<iframe", "<iframe>")
# calc("<a", "<a>")
# calc("onload", "onload")
# calc("onerror", "onerror")
# calc("onunload", "onunload")
# calc("onmouseover", "onmouseover")
# calc("onbeforeunload", "onbeforeunload")
# calc("addEventListener(", "addEventListener()")
# calc("attachEvent(", "attachEvent()")
# calc("dispatchEvent(", "dispatchEvent()")

file = File(name = "test.csv")
file.setContents(scrapper.scrappedItems)

# First Column
file.appendColumn("URL", firstColumn)

#1 Count on Script
file.appendColumn("escape()", calcEscape)
file.appendColumn("unescape()", calcUnescape)

file.appendColumn("eval()", calcEval)
file.appendColumn("search()", calcSearch)
file.appendColumn("charAt()", calcCharAt)
file.appendColumn("charCodeAt()", calcCharCodeAt)
file.appendColumn("Concat()", calcConcat)
file.appendColumn("indexOf()", calcIndexOf)
file.appendColumn("substring()", calcSubstring)
file.appendColumn("replace()", calcReplace)
file.appendColumn("Split()", calcSplit)

#2 URL Length
file.appendColumn("The length of url", urlLenght)

#3 IP Address
file.appendColumn("IP Address", ipAddress)

#4 Special Characters
file.appendColumn("Special Character Count", sc)

# Write To File
file.write()