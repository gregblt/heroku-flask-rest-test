from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
import json
import pytz
import sqlite3
import datetime

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
auth = HTTPBasicAuth()

users = {
    "john": "hello",
    "susan": "bye"
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

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

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