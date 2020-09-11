import csv, sys, time
from classes.scrapper import Scrapper, ScrappedPageStruct
from classes.file import File
from classes import log

import config

# Begin Operation
# get config
config = config.config

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
print("\nWriting to file ...")
# file.write()
print("\nDumping Log to file ...")

with open('logs/scrapper.log', 'a+') as f:
    f.writelines(str(log.dump()))
    f.close()

print("Operation finished")
