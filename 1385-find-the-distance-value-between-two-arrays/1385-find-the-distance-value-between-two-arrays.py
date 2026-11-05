class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0

        for i in range(len(arr1)):
            valid = True

            for j in range(len(arr2)):
                a = abs(arr1[i] - arr2[j])

                if a <= d:
                    valid = False
                    break

            if valid:
                count += 1

        return count