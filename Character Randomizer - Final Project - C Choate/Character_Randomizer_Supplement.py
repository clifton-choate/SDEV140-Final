class playerClass:
    def __init__(self, title, primaryStat, secondaryStat, subReq):
        self.title = title
        self.primaryStat = primaryStat
        self.secondaryStat = secondaryStat
        self.subReq = subReq
        self.subClass = []
    
    # Accessors

    def getTitle(self):
        return self.title
    
    def getPrimaryStat(self):
        return self.primaryStat
    
    def getSecondaryStat(self):
        return self.secondaryStat
    
    def getSubReq(self):
        return self.SubReq
    
    def getSubClass(self):
        return self.subClass
    
   
class species:
    def __init__(self, name, statA, aIncr, statB, bIncr, spIndex):
        self.name = name
        self.statA = int(statA)
        self.aIncr = int(aIncr)
        self.statB = int(statB)
        self.bIncr = int(bIncr)
        self.spIndex = int(spIndex)

        # Accessors

    def getName(self):
        return self.name
    
    def getStatA(self):
        return self.statA
    
    def getAIncr(self):
        return self.aIncr
    
    def getStatB(self):
        return self.statB
    
    def getBIncr(self):
        return self.bIncr
    
    def getSpIndex(self):
        return self.spIndex



class character:
    def __init__(self, name, aScores, cClass, cSubClass, cSpecies, cBackground):
        self.name = name
        self.aScores = aScores
        self.cClass = cClass
        self.cSubClass = cSubClass
        self.cSpecies = cSpecies
        self.background = cBackground
        self.proficiencies = []

    # Accessors

    def getName(self):
        return self.name
  
    def getAScores(self):
        return self.aScores
  
    def getClass(self):
        return self.cClass
  
    def getSubClass(self):
        return self.cSubClass
  
    def getSpecies(self):
        return self.cSpecies
  
    def getBackground(self):
        return self.background

    def getProficiencies(self):
        return self.proficiencies

    # Mutators

    def setAScores(self, aScores):
        self.aScores = aScores

    def setClass(self, cClass):
        self.cClass = cClass

    def setSubClass(self, cSubClass):
        self.cSubClass = cSubClass

    def setSpecies(self, cSpecies):
        self.cSpecies = cSpecies

    def setBackground(self, cBackground):
        self.background = cBackground
  
    def setProficiencies(self, proficiencies):
        self.proficiencies = proficiencies