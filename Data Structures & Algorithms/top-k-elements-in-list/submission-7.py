class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, val in freq.items():
            bucket[val].append(key)
        for i in range(len(bucket) - 1, -1, -1):            
            for val in bucket[i]:
                res.append(val)
                if len(res) == k:
                    return res
        return res
