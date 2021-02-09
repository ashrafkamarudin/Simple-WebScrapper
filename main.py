import csv, sys, config, sys
from src import log, scrapper, file

# Begin Operation
# load src and config files
config      = config.config
File        = file.File
Scrapper    = scrapper.Scrapper

# lazy attempt in making cli args
args = sys.argv
args.pop(0)

thread_count = config['number_of_thread']
write_to     = config['write_to']
for arg in args:
    if "--thread=" in arg:
        thread_input = arg.replace("--thread=", '')
        if thread_input == "max":
            thread_count =  thread_input
        else:
            thread_count = int(arg.replace("--thread=", ''))

    if "--writeto=" in arg:
        write_to =  arg.replace("--writeto=", '')

# Init file
file = File(name = write_to)

# Append Columnd
for key, value in config['column_to_append'].items():
    file.appendColumn(key, value)

# load urls
urls = File(name = config['read_from']['name']).open({
    "column_name": config['read_from']['column'] # Column Name for the urls
})

# Begin Scrapping
scrapper = Scrapper(urls)
scrapper.setThreadCount(thread_count)
scrapper.work()

# Set Scrapped Result to File Content
file.setContents(scrapper.scrappedItems)

# Write To File
print("\nWriting to file", write_to , "... ( This may take awhile )")
file.write()
print("Dumping Log to file ...")

fullPath = config['logs']['path'] + config['logs']['name']
with open(fullPath, 'a+') as f:
    f.writelines(str(log.dump()))
    f.close()

print("Operation finished")
