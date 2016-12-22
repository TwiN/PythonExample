TYPE_NEUTRAL = 0 # does not attack unless attacked
TYPE_NORMAL = 1  # if attack if enemy is within range
TYPE_BOSS = 2    # boss monster

typeInfo = ["will not attack unless attacked first",
            "will attack if within range",
            "is a boss monster"]

class Npc:
    totalNpc = 0
    def __init__(self, name, level, xtype):
        self.name = name
        self.level = level
        self.xtype = xtype
        Npc.totalNpc += 1
    
    def getInfo(self):
        print "this %s has a level of %d and %s."  % (self.name, self.level, typeInfo[self.xtype])

    def getTotalCharacter(self):
        print 'There is a total of %d mobs' % Mobs.totalMobs


class Character:
    totalCharacters = 0
    def __init__(self,name,level):
        self.name = name
        self.level = level
        Character.totalCharacters += 1

    def getLevel(self):
        print "%s's level is %d." % (self.name, self.level)

    def getTotalCharacter(self):
        print 'There is a total of %d characters' % Character.totalCharacters


# Characters
twin = Character("TwiN", 9999)
cath = Character("Cath", 6969)

# NPCs
rat = Npc("Rat", 3, TYPE_NEUTRAL)
spider = Npc("Spider", 5, TYPE_NORMAL)
goblin1 = Npc("Goblin", 10, TYPE_NORMAL)
goblin2 = Npc("Goblin", 10, TYPE_NORMAL)

# Display characters and npcs
twin.getLevel()
cath.getLevel()
rat.getInfo()
spider.getInfo()
goblin1.getInfo()
goblin2.getInfo()

# twin.getTotalCharacter()


