def price(func):
    def wrapper(self):
        func(self)
        if (self.model == "rx6600"):
            print("Price is 200$")
        elif (self.model == "rtx5090"):
            print("Price is infinite")
        else:
            print("Can't identify")
    return wrapper

class Gpu:
    def __init__(self, company, dealer, model):
        self.company = company
        self.dealer = dealer
        self.model = model
    
    @price
    def display(self):
        print(self.company, self.dealer, self.model)

rx6600 = Gpu(company="AMD", dealer="Sapphire", model="rx6600")

rtx5090 = Gpu(company="Nvidia", dealer="Msi", model="rtx5090")

rx6600.display()

rtx5090.display()
