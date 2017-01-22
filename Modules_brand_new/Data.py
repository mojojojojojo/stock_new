
class Data:
    def __init__(self,b_pattern="",s_pattern = ""):
        self.transactions = 0
        self.b_pattern = b_pattern
        self.s_pattern = s_pattern
        self.successful_transac = 0
        self.revenue_in_percent  = 0
    def s_len(self):
        return self.s_pattern.count(",")
    def b_len(self):
        return self.b_pattern.count(",")
    def winrate(self):
        return 1 - (self.transactions - self.successful_transac)/self.transactions


