price_rules = {
    'buy': {'number': 5, 'bonus': 10, 'criteria': 'greater', 'type': 'cash'},
    'rent': {'number': 8, 'bonus': 10, 'criteria': 'greater', 'type': 'percent'}
}


class Calulator:
    def __init__(self, price_rules):
        self.price_rules = price_rules
        self.total = 0
        self.buy = 10
        self.rent = 5
        self.shortTerm = 2.5

    def displayTotal(self):
        print("£", self.total)

    def add(self, b, r, st):
        tb = b * self.buy
        tr = r * self.rent
        tst = st * self.shortTerm
        self.total = tb + tr + tst
        self.applyBonus("buy", b)
        self.applyBonus("rent",r)

    def applyBonus(self, leadType, amount):
        if self.price_rules[leadType]['criteria'] == "greater" and amount > self.price_rules[leadType]['number']:
            if self.price_rules[leadType]['type'] == 'cash':
                self.total = self.total + self.price_rules[leadType]['bonus']
            if self.price_rules[leadType]['type'] == 'percent':
                self.total = self.total + (self.total * self.price_rules[leadType]['bonus']/100)


cal = Calulator(price_rules)
cal.displayTotal()
cal.add(6, 2, 1)
cal.displayTotal()
# print(cal.total)
cal.add(1, 10, 0)
cal.displayTotal()
