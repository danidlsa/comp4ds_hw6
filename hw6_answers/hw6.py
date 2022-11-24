###########################################

#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively

class Patient:
    def __init__(self, name:str, symptoms:list):
        self.name=name
        self.symptoms=symptoms
        self.list_of_tests={}
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.
    
    def add_test(self, name_test:str, results:bool):
        self.list_of_tests[name_test]=results
        return self.list_of_tests
         
        # we should be able to store multiple tests (not there yet).. 
        
#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']





    def has_covid(self) -> float:
           
        if self.list_of_tests.get("covid")==True:
            return 0.99
        
        elif self.list_of_tests.get("covid")==False:
            return 0.01
        
        else:
            prob_covid=0.05
            for i in ["fever", "cough", "anosmia"]:
                if i in self.symptoms:
                    prob_covid=+ prob_covid+0.01
            return round(prob_covid, 2)
        
        
d= Patient("Daniela", sym)

d.has_covid()

d.add_test("covid", False)
d.add_test("flu", True)

d.has_covid() #something not working!


# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.

