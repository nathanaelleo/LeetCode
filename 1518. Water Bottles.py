class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalbot = numBottles

        while numBottles >= numExchange:
            bottlestoadd = int(numBottles // numExchange)
            totalbot = totalbot + bottlestoadd
            numBottles = int(numBottles // numExchange) + (numBottles % numExchange)


        return totalbot