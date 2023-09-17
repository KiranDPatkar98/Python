# class PlayerCaharcter:
#     def __init__(self, name,age):
#         self.name=name
#         self.age=age
     
#     def run(self):
#         print(f'player {self.name} running')

# player1= PlayerCaharcter('kdp',25)
# player1.run()


# class and static methods

# example for class methods
# class Math:
#     @classmethod
#     def sum(cls,num1,num2):
#         return num1+num2
     

# print(Math.sum(5,6))

# example for static methods

# class Math:
#     @staticmethod
#     def

class SuperList(list):
    def __len__(self):
        return 5
    
kdp=SuperList()
print(len(kdp))
print(kdp.append('abc'))