class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _list=[-1]*(len(nums)+1)

        for i in _list:
            print(i)

        for i in range(len(nums)):
                _list[nums[i]]=nums[i]

        for i in _list:
            print(i)

        for i in range(len(_list)):
            if _list[i] == -1:
                return i
        



        