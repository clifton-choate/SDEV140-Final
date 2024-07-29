'''
Cliff Choate
Final Project
Random generation of tabletop RPG (Dungeons & Dragons, 5th edition) character
v1.0
07/28/2024
'''

import os 
from tkinter import*
from Character_Randomizer_Supplement import*
import random

supplementPath = os.getcwd() + "\\Supplements\\"

# Create root

root = Tk()
root.title("Character Generator")
root.geometry('700x500+50+30')
topFrame = Frame(root)
topFrame.pack(side = BOTTOM, fill = BOTH, expand = TRUE)


# Define Functions (Will move this to library and import later)

def scoreGenWin():
    
    global playerC
    playerC = character("Name", None, cClass = "Fighter", cSubClass = "N/A", cSpecies = "Hill Dwarf", cBackground = "Soldier")

    # Initialize function level variables

    def speciesWindow():

        def speciesWinClose():
            scoreWinClose()
            speciesWin.destroy()

        def backgroundsWindow():
            
            # Assign species to player

            playerC.setSpecies(speciesList[speciesSelectVar.get()].getName())
            playerC.setAScores(stats)

            # Builds background selection window

            def bgWinRun():
                bgWin = Toplevel(root)
                bgWin.geometry("400x600+200+100")
                bgWin.title("Backgrounds")
                bgWin.focus_force()
                speciesWin.destroy()

                # Assigns variable for radio buttons

                bgSelectVar = StringVar()

                # Button to confirm selection and finish character

                def bgConfirm():
                    playerC.setBackground(bgSelectVar.get())
                    displayCharacter()
                    generate.configure(state = NORMAL)
                    bgWin.destroy()
                bgRadioList = []
                r = 0
                for bg in bgList:
                    bgRadioList.append(Radiobutton(bgWin, text = bg, variable = bgSelectVar, value = bg))
                    bgRadioList[r].grid(row = r, column = 0, sticky = W)
                    r += 1
                bgRadioList[random.randint(0, len(bgRadioList)-1)].select()
                confirmBg = Button(bgWin, text = "Finish", command = bgConfirm)
                confirmBg.grid(column = 3, row = 12, sticky = E)

                




            # Opens subclass window if required
            
            if classes[classSelectVar.get()].getSubReq() == True:
                subWin = Toplevel(root)
                subWin.geometry("400x400+200+100")
                subWin.title("SubClass")
                subWin.focus_force()
                speciesWin.destroy()

                # Assigns subclass and opens next window

                def subConfirm():
                    playerC.setSubClass(subSelectVar.get())
                    bgWinRun()
                    subWin.destroy()

                # Displays subclass options

                Label(subWin, text = "Subclasses").grid(row = 0, column = 0, sticky = W)
                subSelectVar = StringVar()
                
                # Builds radio buttons with a loop
                buttonList = []
                for sc in classes[classSelectVar.get()].getSubClass():
                    buttonList.append(Radiobutton(subWin, text = sc, variable = subSelectVar, value = sc))
                c = 0
                for b in buttonList:
                    b.grid(row = c, column = 0, sticky = W)
                    c += 1
                buttonList[random.randint(0, len(buttonList) - 1)].select()

                # Builds confirm button to confirm selection

                confirmSub = Button(subWin, text = "Confirm", command = subConfirm)
                confirmSub.grid(column = 1, row = 12, columnspan = 2, sticky = E)

            else:

                # Opens background selection window if no subclass required

                bgWinRun()


        
        
        
        
        # Assign class to player

        playerC.setClass(classes[classSelectVar.get()].getTitle())
        playerC.setProficiencies(classes[classSelectVar.get()].getProfs())

        # Open species select window

        speciesWin = Toplevel(root)
        speciesWin.geometry("400x400+200+100")
        speciesWin.title("Species Selection")
        speciesWin.focus_force()
        scoreWin.destroy()

        confirmSpecies = Button(speciesWin, text = "Confirm", command = backgroundsWindow).grid(row = 12, column = 2, sticky = E)
        
        

        # Build radio buttons from species list

        global speciesSelectVar
        
        speciesSelectVar = IntVar(root,value = 0)

        
        # Builds radio buttons with a loop
        
        speciesButtonList = []

        for sp in speciesList:
            speciesButtonList.append(Radiobutton(speciesWin, text = sp.getName(), variable = speciesSelectVar, value = sp.getSpIndex(), command = speciesUpdate))
        c = 0
        for b in speciesButtonList:
            b.grid(row = c, column = 0, sticky = W)
            c += 1
        speciesButtonList[random.randint(0, len(speciesButtonList) - 1)].select()

        # Add stat bonus for default species

        stats[speciesList[speciesSelectVar.get()].getStatA()] += speciesList[speciesSelectVar.get()].getAIncr()
        stats[speciesList[speciesSelectVar.get()].getStatB()] += speciesList[speciesSelectVar.get()].getBIncr()
        
        
        speciesWin.protocol("WM_DELETE_WINDOW", speciesWinClose)

    
    # Define on close actions

    def scoreWinClose():
        
        # Re-enables generate button when window is closed

        generate.configure(state = NORMAL)
        scoreWin.destroy()

    # Defines actions to be taken on class selection

    def classUpdate():
        for cb in proficiencyBoxes:
            cb.deselect()
        for cl in classList:
            if classSelectVar == cl.getClIndex():
                for p in cl.getProfs():
                    proficiencyBoxes[p].select()
            
            
    
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

        # updateStats(stats)
        
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
    playerC.setAScores(stats)

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
    classSelectVar = IntVar()
    
    for j in classList:
        t = Radiobutton(classFrame, text = j.getTitle(), variable = classSelectVar, value = j.getClIndex(), command = classUpdate)
        t.grid(sticky = W)

    # Remove classes incompatible with secondary stat values from recommendation list

    for j in classList:
        if j.getSecondaryStat() not in secondA and j.getSecondaryStat() not in highA and len(classList) > 1:
            classList.pop(classList.index(j))    
    
    # Pick one class for default setting

    classPick = classList[random.randint(0, (len(classList) - 1))]
    
    for rb in filter(lambda w:isinstance(w,Radiobutton), classFrame.children.values()):
        if rb.cget("value") == classPick.getTitle():
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

# Randomly assings stats

def assignStats():
    statPool = genStatPool()
    random.shuffle(statPool)
    return statPool


# -----------------------------------------------------------------------------

# Updates stat boxes on main window

def updateStats(stats):

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

        # Update proficiency checkboxes

# Build tuple of classes and their attributes from library

def readClasses():
    c = open(supplementPath + "classes.txt","r")
    classes = ()
    for l in c:
        l = l.strip()
        classAttr = l.split(',')
        classes += playerClass(classAttr[0],classAttr[1],classAttr[2],classAttr[3],classAttr[4],classAttr[5],classAttr[6]),
    c.close()
    
    # For classes requiring a subclass at creation, add tuple of possible subclasses to the instance
    
    c = open(supplementPath + "subClasses.txt","r")
    for l in c:
        l = l.strip()
        subClasses = l.split(',')
        for j in classes:
            if subClasses[0] == j.title:
                subClasses.pop(0)
                j.setSubClass(tuple(subClasses))
    c.close()

    return classes
    
classes = readClasses()

# Build tuple of species from library

def readSpecies():
    f = open(supplementPath + "species.txt","r")
    speciesList = ()
    for l in f:
        l = l.strip()
        speciesAttr = l.split(',')
        speciesList += species(speciesAttr[0],speciesAttr[1],speciesAttr[2],speciesAttr[3],speciesAttr[4],speciesAttr[5]),
    f.close()
    return speciesList

speciesList = readSpecies()

# Build tuple of backgrounds from library

def readBgs():
    f = open(supplementPath + "backgrounds.txt","r")
    bgList = ()
    for l in f:
        l.strip('\n')
        bgList += l,
    f.close()
    return bgList

bgList = readBgs()

# Build tuple of random names from library

def readNames():
    f = open(supplementPath + "names.txt","r")
    nameList = ()
    for l in f:
        l.strip('\n')
        nameList += l,
    f.close()
    return nameList

nameList = readNames()

# Display information about player character instance

def displayCharacter():
    updateStats(playerC.getAScores())
    
    # Check boxes corresponding to player's saving throw proficiencies

    for box in proficiencyBoxes:
        box.deselect()
    for prof in playerC.getProficiencies():
        proficiencyBoxes[int(prof)].select()
   
    # Display characer info in boxes

    classBox.configure(state = NORMAL)
    subClassBox.configure(state = NORMAL)
    speciesBox.configure(state = NORMAL)
    backgroundBox.configure(state = NORMAL)

    nameBox.delete(0, END)
    classBox.delete(0, END)
    subClassBox.delete(0, END)
    speciesBox.delete(0, END)
    backgroundBox.delete(0, END)
    
    nameBox.insert(0, playerC.getName())
    classBox.insert(0, playerC.getClass())
    subClassBox.insert(0, playerC.getSubClass())
    speciesBox.insert(0, playerC.getSpecies())
    backgroundBox.insert(0, playerC.getBackground())

    
    classBox.configure(state = 'readonly')
    subClassBox.configure(state = 'readonly')
    speciesBox.configure(state = 'readonly')
    backgroundBox.configure(state = 'readonly')

    # Display an icon representing the class

    #classIconPath = os.getcwd() + "\\Images\\" + playerC.getClass().lower() + ".png"
    
    #supplementPath = os.getcwd() + "\\Supplements\\"

    global classIcon
    classIcon = PhotoImage(file = supplementPath + playerC.getClass().lower() + ".png")
    classIconLabel = Label(infoFrame, image = classIcon)
    classIconLabel.grid(row = 0, rowspan = 5, column = 3, sticky = E)
    #classIconLabel.configure()

def randoName():
    playerC.setName(nameList[random.randint(0,len(nameList) - 1)])
    displayCharacter()



global prevSpecies
prevSpecies = 0


# Create and place button to run selected functions

generate = Button(topFrame, text = "Generate", command = scoreGenWin)
generate.grid(sticky = E, row = 0, column = 2, padx = 50, pady = 50)

randomName = Button(topFrame, text = "Random Name", command = randoName)
randomName.grid(sticky = E, row = 1, column = 2, padx = 50, pady = 50)

# Create frames for output 

aScoreFrame = LabelFrame(topFrame, width = 300, text = "Ability Scores")
aScoreFrame.grid(column = 0, row = 0, ipadx = 115, padx = 10, pady = 10, sticky = W)

infoFrame = LabelFrame(topFrame, text = "Information")
infoFrame.grid(column = 0, row = 1, padx = 10, pady = 10, sticky = W)

# create text boxes to display ability scores

strLbl = Label(aScoreFrame, text = "Strength     (STR) ").grid(row = 1, column = 0, sticky = W)
dexLbl = Label(aScoreFrame, text = "Dexterity    (DEX) ").grid(row = 2, column = 0, sticky = W)
conLbl = Label(aScoreFrame, text = "Constitution (CON) ").grid(row = 3, column = 0, sticky = W)
intLbl = Label(aScoreFrame, text = "Intelligence (INT) ").grid(row = 4, column = 0, sticky = W)
wisLbl = Label(aScoreFrame, text = "Wisdom       (WIS) ").grid(row = 5, column = 0, sticky = W)
chrLbl = Label(aScoreFrame, text = "Charisma     (CHR) ").grid(row = 6, column = 0, sticky = W)

strBox = Entry(aScoreFrame, width = 3)
dexBox = Entry(aScoreFrame, width = 3)
conBox = Entry(aScoreFrame, width = 3)
intBox = Entry(aScoreFrame, width = 3)
wisBox = Entry(aScoreFrame, width = 3)
chrBox = Entry(aScoreFrame, width = 3)

strBox.grid(row = 1, column = 1, sticky = W)
dexBox.grid(row = 2, column = 1, sticky = W)
conBox.grid(row = 3, column = 1, sticky = W)
intBox.grid(row = 4, column = 1, sticky = W)
wisBox.grid(row = 5, column = 1, sticky = W)
chrBox.grid(row = 6, column = 1, sticky = W)

# Create checkboxes to show saving throw proficiency
profLabel = Label(aScoreFrame,text = "Proficient").grid(row = 0, column = 2, sticky = N)

# Uses loop to create list of checkboxes

proficiencyBoxes = []
for i in range(6):
    proficiencyBoxes.append(Checkbutton(aScoreFrame))
    proficiencyBoxes[i].grid(row = (i + 1), column = 2, sticky = W)
    proficiencyBoxes[i].configure(state = "disabled")

# disable user input

strBox.configure(state = "readonly")
dexBox.configure(state = "readonly")
conBox.configure(state = "readonly")
intBox.configure(state = "readonly")
wisBox.configure(state = "readonly")
chrBox.configure(state = "readonly")

# Create output textbox for misc. info

nameLabel = Label(infoFrame, text = "Name").grid(row = 0, column = 0, padx = 10, sticky = W)
classLabel = Label(infoFrame, text = "Class").grid(row = 1, column = 0, padx = 10, sticky = W)
subclassLabel = Label(infoFrame, text = "Sub-Class").grid(row = 2, column = 0, padx = 10, sticky = W)
speciesLabel = Label(infoFrame, text = "Species").grid(row = 3, column = 0, padx = 10, sticky = W)
backgroundLabel = Label(infoFrame, text = "Background").grid(row = 4, column = 0, padx = 10, sticky = W)

nameBox = Entry(infoFrame, width = 22)
classBox = Entry(infoFrame, width = 22)
subClassBox = Entry(infoFrame, width = 22)
speciesBox = Entry(infoFrame, width = 22)
backgroundBox = Entry(infoFrame, width = 22)

nameBox.grid(row = 0, column = 1, padx = 10, sticky = E)
classBox.grid(row = 1, column = 1, padx = 10, sticky = E)
subClassBox.grid(row = 2, column = 1, padx = 10, sticky = E)
speciesBox.grid(row = 3, column = 1, padx = 10, sticky = E)
backgroundBox.grid(row = 4, column = 1, padx = 10, sticky = E)




# Run mainloop

root.mainloop()