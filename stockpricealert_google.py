from googlefinance import getQuotes
import json
import time

#function to get only the price of a company as a float

def get_price(number):
    parsed = json.loads((json.dumps(getQuotes(number))))
    string = str(parsed[0][u'LastTradeWithCurrency'])
    price = float(string.strip('HK$'))
    return price

#print the prices of the companies I'm interested in

# print get_price('HKG:0388') #hkex
# print get_price('HKG:0001')  #CKG
# print get_price('HKG:2800')  #hktracker
# print get_price('HKG:0005')  #hsbc

#check prices for all companies, pause for an hour, then check again

for i in range(8):
    if get_price('HKG:0388') >= 270 or get_price('HKG:0388') <= 160:
        print "HKEX is now worth $%d a share" %(get_price('HKG:0388'))
    else:
        print "No big change in the price of HKEX"
        
    if get_price('HKG:0001') >= 150 or get_price('HKG:0001') <= 97:
        print "CKH is now worth $%d a share" %(get_price('HKG:0001'))
    else:
        print "No big change in the price of CKH"
        
    if get_price('HKG:2800') >= 30 or get_price('HKG:2800') <= 22:
        print "HK Tracker is now worth $%d a share" %(get_price('HKG:2800'))
    else:
        print "No big change in the price of HK Tracker"
        
    if get_price('HKG:0005') >= 80 or get_price('HKG:0005') <= 50:
        print "HSBC is now worth $%d a share" %(get_price('HKG:0005'))
    else:
        print "No big change in the price of HSBC"

    time.sleep(3600)