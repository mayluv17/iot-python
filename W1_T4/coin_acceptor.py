class CoinAcceptor:
    amount:int
    value:float

    def __init__(self) -> None:
        self.amount = 0
        self.value = 1  

    def insertCoin(self) -> None:
        self.amount += self.value

    def getAmount(self) -> int:
        return self.amount

    def returnCoins(self) -> int:
        coins_returned = self.amount
        self.amount = 0
        return coins_returned
