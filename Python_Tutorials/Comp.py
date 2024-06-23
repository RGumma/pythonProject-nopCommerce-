class Comp:
    def __init__(self, cpu, ram):      # if you declare the variable outside init they are static variables
        self.cpu=cpu               #Special method and in java it is constructor
        self.ram=ram

                                     # if you declare the variables inside init they are instance variables
    def config(self):
        print("config is ", self.cpu, self.ram)


com1 = Comp('i5', 16)
com1.config()