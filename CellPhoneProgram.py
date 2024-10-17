import CellPhoneClass as cc

def main():

    phone1 = cc.CellPhone('Apple', 'iphone16', 1600) #creating an instance of the CellPHone Class.
    phone2 = cc.CellPhone('Samsung', 'Galaxy10', 1450)

    phone1.set_retail_price(1250) #changing the retail price of phone 1

    print('Here is the data that you entered:')
    print('Manufacturer:', phone1.get_manufact())
    print('Model Number:', phone1.get_model())
    print(f'Retail Price: ${phone1.get_retail_price():.2f}')




