class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ags = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in ags.keys():
                ags[sorted_s] = [s]
            else:
                ags[sorted_s] += [s]
        return list(ags.values())