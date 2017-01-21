from LoadSave import open_file
import CreateP_Patterns.CreateP_Patterns as Cpp
array = [[], [], [], []]
arraya = open_file("StockData/table (1).csv")
array[2] = arraya[2][0:]
array[3] = arraya[3][0:]
p_patterns = Cpp.P_Patterns()
verlauf, prices = Cpp.prepare_data(array, p_patterns.p_settings.max_stg)
x = 1
for i in range(x):
    p_patterns.extend_b_patterns(verlauf, array)
#p_patterns.p_patterns = p_patterns.verifyP_Patterns(p_patterns.p_patterns)
for f in p_patterns.p_patterns:
    print(f.data.b_pattern,"||",f.data.s_pattern, "   \t revenue -->",
          round(f.data.revenue_in_percent,1),"winrate -->",round(f.data.winrate(),2), "transactions", f.data.transactions)
print("----"*22)
array = [[], [], [], []]
arraya = open_file("StockData/table (2).csv")
array[2] = arraya[2][0:]
array[3] = arraya[3][0:]
p_patterns = Cpp.P_Patterns()
verlauf, prices = Cpp.prepare_data(array, p_patterns.p_settings.max_stg)

for i in range(x):
    p_patterns.extend_b_patterns(verlauf, array)
#p_patterns.p_patterns = p_patterns.verifyP_Patterns(p_patterns.p_patterns)
for f in p_patterns.p_patterns:
    print(f.data.b_pattern,"||",f.data.s_pattern, "   \t revenue -->",
          round(f.data.revenue_in_percent,1),"winrate -->",round(f.data.winrate(),2), "transactions", f.data.transactions)

print("----"*22)
array = [[], [], [], []]
arraya = open_file("StockData/table (3).csv")
array[2] = arraya[2][0:]
array[3] = arraya[3][0:]
p_patterns = Cpp.P_Patterns()
verlauf, prices = Cpp.prepare_data(array, p_patterns.p_settings.max_stg)

for i in range(x):
    p_patterns.extend_b_patterns(verlauf, array)
#p_patterns.p_patterns = p_patterns.verifyP_Patterns(p_patterns.p_patterns)
for f in p_patterns.p_patterns:
    print(f.data.b_pattern,"||",f.data.s_pattern, "   \t revenue -->",
          round(f.data.revenue_in_percent,1),"winrate -->",round(f.data.winrate(),2), "transactions", f.data.transactions)