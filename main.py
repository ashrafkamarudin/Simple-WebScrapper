import csv, sys, config, sys
from src import log, scrapper, file

# Begin Operation
# load src
config      = config.config
File        = file.File
Scrapper    = scrapper.Scrapper

# Init file
file = File(name = config['write_to'])

# Append Columnd
for key, value in config['column_to_append'].items():
    file.appendColumn(key, value)

# load urls
urls = File(name = config['read_from']['name']).open({
    "column_name": config['read_from']['column'] # Column Name for the urls
})


# lazy attempt in making cli args
args = sys.argv
args.pop(0)

thread_count = config['number_of_thread']
for arg in args:
    if "--thread=" in arg:
        thread_count =  int(arg.replace("--thread=", ''))

# Begin Scrapping
scrapper = Scrapper(urls)
scrapper.setThreadCount(thread_count)
scrapper.work()

# Set Scrapped Result to File Content
file.setContents(scrapper.scrappedItems)

# Write To File
print("\nWriting to file ...")
file.write()
print("\nDumping Log to file ...")

fullPath = config['logs']['path'] + config['logs']['name']
with open(fullPath, 'a+') as f:
    f.writelines(str(log.dump()))
    f.close()

print("Operation finished")
