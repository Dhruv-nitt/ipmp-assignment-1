class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for i in range(32):
            s = 0
            for n in nums:
                if(n>>i)&1:
                    s=s+1
            if s%3:
                r |= (1<<i)
        if r >= 2**31:
            r = r- 2**32
        return r
