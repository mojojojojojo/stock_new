from LoadSave import open_file
import Analyze_Data.CreateP_Patterns as Cpp
from storage import Storage
x = 100

print("----"*22)
array = [[], [], [], []]
arraya = open_file("StockData/table (3).csv")
array[2] = arraya[2][0:]
array[3] = arraya[3][0:]
p_patterns = Cpp.P_Patterns(array)
storage = Storage("table (2)")



for i in range(x):
    p_patterns.extend_b_patterns()

    for f in p_patterns.p_patterns:
        storage.update_data_pattern(f.data)
    storage.save_format_file()
    f = storage.get_relevant_buy_data(i + 1)
    print("len_patterns", len(f))
#for g in f:
    #print(" buy pattern " ,g.b_pattern)
#p_patterns.p_patterns = p_patterns.verifyP_Patterns(p_patterns.p_patterns)


for f in p_patterns.p_patterns:
    print(f.data.b_pattern,"||",f.data.s_pattern, "   \t revenue -->",
          round(f.data.revenue_in_percent,1),"winrate -->",round(f.data.winrate(),2), "transactions", f.data.transactions)
