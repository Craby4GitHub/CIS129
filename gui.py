import tkinter
import tkinter.messagebox

class MyGUI:

    def __init__(self):
        #create the main windows widget
        self.mainWindow = tkinter.Tk()

        # Frames
        self.topFrame = tkinter.Frame(self.mainWindow)
        self.bottomFrame = tkinter.Frame(self.mainWindow)

        # Check Boxes
        self.cbVar1 = tkinter.IntVar()
        self.cbVar2 = tkinter.IntVar()
        self.cbVar3 = tkinter.IntVar()

        # Check box start with no value
        self.cbVar1.set(0)
        self.cbVar2.set(0)
        self.cbVar3.set(0)

        # Make widget for Check box
        self.cb1 = tkinter.Checkbutton(self.topFrame, text="Hotdog", variable=self.cbVar1)
        self.cb2 = tkinter.Checkbutton(self.topFrame, text="Hamburger", variable=self.cbVar2)
        self.cb3 = tkinter.Checkbutton(self.topFrame, text="Taco", variable=self.cbVar3)


        self.label = tkinter.Label(self.topFrame,text='Hello World')

        self.label.pack()

        # Button
        self.pushMeButton = tkinter.Button(self.bottomFrame, text='Click me mofo!', command=self.pushedButton)
        self.quitButton = tkinter.Button(self.bottomFrame, text="Don't Click me mofo!", command=self.mainWindow.destroy)

        self.pushMeButton.pack(side='left')
        self.quitButton.pack(side='left')
        self.topFrame.pack()
        self.bottomFrame.pack()
        self.cb1.pack(side='left')
        self.cb2.pack(side='left')
        self.cb3.pack(side='left')

        self.nameLabel = tkinter.Label(self.topFrame, text='name')
        self.textBox = tkinter.Entry(self.topFrame, width=60)
        self.nameLabel.pack()
        self.textBox.pack()



        tkinter.mainloop()

        # event handler
    def pushedButton(self):
        self.message = self.textBox.get() + '\s'
        self.message = 'Your favorite food:\n'
        if self.cbVar1.get() == 1:
            self.message = self.message + 'Hotdog\n'
        if self.cbVar2.get() == 1:
            self.message = self.message + 'Hamburger\n'
        if self.cbVar3.get() == 1:
            self.message = self.message + 'Taco\n'
        tkinter.messagebox.showinfo('Select favorite food', self.message)

myGUI = MyGUI()

