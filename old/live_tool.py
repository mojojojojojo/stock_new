



class Monitor:

    def __init__(self):
        self.b_pattern = None


    """
    pos_path: all path which produce a outcome bigger then startcapital


    pos_pattern:
        transaction_numbers >= 10
        winrate >= 0.50

    winrate pattern =   1 - (all - positive) / all transactions     Auftrittswahrscheinlichkeit
    winrate slice   =  1 - (all - positive) / all paths             Anzahl der positiven Pfade aller pattern vs alle Pattern
    revenue slice   =  all revenues /nbr pos path

    X   =   winrate slice * renvenue slice
    different X for multiple s_pattern lengths
    length should be the pattern with highest X
    if highest X is reached or neg pattern occur  ----> sell
    
    length of buy pattern -> if sum(X) of all slices is bigger than 







    steps:
        1
            analyze first slice
            decide if buy or wait
        2
            analyze first and second slice
            and so on
        -------------------------------------
        if X is bigger than Buy_Value buy





        X,Y is based on winrate per slice
            winrate of the pattern without any selection
            and mean revenue change in %

        winrate becomes higher with longer slice
        transaction_numbers become lower

    when to sell:
        value does not correlate with a pos_path
        best possible path is reached
        (Y) of current is better then following slice








    """
    def calculate_X(self):

        """ calculate a Value to reach a Buy decision
            fixed X for every buy_pattern ?
            X is needed to decide wether to buy or to wait another slice
            aim: best propability for pos_path
        """


    def calculate_Y(self):
        """ calculate a Value to reach a Sell decision
            Y point needs to be evaluated by software
            should determine wheter to sell or hold
        """



    def monitor_data(self):
        """





        """



