from ast import Yield
import csv
from selectors import SelectorKey
import datetime as dt
from datetime import datetime

class SPAC:
    def __init__(self, symbol=None, symbolIss=None, category=None, exsPrice=None, twentyAvg=None, close=None, shell=None):
        self.symbolW = symbol
        self.symbolI = symbolIss
        self.exsPrice = exsPrice
        self.twentyAvg = twentyAvg
        self.close = close
        self.category = category
        self.shell = shell


def getSpac():

    listofSpac = []

    with open('List of Stock Warrants.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter= ',')
        line_count = 0
        for row in csv_reader:
            node = SPAC()
            if line_count == 0:
                line_count += 1
            else:
                for i in range(len(row)):
                    if i == 0:
                        node.symbolW = row[i]
                    if i == 3:
                        node.exsPrice = float(row[i].replace('$',''))
                    
                    if i == 7:
                        node.twentyAvg = float(row[i].replace(',',''))

                    if i == 4:
                        node.close = float(row[i].replace('$',''))
                    
                    if i == 2:
                        if "Shell" in row[i]:
                            node.shell = True

                    if i == 8:
                        node.symbolI = row[i]

                listofSpac.append(node)
    return listofSpac

listOfWar = getSpac()