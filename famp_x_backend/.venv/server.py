
import array
import json
from Controller.TrackSpending import TrackSpending
from Controller.ManageInvestment import ManageInvestment
import random

from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin


from rethinkdb import RethinkDB
r = RethinkDB()

app = Flask(__name__)
 

app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

myarray = []

     


 
# sanity check route

@app.route('/registration', methods=['POST','GET'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def register():
  try:
    conn = r.connect(host='127.0.0.1',
                 port=28015,
                 db='personal_finance_management_db')
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    email = request.form.get('email')

        
    r.table('register').insert({ 'first': first_name, 'last': last_name, 'email': email}).run(conn)
    return "currentPerson"
  except:
     
    return "Error on registering user"
   


@app.route('/setBudget', methods=['POST','GET'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def setBudget():
  try:
    conn = r.connect(host='127.0.0.1',
                 port=28015,
                 db='personal_finance_management_db')
    

    data =  request.get_json()


    ids = r.table('setBudget').insert({'datas' : data.get('data')}, return_changes=True).run(conn)
   
    print(ids)
    

    return jsonify({'id' : ids})
  except:

    return jsonify({'error' : 'error setting Budget'})
    



@app.route('/track-spending', methods=['POST','GET'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def trackSpending():
    conn = r.connect(host='127.0.0.1',
                            port=28015,
                            db='personal_finance_management_db')
    
            
    try:
      if request.method == "GET":
       
    

            budgets = r.table('setBudget').values().run(conn)
      
    
            
            print(budgets)
            return budgets
      
    except:
          return jsonify({'error' : 'error getting budget'}) 
  
    else:
        try:
            data = request.get_json()
        
            trackSpending = TrackSpending(data.get('cost'),data.get('totalbudget'), data.get('totalincome'))
            
           
            totalcost = trackSpending.getTotalCost(data.get('cost'))
            income = trackSpending.getIncome()
            remainingincometospend = trackSpending.calculateIncomeDeduction(income, data.get('totalbudget'))
            onbudget = trackSpending.calculateIfOffBudget(totalcost, remainingincometospend, data.get('totalbudget'))
            moneyLeft = trackSpending.calculateMoneyLeft(data.get('moneysaved'), remainingincometospend)
            
            r.table('track_spending').insert({'cost' : data.get('cost'),
                                      'totalbudget':data.get('totalbudget'),
                                      'totalincome': data.get('totalincome'),
                                      'moneysaved': moneyLeft,
                                      'expensemonth' : data.get('expensemonth'),
                                      'off_or_on_budget': onbudget}).run(conn)
           
            if onbudget:
               return jsonify({"messages" : "You are off budget manage your expenses now to get you back on track" })
            else:
                
                return jsonify({"messages" : "Great You are on budget! Keep up the good work on your personal finance management."})
    
        except RuntimeError():
               return jsonify({"message" : RuntimeError.with_traceback})
 
@app.route('/visual-overview', methods=['POST','GET'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def displayVisualOverview():
  

      
      conn = r.connect(host='127.0.0.1',
                      port=28015,
                      db='personal_finance_management_db')
      cost = r.table("track_spending").get_field("cost").run(conn)
      expensemonth = r.table("track_spending").get_field("expensemonth").run(conn)
      totalincome = r.table("track_spending").get_field("totalincome").run(conn)
      offbudget = r.table("track_spending").get_field('off_or_on_budget').run(conn)
      moneysaved = r.table("track_spending").get_field('moneysaved').run(conn)
      totalbudget = r.table("track_spending").get_field('totalbudget').run(conn)
      
      currentAssets = r.table("manage_investment").get_field("currentAssets").run(conn)
      age = r.table("manage_investment").get_field("age").run(conn)
      
      ages = str(age).replace("rethinkdb.net.DefaultCursor (done streaming):" , "").replace('[', '').replace(']', '').replace(',', '').replace("'", '').split(" ")[1]
  
      manageInvestment = ManageInvestment(str(currentAssets).replace("rethinkdb.net.DefaultCursor (done streaming):" , "").replace('[', '').replace(']', '').replace(',', '').replace("'", '').split(" ")[1], ages)
      print(ages)
      ages = manageInvestment.getAge()
    
        
      stock = manageInvestment.calculateStockPercent(ages)  * 100
  
      bonds = manageInvestment.calculateBondsPercent(ages) * 100
  
      cash = manageInvestment.calculateCashPercent(ages) * 100
      return json.dumps({"cost" : str(cost).replace("rethinkdb.net.DefaultCursor (done streaming):" , ""),
                     "expensemonth" : str(expensemonth).replace("rethinkdb.net.DefaultCursor (done streaming):" , ""),
                     "totalincome" : str(totalincome).replace("rethinkdb.net.DefaultCursor (done streaming):" , ""),
                     "offbudget" : str(offbudget).replace("rethinkdb.net.DefaultCursor (done streaming):" , ""),
                     "moneysaved" : str(moneysaved).replace("rethinkdb.net.DefaultCursor (done streaming):" , ""),
                     "totalbudget" : str(totalbudget).replace("rethinkdb.net.DefaultCursor (done streaming):" , ""),
                     "stock" : str(stock).replace("rethinkdb.net.DefaultCursor (done streaming):" , ""),
                     "bonds" : str(bonds).replace("rethinkdb.net.DefaultCursor (done streaming):" , ""),
                     "cash" : str(cash).replace("rethinkdb.net.DefaultCursor (done streaming):" , ""),
                     
                  })

    

@app.route('/manage_investment', methods=['POST','GET'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def manageInvestment():

      if request.method == "GET":
          conn = r.connect(host='127.0.0.1',
                                port=28015,
                                db='personal_finance_management_db')
          data = r.table('manage_investment').insert([{"companyname" : "TD ltd","companysize" : "50 - 249 employees","currentratio" : 4.9, "qualityrating" : "4.8 star", "earningsanddividends": 2000000000,  "financialleverage" : "good"},
                                              {"companyname": "farmfoods", "companysize" : "50 - 249 employees", "currentratio" : 1.3,"qualityrating" : "2.0 star", "earningsanddividends": 1000000, "financialleverage" : "bad"},
                                              {"companyname" : "Loreal","companysize" : "50 - 500,249 employees", "qualityrating" : "4.5 star", "currentratio" : 3.0, "earningsanddividends": 10000000000, "financialleverage" : "excellent"},
                                              {"companyname" : "Ebena" ,  "companysize" : "250,000+ employees", "qualityrating" : "4.5 star", "currentratio" : 3.0, "earningsanddividends": 7000000000, "financialleverage" : "excellent"},
                                              {"companyname" : "Fineheit ltd", 
                                              "companysize" : "1000+ employees","qualityrating" : "3.0 star", "earningsanddividends": 5000000, "currentratio" : 1.0,  "financialleverage" : "bad"}], return_changes=True).run(conn)
         
          r.table("manage_investment").update({"currentAssets" : "", "age" : "", "savingsperyear": "", "marginaltaxrate" : "", "incomerequired" : "", "risktolerance" : "", "economicoutlook" : "", "isslected" : ""})
          
          return  jsonify({"stocks" : data})
       
      else:
          conn = r.connect(host='127.0.0.1',
                                port=28015,
                                db='personal_finance_management_db')
          datas = request.get_json()
          
          r.table("manage_investment").insert({"currentAssets" : datas.get('currentAssets'), "age" : datas.get('age'), "savingsperyear": datas.get("savingsperyear"), "marginaltaxrate" : datas.get('marginaltaxrate'), "incomerequired" : datas.get("incomerequired"), "risktolerance" : datas.get("risktolerance"), "economicoutlook" : datas.get("economicoutlook"), "isselected" : datas.get("selectedstock"), "companyselected" : datas.get("companyselected")}).run(conn)
        
          companyname = r.table('manage_investment').get_field("companyselected").run(conn)
          earnings =  r.table('manage_investment').get_field("earningsanddividends").run(conn)
          leverage = r.table('manage_investment').get_field("financialleverage").run(conn)
          savings =  r.table('manage_investment').get_field("savingsperyear").run(conn)
          income = r.table('manage_investment').get_field("incomerequired").run(conn)
          print(datas)
          return jsonify({"companyname" : str(companyname).replace("rethinkdb.net.DefaultCursor (done streaming):" , ""),
                     "earnings" : str(earnings).replace("rethinkdb.net.DefaultCursor (done streaming):" , ""),
                     "leverage" : str(leverage).replace("rethinkdb.net.DefaultCursor (done streaming):" , ""),
                     "savings" : str(savings).replace("rethinkdb.net.DefaultCursor (done streaming):" , ""),
                     "income" : str(income).replace("rethinkdb.net.DefaultCursor (done streaming):" , ""),
                     "m":"Assets Allocated"})
         

@app.route('/monitor_investment', methods=['POST','GET', 'PUT', 'DELETE'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def monitorInvestment():
      
  if request.method == "GET":
      conn = r.connect(host='127.0.0.1',
                                port=28015,
                                db='personal_finance_management_db')
      
     
      selectedStock = r.table("manage_investment").filter({"isselected" : "on"}).run(conn)
      
          
        
      return json.dumps({"company" : str(selectedStock).replace("rethinkdb.net.DefaultCursor (done streaming):" , "")})
      
if __name__ == '__main__':
    app.run()
