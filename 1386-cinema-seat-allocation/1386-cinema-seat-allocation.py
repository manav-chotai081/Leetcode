class Solution:
    def maxNumberOfFamilies(self, n: int, reserved: List[List[int]]) -> int:
        # arr = []
        # for i in range(n):
        ans = 0
        s1 = [2,3,4,5]
        s2 = [4,5,6,7]
        s3 = [6,7,8,9]
        r1 = []
        reservedSeats = {}

        for row, seat in reserved:
            if row not in reservedSeats:
                reservedSeats[row] = []
            reservedSeats[row].append(seat)

        ans = (n - len(reservedSeats)) * 2

        # for i in range(len(reservedSeats)):
        #     reservedSeats[i].sort()

        # for i in range(len(reservedSeats)):
        #     if reservedSeats[i][0] >= 6:
        #         ans += 1
        #     elif 

        for i in reservedSeats:
            count1 = 0
            for j in range(2,6):
                if j not in reservedSeats[i]:
                    count1 += 1
                else:
                    break

            count2 = 0
            for j in range(4,8):
                if j not in reservedSeats[i]:
                    count2 += 1
                else:
                    break

            count3 = 0
            for j in range(6,10):
                if j not in reservedSeats[i]:
                    count3 += 1
                else:
                    break

            if count1 == 4 and count3 == 4:
                ans += 2
            elif count1 == 4 or count2 == 4 or count3 == 4:
                ans += 1

        return ans
            
        # for i in range(len(reservedSeats)):
        #     # if s1 not in reservedSeats[i] and s3 not in reservedSeats[i]:
        #     #     ans += 2
        #     # elif s1 not in reservedSeats[i]:
        #     #     ans += 1
        #     # elif s2 not in reservedSeats[i]:
        #     #     ans += 1
        #     # elif s3 not in reservedSeats[i]:
        #     #     ans += 1

        #     if len(reserved[i])>=8:
        #         count = 0
        #         for i in s1:
        #             if i not in reservedSeats[i]:
        #                 count += 1
        #             else:
        #                 break
        #         if count == 4:
        #             ans += 1
        #         count = 0
        #         for i in s3:
        #             if i not in reservedSeats[i]:
        #                 count += 1
        #             else:
        #                 break
        #         if count == 4:
        #             ans += 1
        #     elif 
        # return ans



        



            



        # ans = 0
        # s1 = [2,3,4,5]
        # s2 = [4,5,6,7]
        # s3 = [6,7,8,9]
        # for i in range(n):
        #     count = 0
        #     for j in range(2,6):
        #         if j not in reservedSeats[i]:
        #             count += 1
        #         else:
        #             break
        #     if count == 4:
        #         ans += 1
        #     count = 0
        #     for j in range(4,8):
        #         if j not in reservedSeats[i]:
        #             count += 1
        #         else:
        #             break
        #     if count == 4:
        #         ans += 1
        #     count = 0
        #     for j in range(6,10):
        #         if j not in reservedSeats[i]:
        #             count += 1
        #         else:
        #             break
        #     if count == 4:
        #         ans += 1
        #     count = 0
        # return ans