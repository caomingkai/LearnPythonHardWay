# import sys;
# sys.path.append("~/Desktop/PythonStuff")

from random import *
import ex45person
from ex45challengeItems import *

#----0---------------------------
class Scene():
    # def __init__():
    #     pass
    def enter(self):
        print "It is a default scene, configure it and rewrite enter"

#----1---------------------------
class Challenge(Scene):

    # def maze():
    #     print "Please input y OR n."
    #     print "maze----1+1=2"
    #     userInput = raw_input(">")
    #     if userInput == 'y':
    #         return 1
    #     elif userInput =='n':
    #         return 2
    #     else:
    #         print "<<<<<<-----Just input y or n!------->>>>>>"
    #         return 3
    #
    #
    # def mate():
    #     print "Please input y OR n."
    #     print "mate----1+1=2"
    #     userInput = raw_input(">")
    #     if userInput == 'y':
    #         return 1
    #     elif userInput =='n':
    #         return 2
    #     else:
    #         print "<<<<<<-----Just input y or n!------->>>>>>"
    #         return 3
    #
    #
    # def sudocu():
    #     print "Please input y OR n."
    #     print "sudocu----1+1=2"
    #     userInput = raw_input(">")
    #     if userInput == 'y':
    #         return 1
    #     elif userInput =='n':
    #         return 2
    #     else:
    #         print "<<<<<<-----Just input y or n!------->>>>>>"
    #         return 3

#----------------attention!! maze/mate/sudocu  are not string,but pointer of function.
    items = [ maze, mate, sudocu]
#--------------------------------------------------------
    def enter(self):
        #----the () in the last is part of the function expression
        return self.items[randint(0,2)]()

#----2---------------------------
class Winning(Scene):
    def enter(self):
        print "You win!"

#----3---------------------------
class BloodAdd(Scene):
    def enter(self):
        return maze()
        if result == True:
            return True
        else:
            return False

#----4---------------------------
class Death(Scene):
    def enter(self):
        print "You have no blood any more. YOU DIE!!"
        exit(1)
