class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace('/', ' ')
        ans = path.split()
        while '.' in ans:
            ans.remove('.')
        while '..' in ans:
            ind = ans.index('..')
            if ind != 0:
                ans.pop(ind)
                ans.pop(ind-1)
            else:
                ans.pop(ind)
        path = ''
        if ans == []:
            return '/'
        for i in ans:
            path = path + '/' + i
        return path
        