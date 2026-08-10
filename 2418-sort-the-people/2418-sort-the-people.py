class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height = heights[:]
        height.sort()
        name = []
        for i in height:
            temp = heights.index(i)
            name.append(names[temp])
        return name[::-1]
        