# INHERITANCE - "Is a"
class Person:
    def __init__(self, name, age):        
        self.name = name
        self.age = age

    def display(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, studentid):
        super().__init__(name, age)
        self.studentid = studentid

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

student1 = Student("Armstrong", 22, "S3001")
teacher1 = Teacher("Saviour", 55, "Python")

student1.display()
print(f"My studentid is {student1.studentid}")

teacher1.display()
print(f"My subject is {teacher1.subject}")

print("=============")
# COMPOSITION - "Has a"
class Engine:
    def start(self):
        print("Engine start")


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()

    def car_start(self):
        print(f"Starting car {self.brand}")
        self.engine.start()

car1 = Car("Bugatti")
car1.car_start()        


print("============")
# ECAPSULATION - Protecting your data
class Bank:
    def __init__(self,owner, balance = 0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount
        print(f"Deposit Sucessful. You deposited N{amount}. New balance: N{self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient Funds.")
        self.__balance -= amount
        print(f"Withdrawal successful. You withdrew N{amount}. New balance: N{self.__balance}")

    def get_balance(self):
        return self.__balance



account = Bank("John", 10000)

account.deposit(2000)
account.withdraw(7000)
print(f"Balance: N{account.get_balance()}")