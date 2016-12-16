
class PSettings:
    def __init__(self,b_lenMax = 3, s_lenMax = 3,nr_elements = None, winrateThresh= 0, revenueThresh = 50):
        self.winrateThresh = winrateThresh
        self.revenueThresh = revenueThresh
        self.b_lenMax = b_lenMax
        self.s_lenMax = s_lenMax
        if nr_elements is None:
            self.nr_elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]


