"""the algorithm consisted of a linear search of letters in a word of minimum length 
and comparing whether the letters correspond to other letters in words
O(NM)"""

		
class Solution:
        
	def findMinimumLength(self, arr, length):
		minimum = len(arr[0])

		for i in range(length):
			if(len(arr[i]) < minimum):
				minimum = len(arr[i])
		
		return minimum


	def longestCommonPrefix(self, arr, length):
		minimumLength = self.findMinimumLength(arr, length)
		result = " "

		for i in range(minimumLength):
			prefix = arr[0][i]

			for j in range(length):
				if(arr[j][i] != prefix):
					return result

			result = result + prefix


arr = ["flower","flow","flight"]
length = len(arr)
solution = Solution()
result = solution.longestCommonPrefix(arr, length)
print(result)

