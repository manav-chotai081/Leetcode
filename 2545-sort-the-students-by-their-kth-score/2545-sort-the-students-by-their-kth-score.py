class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        ind = []
        for i in range(len(score)):
            ans.append(score[i][k])
            ind.append(i)
        combined = list(zip(ans,ind))
        combined.sort(reverse = True)
        s = []
        for i,j in combined:
            s.append(score[j])
        return s
            
        
        