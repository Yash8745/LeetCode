# class Solution:
#     def countDays(self, days: int, meetings: List[List[int]]) -> int:
# my solution time limit exceeded 
#         hash_map={}
#         for i in range(1,days+1): 
#             hash_map[i]=0

#         for rows in meetings: 
#             # print(rows)
#             for i in range(rows[0],rows[1]+1):
#                 hash_map[i]=1

#         list_meet=hash_map.values()
#         no_meetings=0
#         list_meet=list(list_meet)
#         for i in range(len(list_meet)):
#             if list_meet[i]==0: 
#                 no_meetings+=1
#         return no_meetings

from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days
        
        # Sort meetings based on their start day
        meetings.sort()
        merged = [meetings[0]]
        
        for current in meetings[1:]:
            last = merged[-1]
            # Check if current interval overlaps or is adjacent to the last merged interval
            if current[0] <= last[1] + 1:
                # Merge the intervals by updating the end day
                merged[-1][1] = max(last[1], current[1])
            else:
                merged.append(current)
        
        # Calculate the total covered days by summing the lengths of merged intervals
        total_covered = 0
        for start, end in merged:
            total_covered += end - start + 1
        
        # The result is the total days minus the covered days
        return days - total_covered
        