'''
Cliff Choate
Final Project
Random generation of tabletop RPG (Dungeons & Dragons, 5th edition) character
v0.1
07/13/2024
'''

from tkinter import*

# Create root

root = Tk()
root.title("Character Generator")
root.geometry('900x800+50+30')
topFrame = Frame(root)
topFrame.pack(side = BOTTOM, fill = BOTH, expand = TRUE)


# Define Functions (Will move this to library and import later)

def genWindow():
    window = Toplevel(root)
    window.title("Results")

# Create frames for user options

selectionFrame = LabelFrame(topFrame, padx =10, text = "Select the characteristics to randomize")
selectionFrame.pack(side = LEFT, anchor = NW, fill = NONE, expand = FALSE)

aScoreFrame = LabelFrame(topFrame, padx = 10, text = "Ability Scores")
aScoreFrame.pack(side = LEFT, anchor = SW, fill = NONE, expand = FALSE)

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

# create text boxes to display ability scores

strLbl = Label(aScoreFrame, text = "STR ").grid(row = 0, column = 0, sticky = W)
dexLbl = Label(aScoreFrame, text = "DEX ").grid(row = 1, column = 0, sticky = W)
conLbl = Label(aScoreFrame, text = "CON ").grid(row = 2, column = 0, sticky = W)
intLbl = Label(aScoreFrame, text = "INT ").grid(row = 3, column = 0, sticky = W)
wisLbl = Label(aScoreFrame, text = "WIS ").grid(row = 4, column = 0, sticky = W)
chrLbl = Label(aScoreFrame, text = "CHR ").grid(row = 5, column = 0, sticky = W)

strBox = Entry(aScoreFrame, width = 5)
dexBox = Entry(aScoreFrame, width = 5)
conBox = Entry(aScoreFrame, width = 5)
intBox = Entry(aScoreFrame, width = 5)
wisBox = Entry(aScoreFrame, width = 5)
chrBox = Entry(aScoreFrame, width = 5)

strBox.grid(row = 0, column = 1, sticky = W)
dexBox.grid(row = 1, column = 1, sticky = W)
conBox.grid(row = 2, column = 1, sticky = W)
intBox.grid(row = 3, column = 1, sticky = W)
wisBox.grid(row = 4, column = 1, sticky = W)
chrBox.grid(row = 5, column = 1, sticky = W)

# disable user input

strBox.configure(state = DISABLED)
dexBox.configure(state = DISABLED)
conBox.configure(state = DISABLED)
intBox.configure(state = DISABLED)
wisBox.configure(state = DISABLED)
chrBox.configure(state = DISABLED)

# Create and place button to run selected functions

generate = Button(topFrame, text = "Generate", command = genWindow)
generate.pack()







# Run mainloop

root.mainloop()