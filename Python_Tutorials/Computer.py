class Pycharm:
    def execute(self):
        print("compiling")
        print("Running")

       # Duck
        #typing is a
        #concept
       # related
        #to
       # dynamic
       # typing, where
      #  the class of an object is less important than the methods it defines.When you use duck typing, you do not check types at all.Instead, you check for the presence of a given method or attribute.

class Computer:
    def code(self,ide):
        ide.execute()

ide=Pycharm()

comp= Computer()
comp.code(ide)