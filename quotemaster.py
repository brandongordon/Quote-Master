import tkinter
import tkinter.messagebox
import json
import random

class ProgramGUI:

    def __init__(self):        
        self.main = tkinter.Tk()    #Creates the main window of the program.
        self.main.title ("QuoteMaster")    #Requirement #1.

        print ("The shell is going to be full of debug info, ignore it if you wish!")

        try:
            f = open('data.txt', 'r')    #Open the file in read mode and assigns information to variable 'f'.
            self.data = json.load(f)    #Read the json data from 'f' into the 'self.data' attribute. Requirement #2.
            f.close()    
            print ("Loaded data from file")   
        except:
            print ("data.txt does not exist!")
            tkinter.messagebox.showerror("Missing File", "data.txt does not exist!")
            self.main.destroy()
            print("Program has terminated")
            return

        self.authors = set()
        for quoteInfo in self.data:
            self.authors.add(quoteInfo['Author'])    #Loops through the data list and stores dictionary items with key "Author" into the buffer, and then adds them to the self.authors set.
        if len(self.authors) < 3:    #Requirement 3.
            tkinter.messagebox.showerror("Insufficient Number of Authors", "At least 3 authors need to exist in the database")
            self.main.destroy()
            print ("Program has terminated")
            return
      
        self.score = 0
        self.questionCount = 0    #Requirement 4.
        
        #create frame widgets
        self.top = tkinter.Frame(self.main, pady=5)
        self.middle = tkinter.Frame(self.main)
        self.bottom = tkinter.Frame(self.main, padx=100, pady=10)

        #create and pack content into frames
        self.whoSaid = tkinter.Label(self.top, width=25, text='Who said...', justify='center')
        self.quoteLabel = tkinter.Label(self.middle, wraplength=400, justify='center' )
        self.buttonLeft = tkinter.Button(self.bottom)
        self.buttonMiddle = tkinter.Button(self.bottom)
        self.buttonRight = tkinter.Button(self.bottom)
        
        self.whoSaid.pack()
        self.quoteLabel.pack()
        self.buttonLeft.pack(side='left')
        self.buttonMiddle.pack(side='left')
        self.buttonRight.pack(side='left')

        #pack the frames
        self.top.pack()
        self.middle.pack()
        self.bottom.pack()    #Requirement #5.

        self.loadQuote()
        
        tkinter.mainloop()    #Should be called once your GUI is ready to run. Requirement #6.
        

    def loadQuote(self):
        self.selectedQuote = random.choice(self.data)    #Select the dictionary entry that we will use for the correct answer
        print ("\nQUOTE INFORMATION BEING TESTED: ", self.selectedQuote)
        self.authors.remove(self.selectedQuote["Author"])    #Remove the chosen quote from self.authors
        btnAuthors = random.sample(self.authors, 2)    
        btnAuthors.append(self.selectedQuote["Author"])    #Append the correct answer to the list of authors displayed
        self.authors.add(self.selectedQuote["Author"])    #Add the selected quote back into the pool
        random.shuffle(btnAuthors)
        lblQuote = '"' + self.selectedQuote ["Quote"] + '"'
        print ("AUTHORS USED IN BUTTONS: ", btnAuthors)
        
        self.quoteLabel.configure(text=lblQuote)
        self.buttonLeft.configure(text=btnAuthors[0], command=lambda: self.checkAnswer(btnAuthors[0]))
        self.buttonMiddle.configure(text=btnAuthors[1], command=lambda: self.checkAnswer(btnAuthors[1]))
        self.buttonRight.configure(text=btnAuthors[2], command=lambda: self.checkAnswer(btnAuthors[2]))

        self.questionCount += 1
        print ("QUESTION COUNT: ", self.questionCount)


    def checkAnswer(self, chosenName):
        print ("CHOSEN AUTHOR :", chosenName)
        if chosenName == self.selectedQuote["Author"]:
            print ("Answer: CORRECT")
            self.score += 1
            print ("SCORE: ", self.score)
            tkinter.messagebox.showinfo ("Correct", "You Are Correct! \nYour score is: " + str(self.score) + "/" + str(self.questionCount))
        else:
            print ("Answer: INCORRECT")
            tkinter.messagebox.showerror ("Incorrect", "Sorry, that was incorrect! \nYour score is: " + str(self.score) + "/" + str(self.questionCount))

        self.loadQuote()


gui = ProgramGUI()    #Calling the constructor
