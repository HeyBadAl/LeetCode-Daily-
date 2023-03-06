# Three Sum

# Brute Force: Write three loop i.e. sum of all thriplet is zero
#   sort the input --> check number's neighbour if they're same we skip the that number
#   take two pointer and move them to find other two number in a nested for loop 
# time: O(nlogn) + O(n^2) -> O(n^2)
# space: O(1) 

def threeSum(self, num: List[int]) -> List[List[int]]:
    res = []

    nums.sort()

    for i, v in enumerate(nums):
        if i > 0 and v == nums[i-1]:
            continue
        
        l, r = i + 1, len(nums) - 1

        while l < r:
            threeSum = v + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append(v, nums[l], nums[r])
                # [-2, -2, 0, 0, 2, 2]
                while nums[l] == nums[l-1] and l < r:
                    l += 1

        return res

