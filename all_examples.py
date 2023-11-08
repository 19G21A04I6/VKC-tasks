
class Order:
    def __init__(self, itemname, cooldrink):
        self.__itemname = itemname
        self.__cooldrink = cooldrink

    def get_details(self):
        return f'Ordered items: {self.__itemname} {self.__cooldrink}'

    def rate(self) -> float:
        pass

class ChickenBiryani(Order):
    __ele = 3

    def __init__(self, itemname, cooldrink):
        super().__init__(itemname, cooldrink)

    def rate(self) -> float:
        return self.__ele * 160

class MuttonBiryani(Order):
    __ele = 4

    def __init__(self, itemname, cooldrink):
        super().__init__(itemname, cooldrink)

    def rate(self) -> float:
        return self.__ele * 240

bba = ChickenBiryani("Chicken Biryani", "Thumbsup-200 ml")
nna = bba.get_details()
print(nna)
print(bba.rate())

aab=MuttonBiryani("Mutton Biryani","Thumbsup-200 ml")
ann=aab.get_details()
print(ann)
print(aab.rate())