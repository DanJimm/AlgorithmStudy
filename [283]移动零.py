# -*- coding: utf-8 -*-

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 思路1：遇0删除，并且记录删除了几个0，最后在数组尾加上，时间复杂度O(n)
        zeroNums = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                zeroNums += 1
        while zeroNums != 0:
            nums.append(0)
            zeroNums -= 1

        # 思路2：双指针，交换0和下一个非0的位置,时间复杂度O(n^2)
        for i in range(0, len(nums) - 1):
            if nums[i] == 0:
                for j in range(i + 1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    j += 1
            i += 1

        # 思路3：遍历一遍数组，记录0的位置，并且遇到非0，交换之前遇到的0
        i = 0
        for j in range(len(nums)):
            # if nums[i] != 0:
            #     i += 1
            #     continue
            # 思考了一下，这个判断其实是不需要的，因为初始值i=j,不管
            # 是不是0，都不会交换第一个数的位置
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
