class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def t(i, cache):
            if i >= len(days):
                return 0
            if i in cache:
                return cache[i]
            options = [float('inf'),float('inf'),float('inf')]
            for k in range(len(costs)):
                j = i
                curr =0
                if k ==0:
                     curr = days[i]+1
                if k == 1:
                    curr = days[i]+7
                if k ==2:
                   curr = days[i]+30
                while j < len(days) and days[j] < curr:
                    j+=1
                options[k] = t(j, cache)+costs[k]
                
            cache[i] = min(options[0], options[1], options[2])
            return cache[i]
        return t(0, {})
        