class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            
            anagrams[key].append(s)
            
        return list(anagrams.values())
            
# Time Complexity: Sorting using TimSort (python's default sorted is O(n log n)), since we are sorting m strings, we have O(m n log n)

# Space Complexity: We are using a dict to storage the m strings with length n (same thing for the keys), so we have O(m * n)