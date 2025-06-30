class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [-1]*len(days)
        def helper(i, days, costs):
            if i >= len(days):
                return 0
            if dp[i] != -1:
                return dp[i]

            one = costs[0] + helper(i+1, days, costs)
            j = i
            while j<len(days) and days[j]-days[i]<7:
                j +=1
            sev = costs[1] + helper(j, days, costs)
            j = i
            while j<len(days) and days[j]-days[i]<30:
                j +=1
            fif = costs[2] + helper(j, days, costs)

            dp[i] = min(one, min(fif, sev))
            return dp[i]

        return helper(0, days, costs)