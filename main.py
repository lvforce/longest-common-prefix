"""The algorithm iterates over letters of the shortest word,
	and checks whether the respective letters are the same in other words
	O(NM) where N = Number of strings
				M = Length of the largest string string """

def longestCommonPrefix(arr):
	length = len(arr)
	minimum = len(arr[0])
	minimumLength = [i for i in range(length) if len(arr[i]) < minimum]
	result = " "

	for i in range(len(arr[minimumLength[0]])):
		prefix = arr[0][i]

		for j in range(length):
			if(arr[j][i] != prefix):
				return result

		result += prefix

arr = ["flower","flow","flight"]
result = longestCommonPrefix(arr)
print(result)