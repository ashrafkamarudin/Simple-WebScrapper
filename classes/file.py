import csv

class File:
    name            = ""
    column_closure  = {} # Dictionary
    contents        = [] # String
    currentContent  = 0 # int

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def setContents(self, contents):
        self.contents = contents

    def appendColumn(self, columnName, closure):
        self.column_closure[columnName] = closure

    def write(self):
        columns = self.column_closure.keys()
        rowOfValues  = []

        for content in self.contents:
            values = []
            for column in columns:
                values.append(self.column_closure[column](content))
            rowOfValues.append(values)

        with open(self.name, mode='w') as file:
            pl_writer = csv.writer(file)
            pl_writer.writerow(list(columns))

            print(list(columns))

            for values in rowOfValues:
                print(list(values))
                pl_writer.writerow(list(values))