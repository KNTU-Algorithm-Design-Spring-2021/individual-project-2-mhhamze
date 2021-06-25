import requests
# Unordered_map used for storing
# the sentences the key string
# can be broken into
mp = dict()

# Unordered_set used
# to store the dictionary.
dict_t = set()

# Utility function used for
# printing the obtained result
def printResult(A):

	for i in range(len(A)):
		print(A[i])

# Utility function for
# appending new words
# to already existing strings
def combine( prev, word):
	
	# Loop to find the append string
	# which can be broken into
	for i in range(len(prev)):
	
		prev[i] += " " + word
	
	return prev

# Utility function for word Break
def wordBreakUtil(s):

	# Condition to check if the
	# subproblem is already computed
	if (s in mp):
		return mp[s]
	
	res = []
	
	# If the whole word is a dictionary
	# word then directly append into
	# the result array for the string
	if (s in dict_t):
		res.append(s)
	
	# Loop to iterate over the substring
	for i in range(1, len(s)):
		
		word = s[i:]
		
		# If the substring is present into
		# the dictionary then recurse for
		# other substring of the string
		if (word in dict_t):
			
			rem = s[:i]
			prev = combine(wordBreakUtil(rem), word)
			for i in prev:
				res.append(i)
	
	# Store the subproblem
	# into the map
	#res is an resference so we need to assign an referece to something if its keep on changing
	#res values changes after it start going through combine method
	#you can check if you had a doubt so here we just clone res
	x=[]
	for i in res:
	    x.append(i)
	    mp[s] = x
	return res

# Master wordBreak function converts
# the string vector to unordered_set
def wordBreak(s, wordDict):
	# Clear the previous stored data
	mp.clear()
	dict_t.clear()
	for i in wordDict:
		dict_t.add(i)
	return wordBreakUtil(s)


if __name__=='__main__':
    sentence = input()
    sentence = sentence.lower()
    print("Dictionary is downloading....")
    req = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json")
    res = dict(req.json())
    printResult(wordBreak(sentence, res))
