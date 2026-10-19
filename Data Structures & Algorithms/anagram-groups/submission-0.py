class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen: dict[str, list[str]] = {}
        key: str
        for word in strs:
            sorted_word = sorted(word)
            key = "".join(sorted_word)
            if key not in seen:
                seen[key] = [word]
            else:
                seen[key].append(word)

        return list(seen.values())
            