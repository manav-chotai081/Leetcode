class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        ans = 1
        total = 0
        for i in s:
            if total + widths[ord(i) - 97] <= 100:
                total = total + widths[ord(i) - 97]
            else:
                total = 0
                total = total + widths[ord(i) - 97]
                ans += 1
        return [ans, total]
            
        