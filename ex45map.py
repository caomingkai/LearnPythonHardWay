import ex45person
import ex45scene

class Map(object):
    adventureNum = 0
    passNum = 0
    hero = ex45person.Person(0)
# only to use its method enter() to show the results.
    deathScene = ex45scene.Death()
    winningScene = ex45scene.Winning()
    bloodAddScene = ex45scene.BloodAdd()
    challengeScene = ex45scene.Challenge()
    # print "1111111111111111111"
    def __init__(self, adventureNum, passNum):
        self.adventureNum = adventureNum
        self.passNum = passNum
        self.hero.blood = adventureNum

    def play(self):
        # print "111111111111"
        while(self.passNum < self.adventureNum):
            result = self.challengeScene.enter()
            if result == 1:
                self.passNum += 1
                print "GOOD JOB. YOU have passed [ Barrier-",self.passNum,"]"
            elif result == 2:
                # print "self.hero.blood:",self.hero.blood
                # print " "
                print "YOU SUCK.YOU are now at [ Barrier-",self.passNum,"]"
                self.hero.blood -= 1
                if self.hero.blood == 0:
                    self.deathScene.enter()
                if self.hero.blood <= 1:
                    userInput = raw_input( "Do you need to add blood? y/n:  ")
                    if userInput == 'y':
                        # run until bloodAdd is True
                        while( not self.bloodAddScene.enter() ):
                            pass
                        # never indent the following code!! since it does not belong to he while
                        self.hero.blood += 1
                    else:
                        # no need for bloodadd, just go challengeScene
                        pass
                else:
                    # no need to ask, just go challengeScene
                    pass
            # return no True OR False, but 2. So just enter() again
            else:
                result = self.challengeScene.enter()

        self.winningScene.enter()
