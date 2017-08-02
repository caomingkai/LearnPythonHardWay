import random
import ex45scene
import ex45challengeItems

class Challenge(Scene):

    items = {
            mize: mize(),
            mate: mate(),
            sudocu: sudocu(),
    }

    def challengeRandom():
        result = choice( items.keys() )

        if result == True:
            return True
        else:
            return False
