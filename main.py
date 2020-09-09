import csv
from classes.scrapper import Scrapper, ScrappedPageStruct
from classes.file import File
from columnClosure import *

# Default Configurations #
config = {
    # File to be written to
    'write_to': 'test.csv',

    # File to read from and which column
    'read_from': {
        'name': 'urls.csv',
        'column': 'A'
    },

    # Number of threads or worker. 
    # The higher it is, The faster the script will run
    'number_of_thread': 150,

    'column_to_append': {

        # First Column
        'URL'                       : firstColumn(),

        # #1 Count on Script
        'escape()'                  : calc("escape("),
        'unescape()'                : calc("unescape("),
        'eval()'                    : calc("eval("),
        'search()'                  : calc("search("),
        'charAt()'                  : calc("charAt("),
        'charCodeAt()'              : calc("charCodeAt("),
        'Concat()'                  : calc("Concat("),
        'indexOf()'                 : calc("indexOf("),
        'substring()'               : calc("substring("),
        'replace()'                 : calc("replace("),
        'Split()'                   : calc("Split("),
        'toString()'                : calc("toString("),
        'document.write()'          : calc("document.write("),
        'Window.location()'         : calc("Window.location("),
        'Document.cookie'           : calc("Document.cookie"),
        'fromCharCode()'            : calc("fromCharCode("),
        'exec()'                    : calc("exec("),
        'setInterval()'             : calc("setInterval("),
        'setTimeout()'              : calc("setTimeout("),
        '<iframe>'                  : calc("<iframe"),
        '<a>'                       : calc("<a"),
        'onload()'                  : calc("onload("),
        'onerror'                   : calc("onerror"),
        'onunload'                  : calc("onunload"),
        'onmouseover'               : calc("onmouseover"),
        'onbeforeunload'            : calc("onbeforeunload"),
        'addEventListener()'        : calc("addEventListener("),
        'attachEvent()'             : calc("attachEvent("),
        'dispatchEvent()'           : calc("dispatchEvent("),

        # #2 URL Length
        'URL Length'                : urlLenght(),

        # #3 IP Address
        'IP Address'                : ipAddress(),

        # #4 Special Characters
        'Special Character Count'   : countSpecialCharacterInUrl(["?", "-", "_", "=", "%"]),

        # #5 Commenting Style
        'Commenting Style'          : commentStyle()
    }
}

# Begin Operation
# Init file
file = File(name = config['write_to'])

# Append Columnd
for key, value in config['column_to_append'].items():
    file.appendColumn(key, value)

# load urls
urls = File(name = config['read_from']['name']).open({
    "column_name": config['read_from']['column'] # Column Name for the urls
})

# Begin Scrapping
scrapper = Scrapper(urls)
scrapper.setThreadCount(config['number_of_thread'])
scrapper.work()

# Set Scrapped Result to File Content
file.setContents(scrapper.scrappedItems)

# Write To File
print("Writing to file ...")
file.write()
print("Operation finished")