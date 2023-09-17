class User:
    def __init__(self,email):
        self.email=email

    def signin(self):
        print('User logging in')



class Wizard(User):
    def __init__(self,name, age,email):
        super().__init__(email)
        self.name=name
        self.age=age
        
wizard1=Wizard('kdp',25,'kdp@gmail.com')
print(wizard1.email)