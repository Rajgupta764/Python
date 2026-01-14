class cars:
    def __init__(self,company,modals,colors):
        self.company=company
        self.modals=modals
        self.colors=colors


    @staticmethod
    def greet():
        print("hello world")

    def colorcar(self):
        print("the color of this car is :",self.colors)
    
    def companycar(self):
        print("the company name of this car is :",self.company)
    
    def modalscar(self):
        print("the modals of this car is :",self.modals)

car=cars("BMW",678,"blue")
car.companycar()
car.colorcar()
car.modalscar()
car.greet()