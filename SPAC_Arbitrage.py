from ast import Yield
import csv
from selectors import SelectorKey
import datetime as dt
from datetime import datetime
import regex

class SPAC:
    def __init__(self, name=None, date=None, type=None, cap=None, close=None, expr=None):
        self.name = name
        self.date = date
        self.type = type
        self.cap = cap
        self.close = close
        self.expr = expr
    
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

with open('SPAC_Arbitrage.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',')
    line_count = 0
    for row in csv_reader:
        node = SPAC()
        if line_count == 0:
            line_count += 1
        else:
            for i in range(len(row)):
                if i == 0:
                    node.name = row[i]
                if i == 3:
                    node.date = row[i]
                if i == 2:
                    node.type = row[i]
                if i == 5:
                    node.cap = float(row[i].replace('$','').replace(',', '').replace(' ', ''))
                if i == 7:
                    node.close = float(row[i])
                if i == 9:
                    node.expr = row[i]
                if i == 6:
                    if row[i] == "N":
                        listofSpac.append(node)

for i in listofSpac:
    today = dt.date.today()
    todayStr = str(today.month) +"/" + str(today.day) +"/" + str(today.year)

    print("Symbol: ", i.name)
    print("Security Type: ", i.type)
    print("IPO Date: ", i.date)
    print("Market Cap: ", i.cap)
    print("Close: ", i.close)
    print("Expiration Date: ", i.expr)
    print("Yield to Average: ", yieldToAvg(i.close, todayStr, i.date))
    print("Yield to Deadline: ", yieldToDeadline(i.close, todayStr, i.expr))
    print("Yield to Effective: ", yieldToEffective(i.close))
    print("\n")