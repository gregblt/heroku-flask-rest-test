from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
import json
import pytz
import sqlite3
import datetime

import ftplib
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger



app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
auth = HTTPBasicAuth()



import subprocess
subprocess.Popen(["python","hitbtc_ETHBTC.py"])

def job_function():
    session = ftplib.FTP('tradefinest.com','zk46dbnj','Zaq1mlp0')
    file = open('./base.db','rb')                  # file to send
    session.storbinary('STOR /etc/tradefinest.com/base_'+datetime.datetime.now(pytz.timezone('Etc/GMT-8')).strftime("%Y-%m-%d_%H:%M:%S")+".db",
     file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=job_function,
    trigger=IntervalTrigger(minutes=5),
    id='printing_job',
    name='Print date and time every five seconds',
    replace_existing=True)

users = {
    "admin": "admin"
}



def getMarketData():
    yest = (datetime.datetime.now(pytz.timezone('Etc/GMT-8'))- datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    conn = sqlite3.connect('base.db')
    # Create table
    c = conn.cursor()
    
    # last day profit
    x=c.execute('''select profit from cycle where rowid in 
              (select cycle from transac 
              where date BETWEEN '%s 00:00:00' AND '%s 23:59:59' and type = 'BUY' and currency = "ETHBTC" and market = "HITBTC") ''' % (yest,yest))
    
    profits=[]
    for row in x:
        profits.append(row[0])
        
    sum1=sum(profits)
    
    last30=(datetime.datetime.strptime(yest,"%Y-%m-%d")- datetime.timedelta(days=30)).strftime("%Y-%m-%d")
    # last 30 day profit
    x=c.execute('''select profit from cycle where rowid in 
              (select cycle from transac 
              where date BETWEEN '%s 00:00:00' AND '%s 23:59:59' and type = 'BUY' and currency = "ETHBTC" and market = "HITBTC") ''' % (last30,yest))
    
    profits30=[]
    for row in x:
        profits30.append(row[0])
        
    if(len(profits30)==0):
        avg30=0
    else:
        avg30=sum(profits30) / float(len(profits30))  
        
    sum30=sum(profits30)
    
    c.close()
    
    return {'sum1':round(sum1, 2),
            'sum30':round(sum30, 2),
            'avg30':round(avg30, 2)}

# @app.before_first_request
# def activate_job():
#     import subprocess
#     subprocess.Popen(["python","hitbtc_ETHBTC.py"])

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/api/v1/history')
def history():
    # Get parames
    site = request.args.get('site')
    market = request.args.get('market')
    date = request.args.get('date')

    if site==None or market==None:
        response = jsonify({'message': "Exhange site and Market are mandatory"})
        response.status_code = 400
        return response

    if date==None:
        date=(datetime.datetime.now(pytz.timezone('Etc/GMT-8'))- datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    
    conn = sqlite3.connect('base.db')
    # Create table
    c = conn.cursor()
        
    # Get the cycles for this day
    x=c.execute('''select rowid, profit from cycle where rowid in 
              (select cycle from transac 
              where date BETWEEN '%s 00:00:00' AND '%s 23:59:59' and type = 'BUY' and currency = "ETHBTC" and market = "HITBTC" ) ORDER BY rowid desc ''' % (date,date))
    
    cycles=[]
    cycle_id=c.rowcount
    for row in x:
        #print(row)
        t={"id":cycle_id,"profit":round(row[1],2),'buy':{},'sell':{}}
        cycle_id-=1
        
        # GET BUY
        c2 = conn.cursor()
        for row2 in c2.execute('''select * from transac where cycle = %s and type = 'BUY' ''' % (row[0])):
            t['buy']={'date':row2[0],'price':row2[2]}
        for row2 in c2.execute('''select * from transac where cycle = %s and type = 'SELL' ''' % (row[0])):
            t['sell']={'date':row2[0],'price':row2[2]}
            
        cycles.append(t)
        
        c2.close()
        
    c.close()
    
    response = app.response_class(
        response=json.dumps(cycles),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/api/v1/summary')
def hello_world():
    # Compute the data for the index page
    data={'HITBTC':{'ETHBTC':None}}
    data['HITBTC']['ETHBTC']=getMarketData()

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/api/v1/realtime/data')
@auth.login_required
def realtime_data():
    # Get parames
    site = request.args.get('site')
    market = request.args.get('market')
    lastTime = request.args.get('start')

    if site==None or market==None:
        response = jsonify({'message': "Exhange site and Market are mandatory"})
        response.status_code = 400
        return response

    date=datetime.datetime.now(pytz.timezone('Etc/GMT-8')).strftime("%Y-%m-%d")
    
    conn = sqlite3.connect('base.db')
    # Create table
    c = conn.cursor()
        
    # Get the cycles for this day
    x=c.execute('''select rowid, profit from cycle where rowid in 
              (select cycle from transac 
              where date BETWEEN '%s %s' AND '%s 23:59:59' and type = 'BUY' and currency = "ETHBTC" and market = "HITBTC" ) ORDER BY rowid desc ''' % (date,lastTime,date))
    
    cycles=[]
    cycle_id=c.rowcount
    for row in x:
        #print(row)
        t={"id":cycle_id,"profit":round(row[1],2),'buy':{},'sell':{}}
        
        # GET BUY
        c2 = conn.cursor()
        for row2 in c2.execute('''select * from transac where cycle = %s and type = 'BUY' ''' % (row[0])):
            t['buy']={'date':row2[0],'price':row2[2]}
        for row2 in c2.execute('''select * from transac where cycle = %s and type = 'SELL' ''' % (row[0])):
            t['sell']={'date':row2[0],'price':row2[2]}
            
        cycles.append(t)
        
        c2.close()

        cycle_id-=1
        
    c.close()
    
    response = app.response_class(
        response=json.dumps(cycles),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/')
@auth.login_required
def index():
    response = app.response_class(
        response=json.dumps({"username":auth.username()}),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run()