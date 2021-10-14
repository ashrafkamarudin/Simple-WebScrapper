import csv
from src import progresss

Progress = progresss.Progress

class File:
    name            = ""
    column_closure  = {} # Dictionary
    contents        = [] # List
    currentContent  = 0 # int

    def open(self, config):
        urls = [] # init list
        with open(self.name, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                urls.append(row[config["column_name"]])
                line_count += 1
            print(f'Processed {line_count} lines.')
        return urls;

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def setContents(self, contents):
        self.contents = contents

    def appendColumn(self, columnName, closure):
        self.column_closure[columnName] = closure

    def write(self):
        columns = self.column_closure.keys()
        rowOfValues  = []
        progress = Progress(len(self.contents))

        for content in self.contents:
            values = []
            for column in columns:
                values.append(self.column_closure[column](content))
            rowOfValues.append(values)
            progress.cont()
            progress.print('Rows')

        with open(self.name, mode='w') as file:
            pl_writer = csv.writer(file)
            pl_writer.writerow(list(columns))

            for values in rowOfValues:
                pl_writer.writerow(list(values))