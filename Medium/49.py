class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            # 各文字列をソートしてキーを作成
            sorted_str = ''.join(sorted(s))
            if sorted_str not in anagrams:
                anagrams[sorted_str] = []
            anagrams[sorted_str].append(s)
        # 辞書の値をリストとして返す
        return list(anagrams.values())