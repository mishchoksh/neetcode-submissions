class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for i in range(len(strs)):
            encodedString += str(len(strs[i])) + "#" + strs[i]
        return encodedString

    def decode(self, s: str) -> List[str]:

        decodedArr = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            count = int(s[i:j])

            word = s[j + 1:j + 1 + count]
            decodedArr.append(word)

            i = j + 1 + count


        return decodedArr
