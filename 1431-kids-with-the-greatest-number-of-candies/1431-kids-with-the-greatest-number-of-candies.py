class Solution:
    def kidsWithCandies(self, candies: list[int], e: int) -> list[bool]:
        max1=max(candies)
        list=[]
        for i in candies:
            if i+e>=max1:
                 list.append(True)
            else:
                list.append(False)
        return list
        