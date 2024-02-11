#tuple vs set
a = (1,2,3)
#hashable str,int,float,set their value can be hashed
#unhashable list, dict, and et, because they are mutable
class car:
    def  __init__(self,make) -> None:
        self.make = make
    def country(self):
        if self.make.lower() == "toyota" or self.make.lower() == "honda" or self.make.lower() == "mitsubhi kia":
            return "The car make is Japanese" 
        elif self.make.lower() == "benz" or self.make.lower() == "bmw" or self.make.lower() == "volkswagen":
            return "Your car make is German"
        else:
            return "Could'nt determine country of make"
myCar = car("toyota")
print(myCar.country())