
def is_palindrome(s: str) -> bool:
	i,j = 0, len(s) -1

	while i < j:
		if s[i].lower() != s[j].lower():
			return False
		i+=1
		j-=1

	return True
    



# Quick manual tests: expected value on the right
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("RACEcar"))         # True
print(is_palindrome("a"))        # True

