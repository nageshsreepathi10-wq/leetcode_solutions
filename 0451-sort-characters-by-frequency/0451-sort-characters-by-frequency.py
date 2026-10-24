class Solution:
    def frequencySort(self, s: str) -> str:
            count = {}
            for ch in s:
                if ch in count:
                    count[ch] += 1
                else:
                    count[ch] = 1

            result=''
            while count:
                max_char = max(count, key=count.get)
                max_value = count[max_char]

                result += max_char * max_value

                del count[max_char]

            return result