"""
load Storage()
load share_file
analyze file/ store in Storage:
    1.Durchlauf b_pattern + length
    for f in range(length):
        extend p_pattern
    store p_pattern in Storage

"""
from statistics import mean
import itertools as it
from time import gmtime, strftime
import re
import sys
import copy
from prepareData import prepare_data
from account import Account
from data import Data


def vergleich3(b_pattern, s_pattern, sell_length, verlauf, prices):
    data = Data()
    pattern = b_pattern  + s_pattern
    #print(pattern)
    account = Account(data)
    strt = 0
    # print(verlauf.find(pattern, strt))
    while verlauf.find(pattern, strt) >= 0:
        account('buy', prices[2][verlauf.count(",", 0, verlauf.find(pattern, strt) + len(b_pattern)) - 1])
        strt = verlauf.find(pattern, strt) + len(b_pattern)
        account('sell', prices[3][verlauf.count(",", 0, strt) - 2 + sell_length])
        account.data.b_pattern = b_pattern
        account.data.s_pattern = s_pattern
    return account
# +++++++++++++++++++++++++++++++++ end of function vergleich ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def generate_dat2(array, nr_elements=None,sell_length = 2):
    verlauf, array = prepare_data(array)
    if nr_elements is None:
        nr_elements = [0, 1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -4, -5, -6, -7]
    ergebnisse = []


    alles2 = list(it.product(nr_elements, repeat=7))
    for g in alles2:
        k = str(g)[1:-1]
        k += ","
        account = vergleich3(k, "", sell_length, verlauf, array)
        account.data.b_pattern = k
        ergebnisse.append(account)

    p_patterns = analyze_dat(ergebnisse)
    while sell_length >0:
        ergebnisse = extend_p_patterns(p_patterns, verlauf, array, sell_length)
        p_patterns = analyze_dat(ergebnisse)
        sell_length -=1

    print("p_patterns2:")
    for f in p_patterns:
        print(" buy", f.data.b_pattern ,"sell", f.data.s_pattern)

def analyze_dat(ergebnisse):
    i = 0
    p_patterns = []
    for x in ergebnisse:
        try:
            winrate = float(1 - ( x.data.transactions - x.data.successful_transac )/ x.data.transactions)
        except:
            winrate = 10000
        if winrate >= 0 and x.data.b_pattern:
            p_patterns.append(x)
        i += 1
    return p_patterns

def extend_p_patterns(p_pattern, verlauf, array,sell_length, nr_elements=None):
    if nr_elements is None:
        nr_elements = [0, 1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -4, -5, -6, -7]

    ergebnisse = []
    alles = list(it.product(nr_elements, repeat=1))
    for x in p_pattern:
        for j in alles:
            l = str(j)[1:-1]
            data = Data()
            data.s_pattern = copy.copy(x.data.s_pattern) + " " + l
            #print(x.data.b_pattern)
            ergebnisse.append(vergleich3(x.data.b_pattern, data.s_pattern, sell_length, verlauf, array))

    return ergebnisse
data = Data()
array = [[],[],[1, 1, 2, 3, 4, 1, 1, 2, 3, 4, 1],[1, 1, 2, 3, 4, 1, 1, 2, 3, 4, 1]]
generate_dat2(array)