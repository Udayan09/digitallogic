class Flipflip:
    def __init__(self):
        self.data = 0
        self.Qout = 0
        self.prev_clk = 0

    def set_data(self,data):
        self.data = data

    def clock_in(self,clk):
        if self.prev_clk == 0 and clk == 1:
            self.Qout == self.data
        self.prev_clk = clk


