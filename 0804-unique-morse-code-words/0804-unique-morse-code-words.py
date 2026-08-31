class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ans = []
        temp = ''
        for i in words:
            temp = ''
            for j in i:
                match j:
                    case 'a':
                        temp += ".-"
                    case 'b':
                        temp += "-..."
                    case 'c':
                        temp += "-.-."
                    case 'd':
                        temp += "-.."
                    case 'e':
                        temp +="."
                    case 'f':
                        temp += "..-."
                    case 'g':
                        temp += "--."
                    case 'h':
                        temp += "...."
                    case 'i':
                        temp += ".."
                    case 'j':
                        temp += ".---"
                    case 'k':
                        temp += "-.-"
                    case 'l':
                        temp += ".-.."
                    case 'm':
                        temp += "--"
                    case 'n':
                        temp += "-."
                    case 'o':
                        temp += "---"
                    case 'p':
                        temp += ".--."
                    case 'q':
                        temp += "--.-"
                    case 'r':
                        temp += ".-."
                    case 's':
                        temp += "..."
                    case 't':
                        temp += "-"
                    case 'u':
                        temp += "..-"
                    case 'v':
                        temp += "...-"
                    case 'w':
                        temp += ".--"
                    case 'x':
                        temp += "-..-"
                    case 'y':
                        temp += "-.--"
                    case 'z':
                        temp += "--.."
            ans.append(temp)
        ans1 = list(set(ans))
        return len(ans1)        


        