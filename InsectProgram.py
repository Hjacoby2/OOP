import InsectClass as i

mosquito = i.Insect(2,4, 'mosquito') #class
housefly = i.Insect(2,4, 'housefly')
# these are two separate instances with their own attributes
mosquito.calc_flight() 
housefly.calc_flight()
# calling the methods 
print(f"the {mosquito.get_name()} can fly up to {mosquito.get_flight()} miles") #dont forget about blue parentheses
print(f"the {housefly.get_name()} can fly up to {housefly.get_flight()} miles")

