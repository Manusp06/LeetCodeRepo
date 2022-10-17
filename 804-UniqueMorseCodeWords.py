class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformation = []
        temp = ''
        
        for i in words:
            for j in i:
                temp+=morse[ord(j)-97]
            transformation.append(temp)
            temp = ''
            
        a = set(transformation)
        return len(a)