#Block_1(Зробити для прямокутників)
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides =[float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Pramokytnick(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)  #super().__init__(3) 

    def findArea(self):
        a, b = self.sides
        perim = (a+b)*2
        area = a*b
        print('The area of the pramokytnick is %0.2f' %area)

t=Pramokytnick()
t.inputSides()
t.findArea()


#Block_2( Створити клас машина з атрибутами name,  make, model та 
# методами start та stop, які виводять інформацію про те що автомобіль стартував чи зупинився відповідно.)
class Car():
    def __init__(self, name, make, model):
        self.name=name
        self.make=make
        self.model=model
    def Start(self):
        print(f"Start{self.name}")

    def Stop(self):
        print(f"STOP{self.name}")

t=Car("BMW", 775, "F8547")
c=Car("toyota", 8525, "hh88")
t.Start()
c.Stop()

