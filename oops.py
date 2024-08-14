#Create a car class with attributes like brand and model.Then create an instance of this class.

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

# my_car1=Car("Toyota","Corolla")
# print(my_car1.brand)
# print(my_car1.model)

# my_car2=Car("Tata","Safari")
# print(my_car2.brand)
# print(my_car2.model)

#Add a method to the car class that displays the full name of the car(brand and model).

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
# my_car1= Car("Toyota","Corolla")
# print(my_car1.full_name())

#Create an electric Car class that inherits from the car class and has an additional attribute battery_size.

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def full_name(self):
#         return f"{self.brand} {self.model}"

# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size=battery_size

# my_car=ElectricCar("Tesla","Model S","85KwH")
# print(my_car.model)
# print(my_car.battery_size)

#Modify the Car class to encapsulate the brand attribute,making it private and provide a getter method for it.

# class Car:
#     def __init__(self,model,brand):
#         self.__model=model                  #to make private:- __model is used here.
#         self.brand=brand
#     def get_model(self):                    #getter method
#         return self.__model+ "!"
    
#     def set_model(self,model):              #setter method
#         self.__model=model

# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size=battery_size

# my_car=ElectricCar("Tesla","Model S","85KwH")
# print(my_car.get_model())
# my_car.set_model("Biston")
# print(my_car.get_model())

#Demonstrate Polymorphism by defining a method fuel_type in both car ElectricCar classes, but with different behaviors.

# class Car:
#     def __init__(self,model,brand):
#         self.__model=model                  
#         self.brand=brand
#     def get_model(self):                   
#         return self.__model+ "!"
    
#     def set_model(self,model):              
#         self.__model=model
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     def fuel_type(self):
#         return "petrol or diesel."

# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size=battery_size

#     def fuel_type(self):
#         return "Electric Charge."

# my_car=ElectricCar("Tesla","Model S","85KwH")
# print(my_car.fuel_type())

# safari=Car("Tata","Safari")
# print(safari.fuel_type())


#Add a static Method to the car class that returns a general description of a car.

# class Car:
#     def __init__(self,model,brand):
#         self.__model=model                  
#         self.brand=brand
#     def get_model(self):                   
#         return self.__model+ "!"
    
#     def set_model(self,model):              
#         self.__model=model
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     def fuel_type(self):
#         return "petrol or diesel."
    
#     @staticmethod             #(static method can be accessed by classes but not from objects)
#     def general_description():
#         return "This is a general description of a car."

# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size=battery_size

#     def fuel_type(self):
#         return "Electric Charge."

# safari=Car("Tata","Safari")
# # print(safari.general_description())   #error bcz object cant access the static method
# print(Car.general_description())

# Use a property decorator in the car class to make the model attribute read-only.

# class Car:
#     def __init__(self,model,brand):
#         self.__model=model                  
#         self.brand=brand
#     def get_model(self):                   
#         return self.__model+ "!"
    
#     def set_model(self,model):              
#         self.__model=model
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     def fuel_type(self):
#         return "petrol or diesel."
    
#     @staticmethod                     
#     def general_description():
#         return "This is a general description of a car."
    
#     @property
#     def model(self):
#         return self.__model

# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size=battery_size

#     def fuel_type(self):
#         return "Electric Charge."

# mycar=Car("Tata","Safari")
# # mycar.model="city"           This can give us an error
# print(mycar.model)

#Demonstrate the use of isinstance() to check, if my_tesla is an instance of car and ElectricCar.

# class Car:
#     def __init__(self,model,brand):
#         self.__model=model                  
#         self.brand=brand
#     def get_model(self):                   
#         return self.__model+ "!"
    
#     def set_model(self,model):              
#         self.__model=model
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     def fuel_type(self):
#         return "petrol or diesel."
    
#     @staticmethod                     
#     def general_description():
#         return "This is a general description of a car."
    
#     @property
#     def model(self):
#         return self.__model

# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size=battery_size

#     def fuel_type(self):
#         return "Electric Charge."

# my_tesla=ElectricCar("Tesla","Model S","85KwH")
# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))

#Create two classes Battery and Engine, and Let the electricCar class inherit from both, demonstrating multiple inheritance. 

# class Car:
#     def __init__(self,model,brand):
#         self.__model=model                  
#         self.brand=brand
#     def get_model(self):                   
#         return self.__model+ "!"
    
#     def set_model(self,model):              
#         self.__model=model
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     def fuel_type(self):
#         return "petrol or diesel."
    
#     @staticmethod                     
#     def general_description():
#         return "This is a general description of a car."
    
#     @property
#     def model(self):
#         return self.__model

# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size=battery_size

#     def fuel_type(self):
#         return "Electric Charge."


# class Battery:
#     def battery_info(self):
#         return "This is battery information."

# class Engine:
#     def engine_info(self):
#         return "This is engine information."

# class ElectricCar2(Battery,Engine,Car):
#     pass

# my_new_car=ElectricCar2("Tesla","Model S")
# print(my_new_car.battery_info())
# print(my_new_car.engine_info())













