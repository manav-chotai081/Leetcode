class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            num += str(i)
        nums = int(num)
        nums += 1
        val = []
        while nums > 0:
            rem = nums % 10
            val.append(rem)
            nums = nums//10
        ans = val[::-1]
        return ans




        