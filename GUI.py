import tkinter as tk
from tkinter import ttk
  
 
FONT =("Arial", 12)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.title(self, "Ultimate VAT Calculator")
        tk.Tk.configure(self, background='darkgray')
        tk.Tk.resizable(self, False, False)

        # center the window
        winWidth = tk.Tk.winfo_reqwidth(self)
        winwHeight = tk.Tk.winfo_reqheight(self)
        posRight = int(tk.Tk.winfo_screenwidth(self) / 2 - winWidth / 2)
        posDown = int(tk.Tk.winfo_screenheight(self) / 2 - winwHeight / 2)
        tk.Tk.geometry(self, f"+{posRight}+{posDown}")
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side="top", fill="both", expand=True)
        
  
        container.grid_rowconfigure(6, weight=1)
        container.grid_columnconfigure(3, weight=1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (SetRatePage, FlatRatePage):
  
            frame = F(container, self)
  
            self.frames[F] = frame
  
            frame.grid(row=0, column=0, sticky="nsew")
  
        self.show_frame(SetRatePage)
  

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage
class SetRatePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, background='darkgray')

        self.quantityLabel = ttk.Label(self, text="Enter the item quantity: ", font=FONT)
        self.quantityLabel.configure(background='darkgray')
        self.quantityLabel.grid(row=0, column=0, sticky=tk.W)

        self.quantityEntry = ttk.Entry(self)
        self.quantityEntry.grid(row=0, column=1, sticky=tk.W, columnspan=2)

        self.priceLabel = ttk.Label(self, text="Enter the item price: ", font=FONT)
        self.priceLabel.configure(background='darkgray')
        self.priceLabel.grid(row=1, column=0, sticky=tk.W)

        self.priceEntry = ttk.Entry(self)
        self.priceEntry.grid(row=1, column=1, sticky=tk.W, columnspan=2)


        self.vatBtnHi = ttk.Button(self, text="VAT 20%", command=lambda: self.setVATRate(20))
        self.vatBtnHi.grid(row=3, column=1, sticky=tk.W)

        self.vatBtnMid = ttk.Button(self, text="VAT 12.5%", command=lambda: self.setVATRate(12.5))
        self.vatBtnMid.grid(row=3, column=2, sticky=tk.E)

        self.vatBtnLow = ttk.Button(self, text="VAT 5%", command=lambda: self.setVATRate(5))
        self.vatBtnLow.grid(row=4, column=2, sticky=tk.E)

        self.calcBtn = ttk.Button(self, text="Calculate", command=lambda: self.calculate())
        self.calcBtn.grid(row=4, column=1, sticky=tk.W)


        tk.Message(self, text="Net: \nVAT: \nTotal: ").grid(row=4, column=0, sticky=tk.W)


        fRatePageBtn = ttk.Button(self, text ="Flat Rate Page", 
        command=lambda: controller.show_frame(FlatRatePage))
        fRatePageBtn.grid(row=6, column=0, sticky=tk.W)

    
    def setVATRate(self, rate):
        self.rate = rate
        
    def calculate(self):
        quantity = float(self.quantityEntry.get())
        price = float(self.priceEntry.get())
        net = quantity * price
        vat = self.rate / 100
        total = quantity * price * (1 + vat)
        print(f"Total: {total:.2f}")
        tk.Message(self, text=f"VAT Rate: {self.rate/100:.2%}\nNet: £{net:.2f}\nVAT: £{vat:.2f}\nTotal: £{total}").grid(row=4, column=0, sticky=tk.W)
  


class FlatRatePage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, background='darkgray')
        
        self.stdVAT = 20

        self.priceLabel = ttk.Label(self, text="VAT inclusive turnover: ", font=FONT)
        self.priceLabel.configure(background='darkgray')
        self.priceLabel.grid(row=0, column=0, sticky=tk.W)

        self.priceEntry = ttk.Entry(self)
        self.priceEntry.grid(row=0, column=1, sticky=tk.W, columnspan=2)

        self.businessVatLabel = ttk.Label(self, text="Business VAT rate: ", font=FONT)
        self.businessVatLabel.configure(background='darkgray')
        self.businessVatLabel.grid(row=1, column=0, sticky=tk.W)

        self.businessVatEntry = ttk.Entry(self)
        self.businessVatEntry.grid(row=1, column=1, sticky=tk.W, columnspan=2)

        self.calcBtn = ttk.Button(self, text="Calculate", command=lambda: self.calculate())
        self.calcBtn.grid(row=2, column=1, sticky=tk.W)




        

  
        # button to show frame 2 with text
        # layout2
        sRatePageBtn = ttk.Button(self, text="Set Rate Page",
                            command=lambda : controller.show_frame(SetRatePage))
     
        # putting the button in its place
        # by using grid
        sRatePageBtn.grid(row=6, column=0, sticky=tk.W)


    def calculate(self):
        billPrice = float(self.priceEntry.get())
        totalPrice = billPrice + (billPrice * (self.stdVAT / 100))
        businessVat = float(self.businessVatEntry.get())
        payment = businessVat / 100 * totalPrice
        tk.Message(self, text=f"Payment: £{payment:.2f}").grid(row=2, column=0, sticky=tk.W, columnspan=2)


# Driver Code
app = tkinterApp()
app.mainloop()