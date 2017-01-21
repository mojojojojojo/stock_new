from Modules_brand_new.CreateP_Patterns.PSettings import PSettings
import itertools as it
from Modules_brand_new.account import Account
from Modules_brand_new.Data import Data
import copy
from Modules_brand_new.CreateP_Patterns.prepareData import prepare_data






class P_Patterns:
    def __init__(self):
        self.p_settings = PSettings()
        self.p_patterns = []
        self.create_patterns()

    def create_basic_patterns(self,length):
        basic_pattern = list(it.product(self.p_settings.nr_elements, repeat=length))
        return basic_pattern


    def create_patterns(self):
        alles = list(it.product(self.p_settings.nr_elements, repeat=1))
        for j in alles:
                l = str(j)[1:-1]
                data = Data(s_pattern=(l + " " ))
                account = Account(data)
                self.p_patterns.append(account)


    def verifyP_Patterns(self,ergebnisse):
        p_patterns = []
        for f in ergebnisse:
            if f.data.transactions >= 1:
                if  f.data.revenue_in_percent >=  self.p_settings.revenueThresh and f.data.winrate() > 0.0:
                    p_patterns.append(f)
                    #print("asdwad")
        #print("p_patterns",p_patterns)
        return p_patterns

    def findPatterns(self, b_pattern, s_pattern, verlauf, prices):
        data = Data()
        pattern = " " + b_pattern + s_pattern
        account = Account(data)
        strt = 0
        flag = False
        while verlauf.find(pattern, strt) >= 0:
            strt = verlauf.find(pattern, strt) + len(b_pattern)
            account('buy', prices[2][verlauf.count(",", 0, strt) - 1])
            account('sell', prices[3][verlauf.count(",", 0, strt) - 2 + self.p_settings.s_lenMax])
            account.data.b_pattern = b_pattern
            account.data.s_pattern = s_pattern
            flag = True
        if flag:
            return account




    def extend_b_patterns(self, verlauf, prices):

        ergebnisse = []

        i = 0
        for x in self.p_patterns:
            alles = list(it.product(self.p_settings.nr_elements, repeat=1))
            for j in alles:
                l = str(j)[1:-1]
                data = Data()
                data.s_pattern = copy.copy(x.data.s_pattern)
                data.b_pattern =  l + " " + copy.copy(x.data.b_pattern)
                f = self.findPatterns(data.b_pattern,data.s_pattern,verlauf, prices)
                if f :
                    ergebnisse.append(f)
                    #print(data.b_pattern ,"|", data.s_pattern)

        self.p_patterns = self.verifyP_Patterns(ergebnisse)
        #self.p_patterns = ergebnisse
"""
prices = [[1,2,3,4,5,3,1,4,5,2,5,2,8,1,1,1,1,1,1,1,1], [1,2,3,4,5,3,1,4,5,2,5,2,8,1,1,1,1,1,1,1,1],[1,2,3,4,5,3,1,4,5,2,5,2,8,1,1,1,1,1,1,1,1],[1,2,3,4,5,3,1,4,5,2,5,2,8,1,1,1,1,1,1,1,1]]
p_patterns = P_Patterns()
verlauf, array = prepare_data(prices, p_patterns.p_settings.max_stg)

for i in range(1):
    p_patterns.extend_b_patterns(verlauf, array[2])

for f in p_patterns.p_patterns:
    print(f.data.b_pattern,"||",f.data.s_pattern, "\t revenue -->", round(f.data.revenue_in_percent,1),"winrate -->", f.data.winrate())
"""