from datetime import date

class Student:
    def __init__(self, studentid, name, dob, classification):
        self.__studentid = studentid
        self.__name = name  
        self.__dob = dob
        self.__classification = classification
        self.__age = 0
        self.__register = ''

    def calc_age(self): #set method, changing value
        today = date.today() #getting today
        dob_list = self.__dob.split('/') #creates a list of 04, 16, 2004
        dob_year = int(dob_list[2])
        age = today.year - dob_year
        
    def register(self):
            if self.__classification =='senior':
                self.__register = '11/1 thru 11/3'
            elif self.__classification == 'junior':
                self.__resgister = '11/4 thru 11/6'
            elif self.__classification == 'sophomore':
                self.__register = '11/7 thru 11/9'
            elif self.__classification == 'freshman':
                self._register = '11/10 thru 11/12'
            else:
                self.__register = 'classification not found'

    def return_age(self):
            return self.__age
        
    def return_registration(self):
            return self.__register



