from sys import exit
from random import randint


class Scene (object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Death(Scene):

    quips = [
        "You died. You kinda suck at this."
        "Your mom would be proud... if she were smarter."
        "Such a loser."
        "I have a small puppy that is better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print "To tell a joke OR to find a way:"
        action = raw_input(">")
        if action == "tell a joke":
            print "Good for you."
            return 'laser_weapon_amory'
        elif action == "find a way":
            print " No way here. You will die."
            return 'death'
        else:
            print "Doesn't compute."
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print "You have to work out a code puzzle."
        code = "%d%d%d" % (randint(1,2),randint(1,2),randint(1,2))
        print " code = %s " % code
        guess = raw_input(">")
        guesses = 0
        while (guesses < 10 and guess != code):
            print "Does not Match!"
            guess = raw_input(">")
            guesses += 1
        if guess == code:
            print "You access the bomb."
            return 'bridge'
        elif guesses == 10:
            print "Too many tries, you will die."
            return 'death'


class Bridge(Scene):
    def enter(self):
        print "You have to burst this bridge."
        print "Throw it OR quitely place it?"
        action = raw_input(">")
        if action == "throw it":
            print "Admire your guts, but you will die here."
            return 'death'
        elif action == "quitely place it":
            print "You are an expert."
            return 'escape_pod'
        else:
            print "Does not compute."
            return 'bridge'

class EscapePod(Scene):
    def enter(self):
        print " Congratulations to you. But you have to input the right password to run it."
        password = randint(1,5)
        guess = raw_input(">")
        guesses = 0
        while guesses < 9 and int(guess) !=password:
            print " Wrong password"
            guess = raw_input(">")
            guesses += 1
        if int(guess) == password:
            print "You make it to escape here."
            return 'finished'
        else:
            print "You lose at the last phase. You will die."
            return 'death'

class Finished(Scene):
    def enter(self):
        print "You won! Good job!"
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_amory' : LaserWeaponArmory(),
        'bridge' : Bridge(),
        'escape_pod' : EscapePod(),
        'death' : Death(),
        'finished' : Finished()
        }

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.scenes.get(self.start_scene)
#        return self.next_scene(self.start_scene)



class Engine(object):

    def __init__(self, scene_map):
        self.scene_map =scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        #print current_scene
        last_scene = self.scene_map.next_scene('finished')
    #    print last_scene

        while current_scene != last_scene:
            print current_scene
            print last_scene
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
#        print current_scene
#        print last_scene
        # be sure to print out the last scene
        current_scene.enter()


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
