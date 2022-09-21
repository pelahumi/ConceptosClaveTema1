class Rectangulo():

    #Constructor
    def __init__(self, pto1, pto2):
        self.pto1 = pto1
        self.pto2 = pto2

    #Getters
    def get_pto1(self):
        return self.pto1

    def get_pto2(self):
        return self.pto2

    #Setters
    def set_pto1(self, pto1):
        if pto1 == "":
            pto1 = (0,0)
        else:
            self.pto1 = pto1

    def set_pto1(self, pto2):
        if pto2 == "":
            pto2 = (0,0)
        else:
            self.pto2 = pto2
