import tkinter as tk


# GPA Calculator - calculating UC GPA
# include: unweighted GPA, UC Capped, Maxed GPA
# semester-based GPA, # of grades



class Main(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('GPA Calculator')
        self.geometry("600x800")
        self.name = tk.Label(self, text='UC GPA', font="Times 20 bold")
        self.name.grid(row=0, column=0)

        # self.label1 = tk.Label(self, text='# of semester total')
        # self.label1.grid(row =1, column=0)
        # self.entry1 = tk.Entry()
        # self.entry1.grid(row=1,column=1)

        self.label2 = tk.Label(self, text="# of A grades")
        self.label2.grid(row=2, column=0)
        self.entry2 = tk.Entry()
        self.entry2.grid(row=2, column=1)

        self.label3 = tk.Label(self, text="# of B grades")
        self.label3.grid(row=3, column=0)
        self.entry3 = tk.Entry()
        self.entry3.grid(row=3, column=1)

        self.label4 = tk.Label(self, text="# of C grades")
        self.label4.grid(row=4, column=0)
        self.entry4 = tk.Entry()
        self.entry4.grid(row=4, column=1)

        self.label5 = tk.Label(self, text="# of D grades")
        self.label5.grid(row=5, column=0)
        self.entry5 = tk.Entry()
        self.entry5.grid(row=5, column=1)

        self.label6 = tk.Label(self, text="# of F grades")
        self.label6.grid(row=6, column=0)
        self.entry6 = tk.Entry()
        self.entry6.grid(row=6, column=1)

        self.label7 = tk.Label(self, text="Honor Points")
        self.label7.grid(row=7, column=0)
        self.entry7 = tk.Entry()
        self.entry7.grid(row=7, column=1)

        self.buttoncal = tk.Button(self, text="Calculate Your GPA", command=lambda: self.showGPA())
        self.buttoncal.grid(row=8, column=1)


    def calculate(self):
        try:

            sum = int(self.entry2.get()) + int(self.entry3.get())+ int(self.entry4.get()) + int(self.entry5.get()) + int(self.entry6.get())

            valueofA = int(self.entry2.get())*4
            valueofB = int(self.entry3.get())*3
            valueofC = int(self.entry4.get())*2
            valueofD = int(self.entry5.get())*1
            honorpoint = int(self.entry7.get())

            GPA = float(((valueofA + valueofB + valueofC + valueofD + honorpoint) / sum))
            output = round(GPA,2)
            return output

        except ValueError:
            return ("""Please try again. Make sure that ALL inputs are numerical value.
                    If you do not have [Letter Grade], insert 0. 
                    """)



    def showGPA(self):
        value = Main.calculate(self)
        toplevel = tk.Toplevel()
        lab1 = tk.Label(toplevel, text="This is your UC GPA:", height=0, width=50)
        lab1.pack()
        lab2 = tk.Label(toplevel, text=value, height=10, width=50)
        lab2.pack()


if __name__ == "__main__":
    app = Main()
    app.mainloop()

#
