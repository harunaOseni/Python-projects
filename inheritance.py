class Animal: 
    def __init__(self): 
        self.num_eyes = 2 

    def breathe(self):
        print("breathing")



class Human(Animal):
    def __init__(self): 
        super().__init__()

    def focused (self):
        print("focused")


junior = Human()
junior.breathe()
junior.focused()
