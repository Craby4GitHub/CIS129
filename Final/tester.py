from tkinter import *

from tkinter import messagebox

main = Tk()
main.wm_title("")
main.geometry("200x150")

usersNum = [0, 0, 0]
genNum = [0, 0, 0]

fourth = '({})  [{}]  ({})'.format(genNum[0], usersNum[1], genNum[2])
second = '[{}]'.format(usersNum[2]).center(int(len(fourth) / 2), ' ')
third = '[{}]'.format(usersNum[0]).center(int(len(fourth) / 2), ' ')
first = '({})'.format(genNum[1]).center(int(len(second) + len(third)), ' ')

triangle = [fourth, second, third, first]


def submitCallBack():
    message = [E1.get(), E2.get(), E3.get()]
    for i in range(3):
        if -40 <= int(message[i]) <= 40:
            if i == 2:
                msg = messagebox.showinfo("Finished Triangle", triangle)
        else:
            msg = messagebox.showinfo("Out of Range", "You put a value outside of the range.")
            break

# Get the total sum of numbers inputted and half it
totalSum = int(sum(usersNum))/2

# Subtract the sum from the opposite number and input that value into genNum
for i in range(3):
    genNum[i] = totalSum - int(usersNum[i])

submitButton = Button(main, text="Submit", command=submitCallBack)

L1 = Label(main, text="First Number:")
L2 = Label(main, text="Second Number:")
L3 = Label(main, text="Third Number:")

E1 = Entry(main, bd=10, width=5)
E2 = Entry(main, bd=10, width=5)
E3 = Entry(main, bd=10, width=5)

usersNum[0] = E1.get()
usersNum[1] = E2.get()
usersNum[2] = E3.get()

L1.grid(row=0, column=0)
E1.grid(row=0, column=1)
L2.grid(row=1, column=0)
E2.grid(row=1, column=1)
L3.grid(row=2, column=0)
E3.grid(row=2, column=1)
submitButton.grid(row=3, column=1)

main.mainloop()
