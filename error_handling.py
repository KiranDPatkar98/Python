# while True:
#     try:
#         age = int(input('What is your age ?'))
#         10/age

#     except ValueError:
#         print('Please enter a valid number')
#     except ZeroDivisionError:
#         print('Age can\'t be zero')
#     else:
#         print('Thank you')
#         break

class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def check_age(age):
    if age <= 0:
        raise CustomError("Age can't be zero or negative")


try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
    print("Age is valid.")
except CustomError as ce:
    print(f"Custom Error: {ce}")
