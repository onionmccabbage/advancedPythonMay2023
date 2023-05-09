from review_class import NumberFun
from datetime import datetime

class ExtendedNumberFun(NumberFun):
    def __init__(self, num, flag):
        super().__init__(num)
        self.flag = flag # could use get/set methods
        if self.flag == True:
            self.today = datetime.today()
        else:
            self.today = 'today'
    def __str__(self):
        txt = super().__str__()
        return txt + f'\nToday is {self.today}'
    

if __name__ == '__main__':
    r = ExtendedNumberFun(100,True)
    print(r)