class normalized_curve():
    def __init__(self, mean = None, standard_deviation = None):
        self.mean = mean
        self.dev = standard_deviation
    
    def get_zscore(self, num):
        return (num - self.mean) * self.dev

    def get_num(self, zscore):
        return (zscore * self.dev) + self.mean


class food():
    def __init__(self, calories):
        self.calories = calories
        self.curve = normalized_curve()
        self.number

class bird():
    def __init__(self):
        self.tempurature = normalized_curve()
        self.food = []
        self.predators = []

    def eat(self):
