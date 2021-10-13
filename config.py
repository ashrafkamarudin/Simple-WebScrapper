from functions import *

# Default Configurations #
config = {
    # File to be written to
    'write_to': 'test.csv',

    # File to read from and which column
    'read_from': {
        'name': 'urls.csv',
        'column': 'A'
    },

    'logs': {
        'path': 'logs/',
        'name': 'scrapper.log'
    },

    # Number of threads or worker. 
    # The higher it is, The faster the script will run
    'number_of_thread': 50,

    # Timeout for trying to get each url
    'timeout': 10,

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