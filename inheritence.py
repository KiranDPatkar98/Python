# class User:
#     def sign_in(self):
#         print('Logging in ')

# class Wizard(User):
#     def __init__(self,name,power):
#         self.name=name
#         self.power=power

#     def description(self):
#         print(f'Iam {self.name} and I have {self.power} powers')


# # new_wizard=Wizard('kdp',5)
# # new_wizard.sign_in()
# # new_wizard.description()


# # Example for multiple inheritence

# class Archer(User):
#      def __init__(self,name,arrows):
#         self.name=name
#         self.arrows=arrows

#      def archery(self):
#          print(f'Iam {self.name} and I have {self.arrows} arrows')
           

# class Hybrid(Wizard,Archer):
#     def __init__(self,name,power,arrows):
#         Wizard.__init__(self,name,power)
#         Archer.__init__(self,name, arrows)

# men=Hybrid('kdp',5,10)

# print(men.sign_in())
# print(men.name)
# print(men.arrows)
# print(men.description())



class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    def show(self):
        print("D")

obj = D()
obj.show()
print(D.mro())
