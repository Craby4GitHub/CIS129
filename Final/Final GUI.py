import tkinter as Tk

class MyApp(object):

    def __init__(self, parent):
        self.root = parent
        self.root.title("Main Frame")
        self.frame = Tk.Frame(parent)
        self.frame.pack()

        submitbtn = Tk.Button(self.frame, text="Submit", command=self.openFrame)
        submitbtn.pack()

    def hide(self):

        self.root.withdraw()

    def openFrame(self):

        self.hide()
        answerFrame = Tk.TopLevel()
        answerFrame.geometry("400x300")
        answerFrame.title("Finished Triangle")
        handler = lambda: self.onCloseAnswerFrame(answerFrame)
        againbtn = Tk.Button(answerFrame, text="Another set", command=handler)
        againbtn.pack()

    def onCloseAnswerFrame(self, answerframe):

        answerFrame.destroy()
        self.show()

    def show(self):

        self.root.update()
        self.root.deiconify()

if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()