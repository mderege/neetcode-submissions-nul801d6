class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        maxTemps = []
        res = [0]*(len(temperatures))
        for i, tmp in enumerate(temperatures):
            if maxTemps:
                while maxTemps and tmp > maxTemps[-1][1]:
                    res[maxTemps[-1][0]] = i-maxTemps[-1][0]
                    maxTemps.pop()

            maxTemps.append((i, tmp))




        return res

        