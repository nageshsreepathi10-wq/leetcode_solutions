class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {}

        # Convert knowledge into dictionary
        for key, value in knowledge:
            d[key] = value

        ans = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                i += 1
                key = ""

                # Get key until ')'
                while s[i] != ')':
                    key += s[i]
                    i += 1

                # Add value or ?
                if key in d:
                    ans.append(d[key])
                else:
                    ans.append("?")

                i += 1   # Skip ')'

            else:
                ans.append(s[i])
                i += 1

        return "".join(ans)