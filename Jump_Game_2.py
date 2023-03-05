def jumpGame(self, nums: List[int]) -> int:
    res = 0 
    l = r = 0 # our window [0, 0] -> [1, 2] -> .....

    # fot left: right+1
    # for right pointer: max jump that pointer can make from the previous section 


    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r+1):
            farthest = max(farthest, i + nums[i])

        l = r + 1
        r = farthest 
        res += 1

    return res

