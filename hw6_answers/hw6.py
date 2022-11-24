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
        

sym= ["cough", "sore throat"]        
d= Patient("Daniela", sym)

d.has_covid()

d.add_test("covid", False)
d.add_test("flu", True)

d.has_covid() 
d.add_test("covid", True)
d.has_covid()

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them


# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.


class Card:
   
    def __init__(self, suit:str, value:int): #value may also be a string (e.g. ace/ king etc)
        self.suit = suit
        self.value = value
        self.show()
        
    def show(self):
        print(str(self.value) +" of " + self.suit)

#test    
Spade_ace = Card("spades", "ace")
Spade_ace.suit
Spade_ace.value

mystery = Card("hearts", 3)
mystery.show()


# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K).
#It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value.
#When a card is drawn, the card should be removed from the deck.

import random

class Deck:
   
    def __init__(self):
        self.deck = []
        self.__create__()  #removed - otherwise confused about the lack of attribute when you "use" the class
        self.show()
        self.shuffle()
        self.draw()
        
    def __create__(self):
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for val in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.deck.append(Card(suit,val))

    def show(self):
       #print(self.deck) #does not work as it returns list of things that refer to 
       for crd in self.deck:
           crd.show()

#test_deck = Deck()
#test_deck.show()

    def shuffle(self):
        for i in range(0,51):
            r = random.randint(0,i)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]
            
    def draw(self):
         #The pop() method removes the item at the given index from the list and returns the removed item.
        return self.deck.pop()

test_deck = Deck()
test_deck.shuffle()
test_deck.show()      #currently showing both shuffled and unshuffuled deck?

random_card = test_deck.draw() # can't just call test_deck.draw(), have to assign to new variable
random_card.show()

#check how (repeatedly) swapping works
list = ["z","one","two","three","four","five"]
list[5]

list[0], list[5] = list[5], list[0]
list 

for i in range(0,5) :
    r = random.randint(0,i)
    list[i], list[r] = list[r], list[i]
list




###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.


#non-abstract version
#class PaneFigure_og()

import abc
from abc import ABC, abstractmethod

class PlaneFigure(ABC):
    #compute_perimeter() #not required for abstract class. - also no self.
    #compute_surface()
    
    @abstractmethod
    def compute_perimeter(self):
       pass

    @abstractmethod #wrong: @abc.abstractproperty
    def compute_perimeter(self):
       pass


# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and
#has as parameters in the constructor "base", "c1", "c2", "h".
#("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height).
#Implement the abstract methods with the formula of the triangle.

class Triangle(PlaneFigure):
    def __init__(self):
    
    @classmethod
    def compute_perimeter(base,c1,c2,h):
        return print(base + c1 + c2)


# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.



#reference examaple

class PlaneFigure(ABC):
    def rk(self):
        print("Abstract Base Class")
 
class Triangle(PlaneFigure):
    def rk(self):
        super().rk() #not required in our case as 
        print("subclass ")
 
# Driver code
r = K()
r.rk()

