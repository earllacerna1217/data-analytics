
class restaurant: 
   """" restaurant class and food types """
   def __init__ (self, rest_name, food_type):
    
    self.rest_name = rest_name
    self.food_type = food_type
    self.number_served = 0
    self.customer_ratings = []

   def describe_rest(self):
      print(f"{self.rest_name} serves {self.food_type}")

   def rest_open(self):
     print(f"{self.rest_name} is open")

   def add_num_served(self):
    self.number_served += int(input("How many customers served today? "))

   def print_num_served (self):
    print(f"{self.rest_name} has served {self.number_served} customer")
    
    
   def customer_rating (rating):
    rating = print(input("How woud you rate your experience today on a scale of 1-5 (5 being excellent)?")) 
    
                                                                                                                

                               
restaurant1 = restaurant("mcdonalds", "Fast food")
restaurant2 =restaurant("Jack in the box", "Fast food")
restaurant3 = restaurant("Wolfgang", "Fine dining")

restaurant1.describe_rest()

for rest in [restaurant1, restaurant2, restaurant3]:
  rest.describe_rest()
  rest.rest_open()

restaurant2.add_num_served()
restaurant2.print_num_served()