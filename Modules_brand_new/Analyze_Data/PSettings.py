
class PSettings:
    def __init__(self,b_lenMax = 3, s_lenMax = 3,nr_elements = None, winrateThresh= -10, revenueThresh = 0.01):
        self.winrateThresh = winrateThresh
        self.revenueThresh = revenueThresh
        self.b_lenMax = b_lenMax
        self.s_lenMax = s_lenMax
        self.max_stg = 100
        if nr_elements is None:
            self.nr_elements =  range(-self.max_stg,self.max_stg +1)


