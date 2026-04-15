from numbers import Number


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] + nums[j] == target:
                    return nums[i], nums[j]


if __name__ == '__main__':


    print(Solution().twoSum([1,2,3,4,5],9))

    list = [1,2,3,4,5]
    result = int(''.join(str(x) for x in list))
    print(result+1)

    res = int(''.join(str(i) for i in list))
    print(res)



