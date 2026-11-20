
class restaurant: 
   """" restaurant class and food types """
   def __init__ (self, rest_name, food_type): 
    self.rest_name = rest_name
    self.food_type = food_type

   def describe_rest(self):
      print(f"{self.rest_name} serves {self.food_type}")

   def rest_open(self):
     print(f"{self.rest_name} is open")

                               
restaurant1 = restaurant("mcdonalds", "Fast food")
restaurant2 =restaurant("Jack in the box", "Fast food")
restaurant3 = restaurant("Wolfgang", "Fine dining")

restaurant1.describe_rest()

for rest in [restaurant1, restaurant2, restaurant3]:
  rest.describe_rest()
  rest.rest_open()
