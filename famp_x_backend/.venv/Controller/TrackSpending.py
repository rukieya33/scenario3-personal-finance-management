class TrackSpending:
    _onbudget = False
    _income = 0.00
    _cost = 0.00
    _budget = 0.00
    _totalCostVarying = 0.00
    _totalCostFixed = 0.00
    _remainingincometospend = 0.00 
    def __init__(self, cost, income, budget):
        self._income = int(income)
        self._cost = cost
        self._budget = float(budget)

    def getIncome(self):
        return self._income
    
    def getTotalCost(self, cost):
        print(cost)
   
        self._totalCostVarying = cost
        return self._totalCostVarying
        
    def calculateIfOffBudget(self,totalcost, remainingincometospend, budget):

       if budget < totalcost:
           
           self._onbudget = True
         
       elif totalcost <= budget:
           self._onbudget = False
    
       
       return self._onbudget
   
    def calculateMoneyLeft(self,moneysaved, income):
  
        if moneysaved > 0:
            return self._remainingincometospend
        else:
            return moneysaved
       
    
    def calculateIncomeDeduction(self, income, totalcost):
        
           self._remainingincometospend = totalcost - income
        
           return self._remainingincometospend
        