"""
storage.data_patterns[x]  -> x = sell_len





"""

import os
import sys
sys.path.insert(0, os.getcwd())

import copy
from Modules_brand_new.Data import Data


class Storage () :


    def __init__ (self,share_name):
        self.data_patterns  = [[]] # length s_pattern[patterns], length b_pattern[patterns]
        self.connected_share = share_name

    def update_data_pattern(self,data):
        k= 0
        while len(self.data_patterns) <= data.s_len():
            self.data_patterns.append([])
            #print("len(self.data_patterns)", len(self.data_patterns))

        for f in self.data_patterns[data.s_len()]:
            if f.b_pattern == data.b_pattern and f.s_pattern == data.s_pattern:
                self.data_patterns[data.s_len()].insert(self.data_patterns[data.s_len()].index(f),copy.copy(data))
                self.data_patterns[data.s_len()].remove(f)
                #print("changed")
                k = 1
        if(k is 0):
            self.data_patterns[data.s_len()].append(copy.copy(data))
            #print("added")

    def get_relevant_buy_data(self, buy_len):
        array = []
        for f in self.data_patterns:
            for g in f:
                if g.b_len() == buy_len:
                    array.append(g)
        return array


    def get_relevant_sell_data(self, sell_len, b_pattern):
        array = []
        for f in self.data_patterns:
            for g in f:
                if g.s_len() == sell_len and g.b_pattern == b_pattern:
                    array.append(g)
        return array

    def load_format_file(self):
        self.data_patterns = [[]]
        with open(self.connected_share+".moj") as f:
            length_all = int(f.readline())
            for k in range(length_all):
                self.data_patterns.append([])
                length = int(f.readline())
                #print("length read = " + str(length))
                for x in range(length):
                    g = Data()
                    try:
                        g.revenue_in_percent = float(f.readline())
                    except:
                        g.revenue_in_percent = 0
                    # print("g.data.revenue = " + str(g.data.revenue))
                    g.b_pattern = str(f.readline()[:-1])
                    g.s_pattern = str(f.readline()[:-1])
                    try:
                        g.successful_transac = int(f.readline())
                    except:
                        g.successful_transac = 0
                    try:
                        g.transactions = int(f.readline())
                    except:
                        g.transactions = 0

                    self.data_patterns[k].append(g)
            print("file loaded")
            f.close()

    def save_format_file(self):

        with open(self.connected_share + ".moj", 'w') as f:
            f.write(str(len(self.data_patterns)) + "\n")
            for t in self.data_patterns:
                f.write(str(len(t)) + "\n")
                for x in t:
                    f.write(str(x.revenue_in_percent) + "\n")
                    f.write(str(x.b_pattern) + "\n")
                    f.write(str(x.s_pattern) + "\n")
                    f.write(str(x.successful_transac) + "\n")
                    f.write(str(x.transactions) + "\n")
        print("file saved")
        f.close()