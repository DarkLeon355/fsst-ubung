import random as r

class Zahlenraten:
    def __init__(self, min: int = 1, max: int = 100):
        self.min = min
        self.max = max
        self.versuche = 0
        self.random_number()

    def random_number(self):
        self.zahl = r.randint(self.min, self.max)

    def raten(self, user_input):
        user_input = int(user_input)
        self.versuche += 1
        if user_input == self.zahl: 
            self.random_number()
            return 0 # richtig
        if user_input < self.zahl: return -1 # zu klein
        if user_input > self.zahl: return 1 # zu groß
        
        


    
