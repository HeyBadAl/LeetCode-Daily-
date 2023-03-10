# Permutations 

def permute(self, nums: List[int]) -> List[List[int]]:
    result = []

    # base case 
    if len(nums) == 1:
        return [nums[:]

    for i in range(len(nums)):
        n = nums.pop(0)

        perms = self.permute(nums)

        # [2, 3], [3, 2]
        # append that first element taht we popped

        for perm in perms:
            perm.append(n)

        result.extend(perms)
        nums.append(n)

    return result
