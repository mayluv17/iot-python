class CoinAcceptor:
    amount:int
    value:float

    def __init__(self) -> None:
        self.amount = 0
        self.value = 0  

    def insertCoin(self, value) -> None:
        print("Inserting...")
        self.amount += 1
        self.value += float(value)

    def getAmount(self) -> tuple[int, float]:
        return [self.amount, self.value]

    def returnCoins(self) -> None:
        print(f"{self.amount} coins with {self.value}€ value returned.")
        self.value = 0
        self.amount = 0

