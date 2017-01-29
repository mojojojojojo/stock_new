from LoadSave import open_file
import Analyze_Data.CreateP_Patterns as Cpp
from storage import Storage
x = 10



print("----"*22)
array = [[], [], [], []]
arraya = open_file("StockData/table (3).csv")
array[2] = arraya[2][0:]
array[3] = arraya[3][0:]
p_patterns = Cpp.P_Patterns(array)
storage = Storage("table (2)")
"""
#for f in p_patterns.p_patterns:
    #print(f.data.b_pattern,"||",f.data.s_pattern, "   \t revenue -->",
          #ound(f.data.revenue_in_percent,1),"winrate -->",round(f.data.winrate(),2),
          #"transactions", f.data.transactions , "sell_len" , f.data.S_len)
#print("__"*123)
for i in range(x):
    p_patterns.extend_b_patterns()

    for f in p_patterns.p_patterns:
        storage.update_data_pattern(f.data)
#storage.save_format_file()

    #f = storage.get_relevant_buy_data(i +2 )
    #print("len_patterns", len(f))
for f in p_patterns.p_patterns:
    print(f.data.b_pattern,"||",f.data.s_pattern, "   \t revenue -->",
          round(f.data.revenue_in_percent,1),"winrate -->",round(f.data.winrate(),2),
          "transactions", f.data.transactions , "sell_len" , f.data.S_len)


#for g in f:
    #print(" buy pattern " ,g.b_pattern)
#p_patterns.p_patterns = p_patterns.verifyP_Patterns(p_patterns.p_patterns)
f = []
for  i in range(7):
    f = f + storage.get_relevant_sell_data(i," 50, 50, 50,")
print(len(f))
for g in f:
    print(" buy pattern " ,g.b_pattern , round(g.revenue_in_percent,3), g.S_len , g.winrate())
f = storage.get_best_pattern()
for g in f:
    print(" buy pattern " ,g.b_pattern , round(g.revenue_in_percent,3), g.S_len , g.winrate())

"""
def live_analyse():
    inall = []
    for f in p_patterns.p_patterns:
        storage.update_data_pattern(f.data)
    for i in range(x):
        p_patterns.extend_b_patterns()

        for f in p_patterns.p_patterns:
            storage.update_data_pattern(f.data)

    for f in p_patterns.p_patterns:
        print(f.data.b_pattern, "||", f.data.s_pattern, "   \t revenue -->",
              round(f.data.revenue_in_percent, 1), "winrate -->", round(f.data.winrate(), 2),
              "transactions", f.data.transactions, "sell_len", f.data.S_len)

    while(1):

        f = []
        ina =  input("Eingabe : ")
        if q in ina :
            break
        inall.append(ina)
        if len(inall) >= p_patterns.p_settings.s_lenMax -1 :
            inall.remove(inall[0])
        print("actual String", inall)

        inall_str =  " " +  ", ".join(map(str, inall)) + ","
        print(inall_str)
        for i in range(p_patterns.p_settings.s_lenMax ):
            f = f + storage.get_relevant_sell_data(i, inall_str)

        print(len(f))
        for g in f:
            print(" buy pattern ", g.b_pattern, round(g.revenue_in_percent, 3), g.S_len)


live_analyse()
print("asdask")






