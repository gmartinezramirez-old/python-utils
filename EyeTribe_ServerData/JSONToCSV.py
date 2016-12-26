#!/usr/bin/env python2

import csv
import json


def writeToCsvHeader(filename):
    filenameCsv=filename+".csv"
    with open(filenameCsv, 'wb') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=';')
        csvWriter.writerow(["TS", "TIME", "X", "Y"])

def writeToCsvFile(filename, ts, time, x, y):
    filenameCsv=filename+".csv"
    with open(filenameCsv, 'ab') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=';')
        csvWriter.writerow([ts,time, x, y])

def printValues(filename,x,y,time,timestamp):
    print filename
    print x
    print y
    print time
    print timestamp

#TODO(gmartinezramirez): Refactor and do shorter method.
def main():
    JSONfile = raw_input("Name of the JSON file to process: ")

    with open(JSONfile) as JSON_file:
        writeToCsvHeader(JSON_file)
        for line in JSON_file:
            JSON_data = json.loads(line)
            if JSON_data["category"] == "tracker":
                ts = JSON_data["values"]["frame"]["timestamp"]
                time = JSON_data["values"]["frame"]["time"]
                x = JSON_data["values"]["frame"]["avg"]["x"]
                y = JSON_data["values"]["frame"]["avg"]["y"]                
                #DEBUG: Print the values readed in the JSON_file
                #printValues(filename,x,y,time,ts)
                writeToCsvFile(filename, ts, time, x, y)

if __name__ == '__main__':
    main()
