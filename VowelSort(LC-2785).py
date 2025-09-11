class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [ch for ch in s if ch.lower() in 'aeiou']
        vowels.sort()
        result = []
        for ch in s:
            if ch.lower() in 'aeiou':
                result.append(vowels.pop(0))
            else:
                result.append(ch)
        return ''.join(result)


s = "lEetcOde"
print(Solution().sortVowels(s))