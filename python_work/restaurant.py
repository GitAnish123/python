# Lets create a class restaurant.




class Restaurant:   
    """A simple representation of a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initillize attributes of a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 25
    
    def describe_restaurant(self):
        """Describe a restaurant"""
        print(f"The restaurant name is {self.restaurant_name} and the cuisine type is: {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Stimulate making a restaurant be opened."""
        print(f"{self.restaurant_name} is now currently open!")

    def set_number_served(self, customers_total):
        """Set the amount of customers that have been served, typically in a restaurant."""
        if customers_total >= self.number_served:
            self.number_served = customers_total
        else:
            print("You already had a greater amount of customers, you can't reduce the amount of customers served!")
    
    def increment_number_served(self, amount_increasing):
        """
        Increase the amount of customers that have been served, typically in a restaurant. 
        Increases the value then adds that value with the existing value to make the total value.
        """
        if amount_increasing >= self.number_served:
            self.number_served += amount_increasing
        else:
            print("You already had a greater amount of customers, you can't reduce the amount of customers served!")

class IceCreamStand(Restaurant):    
    """A simple representation of an ice-cream stand, but relating to a restaurant that shares the same information."""
    def __init__(self, restaurant_name, cuisine_type='ice cream'):   
        """Create/review and access attributes for a child class."""
        super().__init__(restaurant_name, cuisine_type)    
        self.flavors = []   
    
    def display_ice_cream_flavors(self):   
        """Display all the ice cream flavors avaliable in the ice-cream stand."""
        print("\nHere are all the ice-cream flavors available:")
        for flavor in self.flavors:   
            print(f"-- {flavor}")

ice_cream = IceCreamStand('Marble Slab Creamery')
ice_cream.flavors = ['strawberry', 'mint chocolate ship', 'vanilla', 'chocolate', 'butterscotch', 'cotton candy', "cookies 'n cream"]