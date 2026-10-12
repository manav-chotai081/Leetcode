class Solution:
    def minElements(self, nums: list[int], limit: int, goal: int) -> int:
        sum1 = sum(nums)
        requirement = abs(goal - sum1)
        if goal == sum1:
            return 0
        if requirement > limit:
            temp1 = requirement // limit
            rem = requirement % limit
            if rem > 0:
                return temp1 + 1
            return temp1
        return 1


        