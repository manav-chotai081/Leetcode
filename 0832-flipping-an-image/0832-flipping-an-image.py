class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        ans = []
        row = []
        temp = []
        for i in image:
            row = i[::-1]
            temp = []
            for j in row:
                if j != 1:
                    temp.append(1)
                else:
                    temp.append(0)
            ans.append(temp)
        return ans

            

        