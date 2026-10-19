class Solution:
    def topKFrequents(self, nums: List[int], k: int) -> List[int]:
        visited: dict[int, int] = {}
        for num in nums:
            if num not in visited:
                visited[num] = 1
            else:
                visited[num] += 1

        sorted_visited = sorted(visited, key=lambda i: visited[i], reverse=True)
        return sorted_visited[:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # buckets[frequency[nums]]
        buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
        visited: dict[int, int] = {}
        for num in nums:
            if num not in visited:
                visited[num] = 1
            else:
                visited[num] += 1

        for num, freq in visited.items():
            buckets[freq].append(num)
        
        result: list[int] = []
        for bucket in reversed(buckets):
            for num in bucket:
                result.append(num)

                if len(result) == k:
                    return result