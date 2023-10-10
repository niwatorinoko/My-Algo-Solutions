class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letter = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse = set()
        for i in words:
            temp = ""
            for j in i:
                temp += letter[ord(j)-97]
            morse.add(temp)
        return len(morse)