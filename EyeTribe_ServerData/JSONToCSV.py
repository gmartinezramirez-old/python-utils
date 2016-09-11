# -*- coding: cp1252 -*-
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

def printValues(filename,x,y,time,ts):
    print filename
    print x
    print y
    print time
    print ts

def main():
    #Ingresar nombre del archivo json a procesar
    #filename="19"
    filename = raw_input("Ingrese nombre del archivo JSON a procesar, sin la extensión .json: ")

    with open(filename+".json") as file:
        writeToCsvHeader(filename)
        for line in file:
            json_data = json.loads(line)
            if (json_data["category"]=="tracker"):
                ts = json_data["values"]["frame"]["timestamp"]
                time = json_data["values"]["frame"]["time"]
                x = json_data["values"]["frame"]["avg"]["x"]
                y = json_data["values"]["frame"]["avg"]["y"]
                #printValues(filename,x,y,time,ts) #Descomentar solo si se quiere ver el output de procesamiento
                writeToCsvFile(filename, ts, time, x, y)

if __name__ == "__main__":
    main()
