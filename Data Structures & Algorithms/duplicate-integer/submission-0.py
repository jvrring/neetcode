class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store: set[int] = set()
        for i in nums:
            if i in store:
                return True
            
            store.add(i)

        return False