class CellPhoneClass:
    def __init__(self, manufact, model, price):
        self.__manufact = manufact # Private attribute
        self.__model = model          # Protected attribute, the two underscores hide it
        self.__retail_price = price    # Public attribute

    def set_manufact(self,manufact): # Argument is (self, manufact), you are changing something you need user input
        self.__manufact = manufact #DIFFERENCE BETWEEN ATTRIBUTE AND ARGUMENT


    def get_manufact(self): # you are not changing anything, no input from user, returning an attribute
        return self.__manufact
    
    # Setter for model
    def set_model(self, model):
        self.__model = model

    # Getter for model
    def get_model(self):
        return self.__model

    # Setter for retail price
    def set_retail_price(self, price):
        self.__retail_price = price

    # Getter for retail price
    def get_retail_price(self):
        return self.__retail_price

