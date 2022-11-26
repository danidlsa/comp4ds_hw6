###########################################

#
# 1. In this exercise we will make a "Patient" class
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
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
        
# TESTS
            
sym= ["cough", "sore throat"]        
d= Patient("Daniela", sym)

d.has_covid()                   #shoud return 0.6 as has one symptom

d.add_test("covid", False) 
d.add_test("flu", True)         #should show both tests done
d.has_covid()                   #should be 0.1 as the negative covid test overrides symptoms

d.add_test("anosmia", True)     #should show three tests
d.has_covid()                   #should stay at 0.1 as still has a negative covid test

d.add_test("covid", True)       #should still show three tests as negative covid result is now ovewritten
d.has_covid()                   #shoutld return 0.99 due to positive covid test


# 2. In this exercise you will make an English Deck class made of Card classes
# the Card class should represent each of the cards
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
        print (str(self.value) +" of " + self.suit)

#TESTS
        
test_card = Card("spades", "ace")
print(test_card.suit)
print(test_card.value)

test_card.show()


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
        self.__create__() 
        
    def __create__(self):
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for val in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.deck.append(Card(suit,val))
        return self.deck

    def shuffle(self):
        for i in range(0,51):
            r = random.randint(0,i)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]
        return print("Your deck has been shuffled.")
            
    def draw(self):
         last_card = self.deck.pop()
         return Card.show(last_card)

#TESTS 
         
test_deck = Deck()

test_deck.shuffle()

test_deck.draw()



###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.

from abc import ABC, abstractmethod

class PlaneFigure(ABC):
    #compute_perimeter() #not required for abstract class. - also no self.
    #compute_surface()
    
    @abstractmethod
    def compute_perimeter(self):
        raise NotImplementedError() #return NotImplementedError  #previously just "pass" (without return)

    @abstractmethod #wrong: @abc.abstractproperty
    def compute_surface(self):
       raise NotImplementedError() #return NotImplementedError


# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and
#has as parameters in the constructor "base", "c1", "c2", "h".
#("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height).
#Implement the abstract methods with the formula of the triangle.

class Triangle(PlaneFigure):
    
    def __init__(self, base, c1, c2, h):
        self.base = float(base)
        self.c1 = float(c1)
        self.c2 = float(c2)
        self.h = float(h)

    def compute_perimeter(self):
        perimeter = self.c1 + self.c2 + self.base
        print("Your triangle's perimeter is " + str(perimeter) + " unit(s)")
        return perimeter
    
    def compute_surface(self):
        area = 0.5 * self.base * self.h
        print("Your triangle's area is " + str(area) + " unit(s) squared")
        return area 

# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as
#parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.

class Rectangle(PlaneFigure):
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
       
    def compute_perimeter(self):
        per = ((2 * self.a) + (2 * self.b)) #change back to return?
        print("Your rectangle's perimeter is " + str(per) + " unit(s)")
        return per
    
    def compute_surface(self):
        area = (self.a * self.a)
        print("Your rectangle's area is " + str(area) + " unit(s) squared")
        return area


# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as
#parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.

import math
math.pi

class Circle(PlaneFigure):
    def __init__(self, radius):
        self.radius = float(radius)
       
    def compute_perimeter(self):
        per = (2 * self.radius * math.pi)
        print("Your circle's perimeter is " + str(round(per,4)) + " unit(s) (to 4 d.p.")
        return per
    
    def compute_surface(self):
        area = (math.pi * (self.radius **2))
        print("Your circle's area is " + str(round(area,4)) + " unit(s) squared (to 4 d.p.)")
        return area

# TESTS
        
# ringhtangled triangle: (b=5, c1=4, c2=3, h=3 --> A=7.5, P=12)
# tri_test = Triangle(base=5, c1=4, c2=3, h=3) #if we use this version we have to specify the keys for each one

tri_test = Triangle(5, 4, 3, 3)

print(tri_test.base)
print(tri_test.h)

tri_test.compute_perimeter()
tri_test.compute_surface()

tri_test.compute_perimeter() + tri_test.compute_surface() #can catually work with the numbers as the return is numerical

# rectangle  P=16 A=15
rect_test = Rectangle(5,3)

print(rect_test.a)
print(rect_test.b)

rect_test.compute_perimeter()
rect_test.compute_surface()


#circle
circ_test = Circle(3)

print(circ_test.radius)
circ_test.compute_perimeter()
circ_test.compute_surface()
