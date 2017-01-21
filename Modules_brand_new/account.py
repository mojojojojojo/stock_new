class Account:

    def __init__(self,data):
        self.bought_flag = False
        self.b_price = 0.0
        self.data = data

    def __call__(self, bs, price):

        if bs is 'buy':
            self.b_price = float(price)
            self.bought_flag = True

        elif bs is 'sell':
            if self.bought_flag == True:
                if  -((self.b_price- price) / self.b_price) > 0:
                    self.data.successful_transac += 1
                self.data.revenue_in_percent = (((-(self.b_price - float(price)) / self.b_price)*100 + self.data.revenue_in_percent *self.data.transactions)/(self.data.transactions + 1))
                self.data.transactions += 1
                self.bought_flag = False
            else:
                print("ERROR : trying to sell but bought_flag = False")
        else :
            print("ERROR bs flag not set")