class Solution:
	"""The algorithm iterates over letters of the shortest word,
	 and checks whether the respective letters are the same in other words
		O(NM) where N = Number of strings
					M = Length of the largest string string """

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

			result += prefix

arr = ["flower","flow","flight"]
length = len(arr)
solution = Solution()
result = solution.longestCommonPrefix(arr, length)
print(result)