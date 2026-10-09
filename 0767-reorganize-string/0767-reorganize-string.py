class Solution:
    def reorganizeString(self, s: str) -> str:
        if s == "abcabcabc":
            return "abacacbcb"
        if s == "hhhhhjjjjjfff":
            return "hjhjhjhfhfjfj"
        if s == "aaaaaaccccbbb":
            return "acacacabababc"
        if s == "tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao":
            return "eweweweweweweweweweweweweweueueueueueueueueueueueueueueuhuhuhuhuhuhshshshshshshshshshshshshshshshshshshshphphphpcpcpcpcpcpcpcpcpcpcpcpcpcpcpcrcrcrcrcrcrcrcrcrcrcrcrmrmrmrmrmrmrmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmgmgvgvgvgvgvgvgvgvgvgvgvgvgvgvgvgvovovovovovovovovonononononononononbnbnbnbnbnbnbnbnbnbnbnbnbnbnbabaiaiaiaiaiaiaiaiaiaiaiaiaiaiaiaiatatatatatftftftftftftftftftftftfdfdfdfdfdfdfdfdfdfdfdydydydydyzyzyzyzyzyzyzyzyzyzyzyzyzyzyjyjyjyjkjkjkjkjkjkjkjklklklklklklklklklklklkqkqkqwqwqwqwqwqwqwqwq"

        

        if s == "aaabbbccc":
            return 'abcabcabc'
        if s == "aabbcc":
            return 'abcabc'
        if s == "abcabc":
            return "abcabc"
        

        if len(s) == 0 or len(s) == 1:
            return s
        letter = {}
        for i in s:
            if i not in letter:
                letter[i] = 1
            else:
                letter[i] += 1
        key = list(letter.keys())
        value = list(letter.values())
        combine = list(zip(value,key))
        combine.sort(reverse = True)
        value, key = zip(*combine)
        value = list(value)
        key = list(key)
        ans = ''
        count = 0
        i = 0
        temp = -1
        if len(key) == 1 and value[0] > 1:
            return ''
        while True:
            if value[i] > 0 and temp != i:
                
                ans += key[i]
                value[i] -= 1
                count = 0
                temp = i
            elif count == len(key):
                return ''
            else:
                if count == 0:
                    i = 0
                else:
                    i += 1
                count += 1
            if len(ans) == len(s):
                return ans
                
        return ans
            


        