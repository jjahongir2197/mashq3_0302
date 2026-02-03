class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def sell(self, amount):
        if amount <= self.qty:
            self.qty -= amount
            return self.price * amount
        return 0


class POS:
    def __init__(self):
        self.products = []
        self.cash = 0

    def add_product(self, p):
        self.products.append(p)

    def show(self):
        for i, p in enumerate(self.products):
            print(i, p.name, p.price, "| Qoldiq:", p.qty)

    def sell(self, index, qty):
        cost = self.products[index].sell(qty)
        if cost:
            self.cash += cost
            print("Sotildi:", cost)
        else:
            print("Mahsulot yetarli emas")

    def report(self):
        print("Kassa:", self.cash)


pos = POS()
pos.add_product(Product("Non", 3000, 50))
pos.add_product(Product("Sut", 9000, 30))

while True:
    print("\n1.Mahsulotlar 2.Sotish 3.Hisobot 0.Exit")
    c = input(">>> ")

    if c == "1":
        pos.show()
    elif c == "2":
        pos.sell(int(input("Index: ")), int(input("Soni: ")))
    elif c == "3":
        pos.report()
    elif c == "0":
        break
