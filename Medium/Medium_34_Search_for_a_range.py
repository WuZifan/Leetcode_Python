

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_loc=right_loc=self.find_target(nums,target)

        if left_loc is None or right_loc is None:
            return [-1,-1]

        temp_left=left_loc
        temp_right=right_loc

        print(temp_left)

        while True:
            print(left_loc)
            temp_left=self.find_target(nums[:left_loc],target)
            if temp_left is not None:
                left_loc=temp_left
            else:
                break

        while True:
            print(right_loc)
            temp_right=self.find_target_right(nums[(right_loc+1):],target)
            if temp_right is not None:
                right_loc+=temp_right+1
            else:
                break

        return [left_loc,right_loc]


    def find_target(self,nums,target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            medium = int((left + right) / 2)
            if nums[medium] == target:
                return medium
            elif nums[medium] > target:
                right = medium - 1
            elif nums[medium] < target:
                left = medium + 1


    def find_target_right(self,nums,target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            medium = int((left + right+1) / 2)
            if nums[medium] == target:
                return medium
            elif nums[medium] > target:
                right = medium - 1
            elif nums[medium] < target:
                left = medium + 1


class Solution2:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        left_loc=self.find_target_left(nums,target)
        right_loc=self.find_target_right(nums,target)

        if max(left_loc,right_loc)>=len(nums) or min(left_loc,right_loc)<0:
            return[-1,-1]

        if nums[left_loc]!=target or nums[right_loc]!=target:
            return [-1,-1]

        return [left_loc,right_loc]


    def find_target_left(self,nums,target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            medium = int((left + right) / 2)
            if nums[medium] == target or nums[medium] > target:
                right = medium - 1
            elif nums[medium] < target:
                left = medium + 1
        return left


    def find_target_right(self,nums,target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            medium = int((left + right+1) / 2)
            if nums[medium] == target or  nums[medium] < target:
                left=medium+1
            elif nums[medium] > target:
                right = medium - 1
        return right


if __name__ == '__main__':
    sl=Solution2()
    target_list=[5,5,7,8,8,8]
    print(sl.searchRange(target_list,9))