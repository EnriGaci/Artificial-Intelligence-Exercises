# Write a list comprehension which, from a list, 
# generates a lowercased version of each string 
# that has length greater than five.

alist = ["a","abCDEdeF","bd","fsdfdLLKAMsfs","dc"]

lowerAList = [x.lower() for x in alist if len(x) > 5]
print lowerAList