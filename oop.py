# CLASSES
# OOП - объектно-ОРИЕНТИРОВАННОЕ программирование


# class Person:
#     name = "Ivan" # classes' atribut

#     def __init__(self, age, last_name): #конструктор класса, __init__ - thunder methods
#         self.age = age # атрибут экземпляра класса
#         self.last_name = last_name

#     def get_name(self): # метод класса, self - ключевое слово для ссылки на атрибут экз. класса
#         print(self.age)

#     def get_last_name(self):
#         print(self.last_name) 

# person1 = Person(20, "Ivanov") # создание экземпляра класса
# person1.get_last_name()
# person1.get_name()  
# print(person1.age)
# print(person1.name) 


# принципы ООП
# 1. Инкапсуляция - это свойство ситемы, позвол защитить класс оот внешних воздействий
# 2. Наследование - это когда класс наследует все его атрибуты и мнтоды 
# 3. Полиморфизм - это название атрибутов и методов 
# 4. Абстракция - свойство системы, позвол упростить сложные системы и упрощать их разработку

# НАСЛЕДОВАНИЕ
# class Person: # родительский класс
#     h = 180
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")



# class Student(Person):  
#     def __init__(self, name, age, grade):       
#         self.grade = grade
#         self.name = name
#         self.age = age

#     def get_student(self):
#         print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# student1 = Student("A", 20, 5)
# student1.get_info()
# student1.get_student() 
# print(student1.h) 




# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ 
# class A:
#     # def text(self):
#     #     print("A")
#     pass

# class B: 
#     def text(self):
#         print("B")

# class B2:
#     def text(self):
#         print("B2")

# class C(B2): 
#     # def text(self):
#     #     print("C")
#     pass

# class D (A, C, B):
#     pass

# d = D()
# d.text() 
# print(D.mro())





# ПОЛИМОРФИЗМ
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print("Some sound")

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow") 





# ИНКАПСУЛЯЦИЯ
# class BankAccount:
#     def __init__(self, balance, name):
#         self.__balance = balance # приватное
#         self.name = name # публичное
#         self._password = '123' #  защищенное

#     def get_balance(self):
#         return self.__balance
    
#     def __set_password(self, password):
#         self._password = password
    
#     def _set_balance(self, balance):
#         if balance < 0:
#             print("Balance can not be negative")
#         else:
#             self.__balance = balance

# visa = BankAccount(100, "Ivan") 
# print(visa.get_balance())
# visa._set_balance(200)
# print(visa.get_balance())
# visa._BankAccount__set_password("1234")
# print(visa._password)







# АБСТРАКЦИЯ
# from abc import ABC, abstractmethod
# class Figure(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass

#     @abstractmethod
#     def get_perimeter(self):
#         pass

# class Rectange(Figure):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def get_area(self):
#         return self.a * self.b

#     def get_perimeter(self):
#         return 2 * (self.a + self.b)

# class Square(Figure):
#     def __init__(self, a):
#         self.a = a

#     def get_area(self):
#         return self.a ** 2
    
#     def get_perimeter(self):
#         return 4 * self.a
    

# rectangle = [Rectange(2, 5), Square(3)]
# for i in rectangle:
#     print(i.get_area())
#     print(i.get_perimeter())






        














# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year

#     def get_model(self):
#         print(self.model)
#     def get_color(self):
#         print(self.color)
#     def get_year(self):
#         print(self.year)         

# tesla = Car("Craft", "White", "2023")
# vw = Car("Passat", "Black", "2004")

# tesla.get_model()
# tesla.get_color()
# tesla.get_year()

# vw.get_model()
# vw.get_color()
# vw.get_year() 





# class Uni:
#     def __init__(self, name, location, departments, students, grades):
#         self.name = name
#         self.location = location
#         self.departments = departments
#         self.students = students
#         self._grades = grades 

#     def get_name(self):
#         print(self.name)
#     def get_location(self):
#         print(self.location)
#     def get_departments(self):
#         print(self.departments)
#     def get_students(self):
#         print(self.students)
#     def get_grades(self):
#         return self._grades 
    
#     def get_info(self):
#         print(f"Name: {self.name}, location: {self.location}, departments: {self.departments}, students: {self.students}, grades: {self._grades}")


# uni1 = Uni("BSU", "Gagarina", "chinese", 1500, "3")
# uni2 = Uni("Manas", "Manasa", "turkish", 1700, "5")

# uni1.get_grades() # НЕ ВЫВОДИТ 
# print(uni1.get_grades()) # ВЫВОДИТ 



# class Bsu(Uni):
#     def __init__(self, name, location, departments, students, grades):
#         self.name = name
#         self.location = location
#         self.departments = departments
#         self.students = students
#         self._grades = grades

#     def get_location(self):
#         print("Manasa")
#     def get_students(self):
#         print(1333) 
#     def get_teachers(self):
#         print(1200)  


# class Politeh(Uni):
#     def __init__(self, name, location, departments, students, grades):
#         self.name = name
#         self.location = location
#         self.departments = departments
#         self.students = students
#         self._grades = grades

#     def get_location(self):
#         print("Ahunbaeva")
#     def get_students(self):
#         print(1555) 
#     def get_teachers(self):
#         print(1500)   

# uni1.get_info()
# uni2.get_info()

# Bsu.get_location("self")    
# Bsu.get_students("self")

# Politeh.get_location("self")
# Politeh.get_students("Self")








# def parts_sums(ls):
#     total = sum(ls) 
#     res = [total]
#     for l in ls:
#         total -= l
#         res.append(total) 
#     return res
# ls = [0, 1, 3, 6, 10]
# print(parts_sums(ls))  



# def sum_cubes(n):
#     return sum(n**3 for n in range(1, n + 1))
# print(sum_cubes(5)) 


# def generate_shape(n): # first option
#     for i in range(1, n + 1): 
#         print("+" * n)
# generate_shape(8)  
# def generate_square(n): # second option
#     return '\n'.join(['+' * n for _ in range(n)])
# print(generate_square(3)) 












  