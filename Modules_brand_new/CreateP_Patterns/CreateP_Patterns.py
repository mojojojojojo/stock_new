from Modules_brand_new.CreateP_Patterns.PSettings import PSettings
import itertools as it
from Modules_brand_new.account import Account
from Modules_brand_new.Data import Data
import copy
from prepareData import prepare_data
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
            if f.data.transactions != 0:
                if  f.data.revenue_in_percent >=  self.p_settings.revenueThresh:
                    p_patterns.append(f)
                    print("asdwad")
        print("p_patterns",p_patterns)
        return p_patterns

    def findPatterns(self, b_pattern, s_pattern, verlauf, prices):
        data = Data()
        pattern = b_pattern + s_pattern
        #print(pattern)
        account = Account(data)
        strt = 0
        flag = False
        #print(verlauf.find(pattern, strt))
        while verlauf.find(pattern, strt) >= 0:
            #print("nom")
            #print(verlauf.find(pattern, strt), " pattern : " , pattern)
            strt = verlauf.find(pattern, strt) + len(b_pattern)
            account('buy', prices[1][verlauf.count(",", 0, strt) - 1])
            #print(strt)
            account('sell', prices[2][verlauf.count(",", 0, strt) - 2 + self.p_settings.s_lenMax])
            account.data.b_pattern = b_pattern
            #print(b_pattern)
            account.data.s_pattern = s_pattern
            flag = True
        if flag:
            return account




    def extend_b_patterns(self, preis, array):

        ergebnisse = []

        i = 0
        for x in self.p_patterns:
            alles = list(it.product(self.p_settings.nr_elements, repeat=1))
            for j in alles:
                l = str(j)[1:-1]
                data = Data()
                data.s_pattern = copy.copy(x.data.s_pattern)
                data.b_pattern = copy.copy(x.data.b_pattern) + l + " "
                f = self.findPatterns(data.b_pattern,data.s_pattern,verlauf, preis)
                if f :
                    ergebnisse.append(f)
                    print(data.b_pattern , data.s_pattern)

        self.p_patterns = self.verifyP_Patterns(ergebnisse)


prices = [[1,2,3,4,5,3,1,4,5,2,5,2,8,1,1,1,1,1,1,1,1], [1,2,3,4,5,3,1,4,5,2,5,2,8,1,1,1,1,1,1,1,1],[1,2,3,4,5,3,1,4,5,2,5,2,8,1,1,1,1,1,1,1,1],[1,2,3,4,5,3,1,4,5,2,5,2,8,1,1,1,1,1,1,1,1]]
p_patterns = P_Patterns()
verlauf, prices = prepare_data(prices, p_patterns.p_settings.max_stg)

for i in range(1):
    p_patterns.extend_b_patterns(prices, verlauf)

for f in p_patterns.p_patterns:
    print(f.data.b_pattern,"||",f.data.s_pattern, "\t revenue -->", round(f.data.revenue_in_percent,1),"winrate -->", f.data.winrate())