class Ancestralstories:
    def__init__(self)



#2. **African Cuisine:** You're creating a recipe app specifically for African cuisine.
#The app needs to handle recipes from different African countries, each with its
#unique ingredients, preparation time, cooking method, and nutritional
#information. Consider creating a `Recipe` class, and think about how you might
#create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
#`EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
#methods.

#input-different recipes
#output-different african recipes each its unique ingredient,preparation,time,cooking and nutritional information
#Process-create a recipe class and subclasses for for diffent types of recipes
class Recipe:
    def__init__(self,ingredients,preparation time,cookingMethethod,nutritonInfomation):
        self.ingredients=ingredients
        self.preparation=preparation
        self.time=time
        self.cookingMethethod=cookingMethethod
        self.nutritonInfomation=nutritonInfomation
        
        def handle_different_recipes:
            if {self.ingredients}<={self.preparation} and {self.cookingMethethod}<={self.time}
            return f"food not well cooked "
            else:
                return f"food is well cooked"

        class Morrocanrecipe extends class Recipe:
            def__init__(self,tasty,peprish,hardpreparation):
                self.tasty=tasty
                self.peprish=peprish
                self.hardpreparation=hardpreparation
                def prepare(self):
                    return f"Morrocan food is so {self.peprish} when prepared with too much pepper"
                def eat(self):
                    return f"when prepared with much tomatoes,then Morrocan food can be so {self.tasty} "

        class Ethiopianrecipe extends class Recipe:
            def__init__(self,yummy,unique):
                self.yummy=yummy
                self.unique=unique
                def prepare(self):
                    return f"Ethiopian food uses {self.ingredients} as ingredient there by making it so {self.yummy}"

        class Nigerianrecipe extends class Recipe:
            def __init__(self,sweet,peprish):
                self.sweet=sweet
                self.peprish=peprish
                def cooking(self):
                    return f"Using the right {self.ingredients} nigerian food is one of the most popular food in africa beacause of it's {nutritonInfomation}"

#**African Music Festival:** You're in charge of organizing a Pan-African music
#festival. Many artists from different countries, each with their own musical style
#and instruments, are scheduled to perform. You need to write a program to
#manage the festival lineup, schedule, and stage arrangements. Think about how
#you might model the `Artist`, `Performance`, and `Stage` classes, and consider
#how you might use inheritance if there are different types of performances or
#stages.


#5. Create a class called Product with attributes for name, price, and quantity.
#Implement a method to calculate the total value of the product (price * quantity).
#Create multiple objects of the Product class and calculate their total values.

class Product:
    def__init__(self,name,price,quantity)
    self.name=name
    self.price=price
    self.quantity=quantity
    def calculate_total_value(self):
        if {self.price}==20 and {self.quantity}==5:
            return {self.price}*{self.quantity}
            else:
                return f"not multipled"

        
 
#6. Implement a class called Student with attributes for name, age, and grades (a
#list of integers). Include methods to calculate the average grade, display the
#student information, and determine if the student has passed (average grade >=
#60). Create objects for the Student class and demonstrate the usage of these
#methods.

#7. Create a FlightBooking class that represents a flight booking system. Implement
#methods to search for available flights based on destination and date, reserve
#seats for customers, manage passenger information, and generate booking
#confirmations.

#input-information to determine the availability of a flight
#output-the availability of flights 
#process-create a flightbooking class with methods to determine availbale flights
class FlightBooking:
    def__init__(self):
        def search_available_flights(self):
         if reserved_seats=="full" and passenger_info =="All passenger in"
         return f"No flight available at the moment"
            elif reserved_seats =="not full" and passenger_info =="5 people canceled the flight"
            return f"Flight avaible for 5 people"
            else:
                return f"All flights are booked"

        def find_seat_by_destination(self):
         if destination=="In kisumu 6 will alight" and passenger_info=="6 available seats"
         return f"Flight availble"
         else:
            return f"flight not available"