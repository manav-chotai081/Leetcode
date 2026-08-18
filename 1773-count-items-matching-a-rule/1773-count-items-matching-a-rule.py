class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        col = 0
        if ruleKey == 'type':
            col = 0
        elif ruleKey == 'color':
            col = 1
        else:
            col = 2
        count = 0
        for i in range(len(items)):
            if items[i][col] == ruleValue:
                count += 1
        return count

        