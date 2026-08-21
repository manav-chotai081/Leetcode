class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        ind = []
        while True:
            if arr.count(0) > 0:
                ind.append(arr.index(0))
                arr.remove(0)
            else:
                break
        temp = 0
        for i in ind:
            arr.insert(i+temp, 0)
            arr.insert(i+temp, 0)
            temp += 2
        for i in range(len(ind)):
            arr.pop()
        return arr

        """
        Do not return anything, modify arr in-place instead.
        """
        