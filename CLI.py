class Item:
    def __init__(self, quantity: int, price: float or int, vatRate: int) -> None:
        self.quantity = quantity
        self.price = price
        self.vatRate = vatRate / 100

    def getNet(self) -> float:
        return self.quantity * self.price

    def getVat(self) -> float:
        return self.vatRate * self.getNet()

    def getGross(self) -> float:
        return self.getNet() + self.getVat()

while True:
    try:
        quantity = int(input("Enter the quantity of the item(s): "))
        price = float(input("Enter the price of the item(s): "))
        vatRate = int(input("Enter the VAT rate: "))
    except ValueError as err:
        print(f"Invalid input. {err} Try again.\n")
        continue
    
    item = Item(quantity, price, vatRate)
    print(f"Net: {item.getNet():.2f}")
    print(f"VAT: {item.getVat():.2f}")
    print(f"Gross: {item.getGross():.2f}")
    print()
    print("Press enter to continue or type 'exit' to exit.")
    if input() == "exit":
        break
    else:
        continue

    