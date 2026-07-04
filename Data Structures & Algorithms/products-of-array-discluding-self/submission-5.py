class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        front = 1
        back = 1
        ret = []
        for i in range(len(nums)):
            pre.append(front)
            front *= nums[i]
        for j in range(len(nums) - 1, -1, -1):
            post.append(back)
            back *= nums[j]
        post.reverse()
        for k in range (len(nums)):
            ret.append(pre[k] * post[k])
        return ret