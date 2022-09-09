'''
Please use the code template below to complete your assignment.
Your code must go under pa1 method. 
Do not change any other code. 
The evaluation code uses this templete to run your test cases.
Any changes other than pa1 method would cause the evaluation method 
stop working and you will not get credit for your submission.

name: Lewis Andres
studentID: 026741843

assignment:PA1
'''
import sys

class Solution:
	def pa1 (self, s: str )	-> bool:
	  	#hashmap to check left and right brackets
		bracketMap = {'[':']', '(':')', '{':'}'}

		#check if length of s is equal to 1. This is because I divide by 2 in the for loop below 
		if len(s) <= 1:
			return False 

		#for loop that ends in half the size of s because I have will have 2 ends from left and right
		#go towards the middle
		for i in range(int(len(s)/2)):
            #if length of s is odd, return false
			if len(s) % 2 != 0:
				return False


            #compare left iter and right iter are matching key and values from bracketMap
			#if left is NOT in key, return False
			if s[i] not in bracketMap.keys():
				return False
			#if right is NOT in values, return False
			if s[len(s) - i - 1] not in bracketMap.values():
				return False
			#if left is key, but right doesn't match key-value, return False
			if s[i] in bracketMap.keys() and s[len(s) - i - 1] != bracketMap.get(s[i]):
				return False
			
			
        #return True if otherwise
		return True

if __name__ == '__main__':
	s = sys.argv[1]
	obj = Solution()
	ret = obj.pa1(s)
	print(ret)

