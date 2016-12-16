import copy

from Modules_brand_new.Data import Data


class Storage () :


    def __init__ (self ):
        self.data_patterns  = [[]] # length s_pattern[patterns], length b_pattern[patterns]
        self.connected_share = "None"

    def update_data_pattern(self,data):
        while len(self.data_patterns) <= data.sell_len:
            self.data_patterns.append([])
            print(len(data.s_pattern))
        if len(self.data_patterns[data.sell_len]) == 0:
            self.data_patterns[data.sell_len].append(copy.copy(data))
            print("added")
        else:
            for f in self.data_patterns[data.sell_len]:
                if f.b_pattern == data.b_pattern and f.s_pattern == data.s_pattern:
                    self.data_patterns[data.sell_len].insert(self.data_patterns[data.sell_len].index(f),copy.copy(data))
                    self.data_patterns[data.sell_len].remove(f)
                    print("changed")



    def load_format_file(self,file):
        self.data_patterns = [[]]
        with open(file) as f:
            length_all = int(f.readline())
            for k in range(length_all):
                self.data_patterns.append([])
                length = int(f.readline())
                #print("length read = " + str(length))
                for x in range(length):
                    g = Data()
                    try:
                        g.sell_len = float(f.readline())
                    except:
                        print("ERROR reading file.sell_len")
                        g.sell_len = 0
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

            f.close()

    def save_format_file(self,file):

        with open(file, 'w') as f:
            f.write(str(len(self.data_patterns)) + "\n")
            for t in self.data_patterns:
                f.write(str(len(t)) + "\n")
                for x in t:
                    f.write(str(x.sell_len) + "\n")
                    f.write(str(x.revenue_in_percent) + "\n")
                    f.write(str(x.b_pattern) + "\n")
                    f.write(str(x.s_pattern) + "\n")
                    f.write(str(x.successful_transac) + "\n")
                    f.write(str(x.transactions) + "\n")
        f.close()

storage = Storage()
data = Data()
data.b_pattern = "0, 0"
data.s_pattern = "0, 1"
data.sell_len = 2
data.revenue_in_percent = 12
#print(len(storage.data_patterns))
storage.update_data_pattern(data)
for f in storage.data_patterns[2]:
    print(f.revenue_in_percent)
data.revenue_in_percent = 20
storage.update_data_pattern(data)
for f in storage.data_patterns[2]:
    print(f.revenue_in_percent)
storage.save_format_file('test.moj')
storage.load_format_file('test.moj')
for f in storage.data_patterns[2]:
    print(f.revenue_in_percent)
data.revenue_in_percent = 223
storage.update_data_pattern(data)
for f in storage.data_patterns[2]:
    print(f.revenue_in_percent)
#print(str(storage.data_patterns[1][1].s_pattern) + "  " + str(storage.data_patterns[0][0].b_pattern))
#for x in storage.data_patterns:
 #   if x.revenue_in_percent:
  #      print(x.revenue_in_percent)
