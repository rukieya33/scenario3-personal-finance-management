class ManageInvestment:
    _currentAsset = 0
    _age = 0
    _stock = 0
    _bonds = 0
    _cash = 0
    def __init__(self, currentAssets, age):
        self._currentAsset = currentAssets
        self._age = age
     

    def getAge(self):
        return self._age
    def calculateStockPercent(self, age):
       asset = 100 - int(age)
       self._stock = asset / 100

       
       return self._stock
   
    def calculateBondsPercent(self, age):
        
        remainingAsset = int(age)/100
         
        self._bonds = (remainingAsset * int(self._currentAsset)) - (66 - int(age))
        bondspercent = self._bonds / 100
        
        return  bondspercent
    
    def calculateCashPercent(self, age):
         
        self._cash = (66 - int(age)) / 100
    
        return self._cash
       
    
   