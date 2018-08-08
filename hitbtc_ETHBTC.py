
import time, json, requests, datetime, pytz

import sqlite3



## SECTION 1: Request.get JSON from server API


## HITBTC
def hitbtcETHBTCbidP():
    hitbtcETHBTCTickbidP = requests.get('https://api.hitbtc.com/api/2/public/candles/ETHBTC?period=M3&limit=35')
    #print(binanceBTCUSDTTickbidP.json())
    p35 = hitbtcETHBTCTickbidP.json()[0]['close']
    p34 = hitbtcETHBTCTickbidP.json()[1]['close']
    p33 = hitbtcETHBTCTickbidP.json()[2]['close']
    p32 = hitbtcETHBTCTickbidP.json()[3]['close']
    p31 = hitbtcETHBTCTickbidP.json()[4]['close']
    p30 = hitbtcETHBTCTickbidP.json()[5]['close']
    p29 = hitbtcETHBTCTickbidP.json()[6]['close']
    p28 = hitbtcETHBTCTickbidP.json()[7]['close']
    p27 = hitbtcETHBTCTickbidP.json()[8]['close']
    p26 = hitbtcETHBTCTickbidP.json()[9]['close']
    p25 = hitbtcETHBTCTickbidP.json()[10]['close']
    p24 = hitbtcETHBTCTickbidP.json()[11]['close']
    p23 = hitbtcETHBTCTickbidP.json()[12]['close']
    p22 = hitbtcETHBTCTickbidP.json()[13]['close']
    p21 = hitbtcETHBTCTickbidP.json()[14]['close']
    p20 = hitbtcETHBTCTickbidP.json()[15]['close']
    p19 = hitbtcETHBTCTickbidP.json()[16]['close']
    p18 = hitbtcETHBTCTickbidP.json()[17]['close']
    p17 = hitbtcETHBTCTickbidP.json()[18]['close']
    p16 = hitbtcETHBTCTickbidP.json()[19]['close']
    p15 = hitbtcETHBTCTickbidP.json()[20]['close']
    p14 = hitbtcETHBTCTickbidP.json()[21]['close']
    p13 = hitbtcETHBTCTickbidP.json()[22]['close']
    p12 = hitbtcETHBTCTickbidP.json()[23]['close']
    p11 = hitbtcETHBTCTickbidP.json()[24]['close']
    p10 = hitbtcETHBTCTickbidP.json()[25]['close']
    p9 = hitbtcETHBTCTickbidP.json()[26]['close']
    p8 = hitbtcETHBTCTickbidP.json()[27]['close']
    p7 = hitbtcETHBTCTickbidP.json()[28]['close']
    p6 = hitbtcETHBTCTickbidP.json()[29]['close']
    p5 = hitbtcETHBTCTickbidP.json()[30]['close']
    p4 = hitbtcETHBTCTickbidP.json()[31]['close']
    p3 = hitbtcETHBTCTickbidP.json()[32]['close']
    p2 = hitbtcETHBTCTickbidP.json()[33]['close']
    p1 = hitbtcETHBTCTickbidP.json()[34]['close']
    return p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35


def run():

    # Connection to db

    conn = sqlite3.connect('base.db')
    # Create table
    c = conn.cursor()
    # Init script

    # Get last entry 
    entry = None
    for row in c.execute('select * from transac where date = (select max(date) from transac) and currency = "ETHBTC" and market = "HITBTC"'):
        entry = row

    if entry == None:
        buying=True
        entryPrice=None
        exitPrice=None
        cycle=None
    elif entry[1]=="BUY":
        buying=False
        entryPrice=entry[2]
        exitPrice=None
        cycle=entry[3]
    else:
        buying=True
        entryPrice=None
        exitPrice=entry[2]
        cycle=None
        
    ## SECTION 2: Get Value
    while True:

        try:
            
                    
            a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35 = hitbtcETHBTCbidP()
            n1 = float(a1)
            n2 = float(a2)
            n3 = float(a3)
            n4 = float(a4)
            n5 = float(a5)
            n6 = float(a6)
            n7 = float(a7)
            n8 = float(a8)
            n9 = float(a9)
            n10 = float(a10)
            n11 = float(a11)
            n12 = float(a12)
            n13 = float(a13)
            n14 = float(a14)
            n15 = float(a15)
            n16 = float(a16)
            n17 = float(a17)
            n18 = float(a18)
            n19 = float(a19)
            n20 = float(a20)
            n21 = float(a21)
            n22 = float(a22)
            n23 = float(a23)
            n24 = float(a24)
            n25 = float(a25)
            n26 = float(a26)
            n27 = float(a27)
            n28 = float(a28)
            n29 = float(a29)
            n30 = float(a30)
            n31 = float(a31)
            n32 = float(a32)
            n33 = float(a33)
            n34 = float(a34)
            n35 = float(a35)
            SMA7 = (n1 + n2 + n3 + n4 + n5 + n6 + n7) / 7
            SMA7b = (n2 + n3 + n4 + n5 + n6 + n7 + n8) / 7
            SMA7c = (n3 + n4 + n5 + n6 + n7 + n8 + n9) / 7
            EMAmultiplier7 = 2 / (7 + 1)
            EMAmultiplier25 = 2 / (25 + 1)
            SMA7_initial = (n19 + n20 + n21 + n22 + n23 + n24 + n25) / 7
            EMA7_18 = ((n18 - SMA7_initial) * EMAmultiplier7) + SMA7_initial
            EMA7_17 = ((n17 - EMA7_18) * EMAmultiplier7) + EMA7_18
            EMA7_16 = ((n16 - EMA7_17) * EMAmultiplier7) + EMA7_17
            EMA7_15 = ((n15 - EMA7_16) * EMAmultiplier7) + EMA7_16
            EMA7_14 = ((n14 - EMA7_15) * EMAmultiplier7) + EMA7_15
            EMA7_13 = ((n13 - EMA7_14) * EMAmultiplier7) + EMA7_14
            EMA7_12 = ((n12 - EMA7_13) * EMAmultiplier7) + EMA7_13
            EMA7_11 = ((n11 - EMA7_12) * EMAmultiplier7) + EMA7_12
            EMA7_10 = ((n10 - EMA7_11) * EMAmultiplier7) + EMA7_11
            EMA7_9 = ((n9 - EMA7_10) * EMAmultiplier7) + EMA7_10
            EMA7_8 = ((n8 - EMA7_9) * EMAmultiplier7) + EMA7_9
            EMA7_7 = ((n7 - EMA7_8) * EMAmultiplier7) + EMA7_8
            EMA7_6 = ((n6 - EMA7_7) * EMAmultiplier7) + EMA7_7
            EMA7_5 = ((n5 - EMA7_6) * EMAmultiplier7) + EMA7_6
            EMA7_4 = ((n4 - EMA7_5) * EMAmultiplier7) + EMA7_5
            EMA7_3 = ((n3 - EMA7_4) * EMAmultiplier7) + EMA7_4
            EMA7_2 = ((n2 - EMA7_3) * EMAmultiplier7) + EMA7_3
            EMA7_1 = ((n1 - EMA7_2) * EMAmultiplier7) + EMA7_2

            SMA25_initial = (n11 + n12 + n13 + n14 + n15 + n16 + n17 + n18 + n19 + n20 + n21 + n22 + n23 + n24 + n25 + n26 + n27 + n28 + n29 + n30 + n31 + n32 + n33 + n34 + n35) / 25
            EMA25_10 = ((n10 - SMA25_initial) * EMAmultiplier25) + SMA25_initial
            EMA25_9 = ((n9 - EMA25_10) * EMAmultiplier25) + EMA25_10
            EMA25_8 = ((n8 - EMA25_9) * EMAmultiplier25) + EMA25_9
            EMA25_7 = ((n7 - EMA25_8) * EMAmultiplier25) + EMA25_8
            EMA25_6 = ((n6 - EMA25_7) * EMAmultiplier25) + EMA25_7
            EMA25_5 = ((n5 - EMA25_6) * EMAmultiplier25) + EMA25_6
            EMA25_4 = ((n4 - EMA25_5) * EMAmultiplier25) + EMA25_5
            EMA25_3 = ((n3 - EMA25_4) * EMAmultiplier25) + EMA25_4
            EMA25_2 = ((n2 - EMA25_3) * EMAmultiplier25) + EMA25_3
            EMA25_1 = ((n1 - EMA25_2) * EMAmultiplier25) + EMA25_2

            #EMA25previous
            diffEMA7SMA7 = EMA7_1 - SMA7
            diffEMA7EMA25 = EMA7_1 - EMA25_1
            diffSMA7EMA25 = SMA7 - EMA25_1
            EMA7Slope = EMA7_1 - EMA7_2
            SMA7Slope = SMA7 - SMA7b
            EMA25Slope = EMA25_1 - EMA25_2
            diffEMA7_10SMA7_10 = EMA7_10 - EMA25_10

            print("MARKET: ETHBTC")

        ##SECTION 3: PRINT AND DO CALCULATIONS

            print("n1 =", n1)
            print("n2 =", n2)
            print("SMA7 =", SMA7)
            print("EMA7 =", EMA7_1)
            print("EMA25 =", EMA25_1)
            print("EMA7 - SMA7 =", diffEMA7SMA7)
            print("EMA7 - EMA25 =", diffEMA7EMA25)
            print("SMA7 - EMA25 =", diffSMA7EMA25)
            print()
            print("EMA Slope (EMA7 - EMA7b) =", EMA7Slope)
            print()
            print("SMA Slope (SMA7 - SMA7b) =", SMA7Slope)
            print()

    ##### SCENARIO 1
            
            if(buying):
                if(exitPrice==None):
                    exitPrice=n2
                print("n1 =", n1)
                print("n2 =", n2)
                print("Exit Price =", exitPrice)
                if diffEMA7SMA7 > 0:
                    print("Buy Signal 1 (EMA7 higher than SMA7) -> EMA7 above SMA7")
                    print("n1/n2 (criteria < 0.9996) =", n1/n2)
                    print("n1/exitPrice (criteria < 0.9996) =", n1/exitPrice)
                else:
                    print("Buy Signal 1 (EMA7 higher than SMA7) -> EMA7 below SMA7")
                    print("n1/n2 (criteria < 0.9993 =", n1/n2)
                    print("n1/exitPrice (criteria < 0.9993) =", n1/exitPrice)
        
                #f EMA7Slope > 0:
                #       print("Buy Signal 2 (EMA7 Slope) -> OK")
                #else:
                #       print("Buy Signal 2 (EMA7 Slope) -> Dont Buy")
        
                #if SMA7Slope > 0:
                #       print("Buy Signal 3 (SMA7 Slope) -> OK")
                #else:
                #       print("Buy Signal 3 (SMA7 Slope) -> Dont Buy")
        
                #if EMA25Slope > 0:
                #       print("Buy Signal 4 (EMA25 Slope) -> OK")
                #else:
                #       print("Buy Signal 4 (EMA25 Slope) -> Dont Buy")
        
                #if EMA7Slope > SMA7Slope:
                #       print("Buy Signal 5 (EMA increasing slope over SMA) -> OK")
                #else:
                #       print("Buy Signal 5 (EMA increasing slope over SMA) -> Dont Buy")
        
                if (diffEMA7SMA7 > 0 and ((n1/n2 < 0.9996 and exitPrice/n2 < 0.9993) or n1/exitPrice < 0.9996)) or (diffEMA7SMA7 < 0 and ((n1/n2 < 0.9993 and exitPrice/n2 < 0.9990) or n1/exitPrice < 0.9993)):

                    # Insert a row of data
                    c.execute('''INSERT INTO cycle
                                 (rowid, profit) values (null, -100)''')
                    cycle=c.lastrowid

                    now = datetime.datetime.now(pytz.timezone('Etc/GMT-8'))

                    c.execute("INSERT INTO transac VALUES ('%s','BUY','%s','%s','ETHBTC','HITBTC')" % (now.strftime("%Y-%m-%d %H:%M:%S"),n1,cycle))
                    
                    # Save (commit) the changes
                    conn.commit()
                    print("BUY NOW AT =", n1)
                    buying=False
                    entryPrice=n1
        
        # "BUY NOW AT = n1 in line 186 is supposed to be recorded as "entry price" to be used by SCENARIO 2 in successive run; achieving this value will also trigger scenario 2 to run instead of scenario 1"

            else:

    ##### SCENARIO 2
                # Replace n2 with the recorded entryPrice
                z1=entryPrice
                print("Entry Price =", z1)
                print("n1 =", n1)
                print("n2 =", n2)
                print()
                print("n1/entryPrice =", n1/z1)
                
                if diffEMA7SMA7 > 0 and EMA7Slope > 0:
                    print("Criteria: n1/z1 >= 1.0004 or n1/z1 <= 0.9985")
                if diffEMA7SMA7 > 0 and EMA7Slope < 0:
                    print("Criteria: n1/z1 >= 1.0002 or n1/z1 <= 0.9997")
                if diffEMA7SMA7 < 0 and EMA7Slope > 0:
                    print("Criteria: n1/z1 >= 1.0002 or n1/z1 <= 0.9995")
                if diffEMA7SMA7 < 0 and EMA7Slope < 0:
                    print("Criteria: n1/z1 >= 1.0002 or n1/z1 <= 0.9997")
                
                #if EMA7Slope < SMA7Slope:
                #    print("Sell Signal 1 (EMA decreasing slope over SMA) -> Sell Now")
                #else:
                #    print("Sell Signal 1 (EMA decreasing slope over SMA) -> Dont Sell Yet")
        
                if EMA7Slope > 0:
                    print("Sell Signal 2 (EMA7 Slope) -> EMA7 Positive Slope")
                else:
                    print("Sell Signal 2 (EMA7 Slope) -> EMA7 Negative Slope")
        
                if diffEMA7SMA7 > 0:
                    print("Sell Signal 3 (if EMA7 > SMA7) -> EMA7 is above SMA7")
                else:
                    print("Sell Signal 3 (if EMA7 > SMA7) -> EMA7 is below SMA7")
        
                if (diffEMA7SMA7 > 0 and (n1/z1 >= 1.0002 or n1/z1 <= 0.9997)) or (diffEMA7SMA7 > 0 and (n1/z1 >= 1.0002 or n1/z1 <= 0.9997)):
                    c.execute('''UPDATE cycle SET
                                 profit='%s' WHERE rowid = '%s' ''' % (((n1*100.0)/entryPrice)-100,cycle))
                    

                    now = datetime.datetime.now(pytz.timezone('Etc/GMT-8'))

                    c.execute("INSERT INTO transac VALUES ('%s','SELL','%s','%s','ETHBTC','HITBTC')" % (now.strftime("%Y-%m-%d %H:%M:%S"),n1,cycle))
                
                    
                    # Save (commit) the changes
                    conn.commit()
                    entryPrice=None
                    cycle=None
                    print("SELL NOW AT =", n1)
                    profit = (n1*100.00/z1) - 100
                    print("Profit =", profit,"%")
                    buying=True
                    exitPrice=n1
                    # Reset
                    entryPrice=None
                    

    # variable "n2" in line 210 should be the "entry price" recorded in previous run by SCENARIO 1
    # "SELL NOW AT = n1 in line 186 is supposed to be recorded as "exit price", achieving this value will also trigger scenario 1 to run again instead of scenario 1"


    #        print("Difference between Coinex and Bibox BuyPrice =",coinexBTCUSDTlivebidP - biboxBTCUSDTlivebidP)
        
            now = datetime.datetime.now(pytz.timezone('Etc/GMT-8'))
            print("Iteration : ")
            print(now.strftime("%Y-%m-%d %H:%M:%S"))

            print(); 
            print("--------------------------"); 
            print()

        except:
            print("Something is wrong with a request - Retrying...")
            now = datetime.datetime.now()
            print("Iteration : ")
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            pass
        time.sleep(7) # 120 equals two minutes, you can ping it every second by putting a 1 in here

run()