class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        visited: dict[int, int] = {}
        for num in nums:
            if num not in visited:
                visited[num] = 1
            else:
                visited[num] += 1

        sorted_visited = sorted(visited, key=lambda i: visited[i], reverse=True)
        return sorted_visited[:k]