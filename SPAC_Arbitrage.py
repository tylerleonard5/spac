from ast import Yield
import csv
from selectors import SelectorKey
import datetime as dt
from datetime import datetime

class SPAC:
    def __init__(self, symbol=None, symbolIss=None, category=None, exsPrice=None, close=None, closeIss=None, twentyAvg=None, type=None):
        self.symbol = symbol
        self.symbolIss = symbolIss
        self.category = category
        self.exsPrice = exsPrice
        self.close = close
        self.closeIss = closeIss
        self.twentyAvg = twentyAvg
        self.type = type
    
def yearToDay(date):
    date_format = "%m/%d/%Y"
    a = datetime.strptime(date, date_format)
    return a
    


def yieldToAvg(price, todayDate, IPOdate):
    today = yearToDay(todayDate)
    IPO = yearToDay(IPOdate)

    diff = ((today - IPO).days)

    return ((10.0/price) - 1) / (((-(diff)) + 155.0) / 360.0) * 100.0

def yieldToDeadline(price, todayDate, targDate):
    today = yearToDay(todayDate)
    targ = yearToDay(targDate)

    diff = ((targ - today).days)

    return ((10.0/price) - 1) / ((((diff))) / 360.0) * 100.0

def yieldToEffective(price):
    return ((10.0/price) - 1) * 100.0



listofSpac = []

with open('SPAC_ArbitrageExcel.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',')
    line_count = 0
    for row in csv_reader:
        node = SPAC()
        if line_count == 0:
            line_count += 1
        else:
            for i in range(len(row)):
                if i == 0:
                    node.symbol = row[i]
                if i == 2:
                    node.category = row[i]
                if i == 3:
                    node.exsPrice = float(row[i].replace('$',''))
                if i == 5:
                    node.closeIss = float(row[i].replace('$',''))
                if i == 4:
                    node.close = float(row[i].replace('$',''))
                if i == 7:
                    node.twentyAvg = float(row[i].replace(',',''))
                if i == 8:
                    node.symbolIss = row[i]
                if i == 10:
                    node.type = row[i]

            listofSpac.append(node)

for i in listofSpac:
    today = dt.date.today()
    todayStr = str(today.month) +"/" + str(today.day) +"/" + str(today.year)

    print("Symbol: ", i.symbol)
    print("Issuer Symbol: ", i.symbolIss)
    print("Category: ", i.category)
    print("Type: ", i.type)
    print("Exercise Price: ", i.exsPrice)
    print("Last Close: ", i.close)
    print("Issuer Last Close Price: ", i.closeIss)
    print("20 Day Average: ", i.twentyAvg)
    #print("Yield to Average: ", yieldToAvg(i.close, todayStr, i.date))
    #print("Yield to Deadline: ", yieldToDeadline(i.close, todayStr, i.expr))
    #print("Yield to Effective: ", yieldToEffective(i.close))
    print("\n")