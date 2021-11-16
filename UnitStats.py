import random

class BasicUnit():
    def __init__(self,life, attack, defend,initiative,attacker,totwin,totloss,unitwin,tempRoll,totalAttack,totalDefense,hits,gameState):
        self.life = 100
        self.attack = random.randint(1, 10)
        self.defend = random.randint(1, 10)
        self.initiative = 0
        self.attacker=0
        self.damage = 10
        self.totwin=0
        self.totloss=0
        self.unitwin=0
        self.tempRoll = 0
        self.totalAttack = 0
        self.totalDefense = 0
        self.hits = 0
        self.initWin = 0
