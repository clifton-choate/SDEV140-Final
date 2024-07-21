'''
Cliff Choate
Final Project
Random generation of tabletop RPG (Dungeons & Dragons, 5th edition) character
v0.2
07/19/2024
'''


from tkinter import*
from Character_Randomizer_Supplement import*
import random


# Create root

root = Tk()
root.title("Character Generator")
root.geometry('900x800+50+30')
topFrame = Frame(root)
topFrame.pack(side = BOTTOM, fill = BOTH, expand = TRUE)


# Define Functions (Will move this to library and import later)

def scoreGenWin():
    
    # Initialize function level variables

    def speciesWindow():

        def speciesWinClose():
            scoreWinClose()
            speciesWin.destroy()

        def backgroundsWindow():
            
            def bgWinClose():
                speciesWinClose()
                bgWin.destroy()

            bgWin = Toplevel(root)
            bgWin.geometry("400x400+200+100")
            bgWin.title("Backgrounds")
            bgWin.focus_force()
            speciesWin.destroy()
        
        
        # Open species select window
        
        speciesWin = Toplevel(root)
        speciesWin.geometry("400x400+200+100")
        speciesWin.title("Species Selection")
        speciesWin.focus_force()
        scoreWin.destroy()

        confirmSpecies = Button(speciesWin, text = "Confirm", command = backgroundsWindow).grid(row = 1, column = 0)
        
        # Add stat bonus for default species

        stats[species.getStatA(speciesList[0])] += speciesList[0].getAIncr()
        stats[speciesList[0].getStatB()] += speciesList[0].getBIncr()

        updateStats()

        # Build radio buttons from species list

        global speciesSelectVar
        #speciesSelectVar = StringVar(root,value = speciesList[0].name)
        speciesSelectVar = IntVar(root,value = 0)

        for s in speciesList:
            Radiobutton(speciesWin, text = s.getName(), variable = speciesSelectVar, value = s.getSpIndex(), command = speciesUpdate).grid(sticky = W)


        speciesWin.protocol("WM_DELETE_WINDOW", speciesWinClose)

    
    # Define on close actions

    def scoreWinClose():
        
        # Re-enables generate button when window is closed

        generate.configure(state = NORMAL)
        scoreWin.destroy()

    # Defines actions to be taken on class selection

    def classUpdate():
        return
    
    # Defines actions to be taken on species selection

    def speciesUpdate():
        global prevSpecies
        
        # Remove stat bonuses from previously selected species
        
        # Special case for Human (+1 to all)

        if prevSpecies == 7:
            for s in range(6):
                stats[s] -= 1
        else:
            stats[speciesList[prevSpecies].getStatA()] -= speciesList[prevSpecies].getAIncr()
            stats[speciesList[prevSpecies].getStatB()] -= speciesList[prevSpecies].getBIncr()

        # Add stat bonuses from new species

        # Special case for Human (+1 to all)

        if speciesSelectVar.get() == 7:
            for s in range(6):
                stats[s] += 1
        else:
            stats[speciesList[speciesSelectVar.get()].getStatA()] += speciesList[speciesSelectVar.get()].getAIncr()
            stats[speciesList[speciesSelectVar.get()].getStatB()] += speciesList[speciesSelectVar.get()].getBIncr()
        
        # Store current selection in prevSpecies in case of changes

        prevSpecies = speciesSelectVar.get()

        updateStats()
        
    # Initialize window and disable generate button

    scoreWin = Toplevel(root)
    scoreWin.title("Class Selection")
    generate.config(state = DISABLED)

    aScoreFrame1 = LabelFrame(scoreWin, width = 300, text = "Ability Scores")
    aScoreFrame1.grid(column = 0, row = 1, ipadx = 115, padx = 10, pady = 10, sticky = W)

    classFrame = LabelFrame(scoreWin, text = "Class selection")
    classFrame.grid(column = 1, row = 1, sticky = E)

    confirmAScores = Button(scoreWin, text = "Confirm", command = speciesWindow).grid(column = 1, row = 3, pady = 40)

    # create text boxes to display ability scores

    strLbl1 = Label(aScoreFrame1, text = "STR ").grid(row = 0, column = 0, sticky = W)
    dexLbl1 = Label(aScoreFrame1, text = "DEX ").grid(row = 1, column = 0, sticky = W)
    conLbl1 = Label(aScoreFrame1, text = "CON ").grid(row = 2, column = 0, sticky = W)
    intLbl1 = Label(aScoreFrame1, text = "INT ").grid(row = 3, column = 0, sticky = W)
    wisLbl1 = Label(aScoreFrame1, text = "WIS ").grid(row = 4, column = 0, sticky = W)
    chrLbl1 = Label(aScoreFrame1, text = "CHR ").grid(row = 5, column = 0, sticky = W)

    strBox1 = Entry(aScoreFrame1, width = 3)
    dexBox1 = Entry(aScoreFrame1, width = 3)
    conBox1 = Entry(aScoreFrame1, width = 3)
    intBox1 = Entry(aScoreFrame1, width = 3)
    wisBox1 = Entry(aScoreFrame1, width = 3)
    chrBox1 = Entry(aScoreFrame1, width = 3)

    strBox1.grid(row = 0, column = 1, sticky = W)
    dexBox1.grid(row = 1, column = 1, sticky = W)
    conBox1.grid(row = 2, column = 1, sticky = W)
    intBox1.grid(row = 3, column = 1, sticky = W)
    wisBox1.grid(row = 4, column = 1, sticky = W)
    chrBox1.grid(row = 5, column = 1, sticky = W)

    # Generate character stats
    global stats
    stats = assignStats()

    # Display stats as assigned

    strBox1.configure(state = NORMAL)
    dexBox1.configure(state = NORMAL)
    conBox1.configure(state = NORMAL)
    intBox1.configure(state = NORMAL)
    wisBox1.configure(state = NORMAL)
    chrBox1.configure(state = NORMAL)

    strBox1.insert(0,stats[0])
    dexBox1.insert(0,stats[1])
    conBox1.insert(0,stats[2])
    intBox1.insert(0,stats[3])
    wisBox1.insert(0,stats[4])
    chrBox1.insert(0,stats[5])

    strBox1.configure(state = "readonly")
    dexBox1.configure(state = "readonly")
    conBox1.configure(state = "readonly")
    intBox1.configure(state = "readonly")
    wisBox1.configure(state = "readonly")
    chrBox1.configure(state = "readonly")

    
    # This whole following section could probably be cleaned up
    # Determine index of highest stat value(s) for class selection
    tops = []
    for i in range(len(stats)):
        
        if stats[i] == max(stats):
            tops.append(i)

    
    # Build high ability list

    highA = []

    for e in tops:
        match e:
            case 0:
                highA.append("STR")
            case 1:
                highA.append("DEX")
            case 2:
                highA.append("CON")
            case 3:
                highA.append("INT")
            case 4:
                highA.append("WIS")
            case 5:
                highA.append("CHR")

    # If only one high value, determine second highest value(s)
    
    seconds = []

    if len(highA) == 1:
        
        second = []
        second.extend(stats)

        # Sets highest value to 0 to check for next highest value, but retain index

        second[tops[0]] = 0

        # Loops to find highest remaining score
        for i in range(len(second)):
            if stats[i] == max(second):
                seconds.append(i)
    
    

    # Makes a list of second highest stat(s)
    
    
    secondA = []

    for e in seconds:
        match e:
            case 0:
                secondA.append("STR")
            case 1:
                secondA.append("DEX")
            case 2:
                secondA.append("CON")
            case 3:
                secondA.append("INT")
            case 4:
                secondA.append("WIS")
            case 5:
                secondA.append("CHR")    

    # Checks for edge case where CON alone is highest, which is incompatible with valid classes
    # Reassigns second highest score(s) to highest

    if len(highA) == 1 and highA[0] == "CON":
        highA.extend(secondA)
   
    # Creating a valid playerClass list by primaryStat attribute

    classList = []

    for c in classes:
        if c.getPrimaryStat() in highA:
            classList.append(c)

    # Build radio buttons for all valid classes
    
    global classSelectVar
    classSelectVar = StringVar()
    
    for j in classList:
        Radiobutton(classFrame, text = j.getTitle(), variable = classSelectVar, value = j.getTitle(), command = classUpdate).grid(sticky = W)

    # Remove classes incompatible with secondary stat values from recommendation list

    for j in classList:
        if j.getSecondaryStat() not in secondA and j.getSecondaryStat() not in highA and len(classList) > 1:
            classList.pop(classList.index(j))    
    
    # Pick one class for default setting

    classPick = classList[random.randint(0, (len(classList) - 1))]
    
    for rb in filter(lambda w:isinstance(w,Radiobutton), classFrame.children.values()):
        if rb.cget("value") == classPick.title:
            rb.invoke()

    # On close action

    scoreWin.protocol("WM_DELETE_WINDOW", scoreWinClose)

# -----------------------------------------------------------------------------    
   
def genStatPool():

    ''' Generates stat scores
        Rolls 4 six sided dice, discards the lowest, and adds remaining total to list
        Generates 7 such numbers and discards the lowest'''
    
    # Allows access to box values
    
    strBox.configure(state = NORMAL)
    dexBox.configure(state = NORMAL)
    conBox.configure(state = NORMAL)
    intBox.configure(state = NORMAL)
    wisBox.configure(state = NORMAL)
    chrBox.configure(state = NORMAL)

    # Prepares list for seven scores
    statPool = []

    # Generates the seven scores

    for i in range(7):

        # Prepares list for 4 numbers to discard the lowest

        sorter = []
        
        # Generates the 4 rolls

        for x in range (4):
            raw = random.randint(1,6)
            sorter.append(raw)

        # Removes lowest roll and adds sum to statPool

        sorter.sort()
        sorter.pop(0)
        statPool.append(sum(sorter))
    
    # Removes lowest score and returns the list

    statPool.sort()
    statPool.pop(0)
    return statPool

# -----------------------------------------------------------------------------

def assignStats():
    statPool = genStatPool()
    random.shuffle(statPool)
    
    
    
    '''
    
    '''


    return statPool


# -----------------------------------------------------------------------------

def updateStats():

    # Clear stat value boxes
        
        strBox.configure(state = NORMAL)
        dexBox.configure(state = NORMAL)
        conBox.configure(state = NORMAL)
        intBox.configure(state = NORMAL)
        wisBox.configure(state = NORMAL)
        chrBox.configure(state = NORMAL)

        strBox.delete(0,END)
        dexBox.delete(0,END)
        conBox.delete(0,END)
        intBox.delete(0,END)
        wisBox.delete(0,END)
        chrBox.delete(0,END)

        # Display stat assignments on root

        strBox.insert(0,stats[0])
        dexBox.insert(0,stats[1])
        conBox.insert(0,stats[2])
        intBox.insert(0,stats[3])
        wisBox.insert(0,stats[4])
        chrBox.insert(0,stats[5])

        # disable user input

        strBox.configure(state = "readonly")
        dexBox.configure(state = "readonly")
        conBox.configure(state = "readonly")
        intBox.configure(state = "readonly")
        wisBox.configure(state = "readonly")
        chrBox.configure(state = "readonly")

# Build list of valid classes and their attributes from library

def readClasses():
    c = open("classes.txt","r")
    classes = []
    for l in c:
        l = l.strip()
        classAttr = l.split(',')
        classes.append(playerClass(classAttr[0],classAttr[1],classAttr[2],classAttr[3]))
    c.close()

    c = open("subClasses.txt","r")
    for l in c:
        l = l.strip()
        subClasses = l.split(',')
        for j in classes:
            if subClasses[0] == j.title:
                subClasses.pop(0)
                j.subClass.extend(subClasses)
    c.close()
    return classes
    
classes = readClasses()

# Build list of species from library

def readSpecies():
    f = open("species.txt","r")
    speciesList = []
    for l in f:
        l = l.strip()
        speciesAttr = l.split(',')
        speciesList.append(species(speciesAttr[0],speciesAttr[1],speciesAttr[2],speciesAttr[3],speciesAttr[4],speciesAttr[5]))
    f.close()
    return speciesList

speciesList = readSpecies()

global prevSpecies
prevSpecies = 0

# Create and place button to run selected functions

generate = Button(topFrame, text = "Generate", command = scoreGenWin)
generate.grid(sticky = E, row = 0, column = 2, padx = 50, pady = 50)

# Create frames for user options

'''

selectionFrame = LabelFrame(topFrame, width = 300, text = "Select the characteristics to randomize")
selectionFrame.grid(row = 0, column = 0, ipadx = 50, padx = 10, pady = 10, sticky = W)
selectionFrame

'''

aScoreFrame = LabelFrame(topFrame, width = 300, text = "Ability Scores")
aScoreFrame.grid(column = 0, row = 0, ipadx = 115, padx = 10, pady = 10, sticky = W)

infoFrame = LabelFrame(topFrame, text = "Information")
infoFrame.grid(column = 0, row = 1, ipadx = 119, padx = 10, pady = 10, sticky = W)


'''
# Create check boxes so user can determine which characteristics to generate
aScore = 0
cClass = 0
subClass = 0
species = 0
background = 0



Checkbutton(selectionFrame, text = "Ability Scores", variable = aScore).grid(row = 1, sticky = W)
Checkbutton(selectionFrame, text = "Class", variable = cClass).grid(row = 2, sticky = W)
Checkbutton(selectionFrame, text = "Species", variable = species).grid(row = 3, sticky = W)
Checkbutton(selectionFrame, text = "Background", variable = background).grid(row = 4, sticky = W)

'''

# create text boxes to display ability scores

strLbl = Label(aScoreFrame, text = "STR ").grid(row = 0, column = 0, sticky = W)
dexLbl = Label(aScoreFrame, text = "DEX ").grid(row = 1, column = 0, sticky = W)
conLbl = Label(aScoreFrame, text = "CON ").grid(row = 2, column = 0, sticky = W)
intLbl = Label(aScoreFrame, text = "INT ").grid(row = 3, column = 0, sticky = W)
wisLbl = Label(aScoreFrame, text = "WIS ").grid(row = 4, column = 0, sticky = W)
chrLbl = Label(aScoreFrame, text = "CHR ").grid(row = 5, column = 0, sticky = W)

strBox = Entry(aScoreFrame, width = 3)
dexBox = Entry(aScoreFrame, width = 3)
conBox = Entry(aScoreFrame, width = 3)
intBox = Entry(aScoreFrame, width = 3)
wisBox = Entry(aScoreFrame, width = 3)
chrBox = Entry(aScoreFrame, width = 3)

strBox.grid(row = 0, column = 1, sticky = W)
dexBox.grid(row = 1, column = 1, sticky = W)
conBox.grid(row = 2, column = 1, sticky = W)
intBox.grid(row = 3, column = 1, sticky = W)
wisBox.grid(row = 4, column = 1, sticky = W)
chrBox.grid(row = 5, column = 1, sticky = W)

# disable user input

strBox.configure(state = "readonly")
dexBox.configure(state = "readonly")
conBox.configure(state = "readonly")
intBox.configure(state = "readonly")
wisBox.configure(state = "readonly")
chrBox.configure(state = "readonly")


# Create output textbox for misc. info

infoLabel = Label(infoFrame, width = 5)
infoLabel.pack()



# Run mainloop

root.mainloop()
