class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        c = celsius
        return [c+273.15, c*1.80+32.00]
