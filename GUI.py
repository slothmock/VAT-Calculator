from tkinter import *

class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Ultimate VAT Calculator")
        self.window.configure(bg='darkgray')
        self.window.resizable(False, False)
        self.window.columnconfigure(3, weight=1)
        self.window.rowconfigure(6, weight=1)

        # center the window
        winWidth = self.window.winfo_reqwidth()
        winwHeight = self.window.winfo_reqheight()
        posRight = int(self.window.winfo_screenwidth() / 2 - winWidth / 2)
        posDown = int(self.window.winfo_screenheight() / 2 - winwHeight / 2)
        self.window.geometry(f"+{posRight}+{posDown}")

        # create a quantity label
        self.quantityLabel = Label(self.window, text="Enter the quantity of the item:")
        self.quantityLabel.configure(bg='darkgray')
        self.quantityLabel.grid(row=0, column=0, sticky=W)

        # create a quantity entry
        self.quantityEntry = Entry(self.window)
        self.quantityEntry.grid(row=0, column=1, sticky=W)

        # create a price label
        self.priceLabel = Label(self.window, text="Enter the price of the item:")
        self.priceLabel.configure(bg='darkgray')
        self.priceLabel.grid(row=1, column=0, sticky=W)

        # create a price entry
        self.priceEntry = Entry(self.window)
        self.priceEntry.grid(row=1, column=1, sticky=W)
        
        # create VAT rate selector buttons
        self.vatRateLabel = Label(self.window, text="Select the VAT rate:")
        self.vatRateLabel.configure(bg='darkgray')
        self.vatRateLabel.grid(row=4, column=0, sticky=W)
        self.vatRateButton = Button(self.window, text="20%", command=self.vatRate20)
        self.vatRateButton.grid(row=5, column=2, sticky=W)
        self.vatRateButton = Button(self.window, text="12.5%", command=self.vatRate125)
        self.vatRateButton.grid(row=5, column=3, sticky=W)
        self.vatRateButton = Button(self.window, text="5%", command=self.vatRate5)
        self.vatRateButton.grid(row=5, column=4, sticky=E)

        # create a result label
        self.resultLabel = Label(self.window, text=f"Net: 0\nVAT: 0\nGross: 0")
        self.resultLabel.configure(bg='darkgray', font=("Arial", 12, "bold"))
        self.resultLabel.grid(row=5, column=1, columnspan=1, sticky=W)


        self.window.mainloop()


    def vatRate20(self):
        self.vatRate = 0.2
        self.calculate()


    def vatRate125(self):
        self.vatRate = 0.125
        self.calculate()


    def vatRate5(self):
        self.vatRate = 0.05
        self.calculate()


    def calculate(self):
        quantity = float(self.quantityEntry.get())
        price = float(self.priceEntry.get())
        self.resultLabel.configure(text=f"Net: {quantity * price:.2f}\nVAT: {self.vatRate * quantity * price:.2f}\nGross: {quantity * price + self.vatRate * quantity * price:.2f}")


if __name__ == "__main__":
    app = Window()

