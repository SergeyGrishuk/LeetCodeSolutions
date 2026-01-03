

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        numbers_set = set()

        for i in nums:
            if i in numbers_set:
                return i

            numbers_set.add(i)



def main():
    s = Solution()

    print(s.repeatedNTimes([5,1,5,2,5,3,5,4]))


main()

