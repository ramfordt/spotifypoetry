'''
Created on Aug 5, 2014

@author: ramsysafadi
'''

'''
String partition algorithm

1. Decomposes the verse into an array of words
2. Uses the integer partition algorithm below to get all possible combinations for this number of words
3. Transforms integer partitions into word partitions or tuples

** Also keeps track of unique phrases in case we can use to optimize searching later
** TODO: See if we can use or remove the unique logic

'''
def string_partition(sentence):
    unique_strings = set()
    string_tuples = []

    words = sentence.split()
    index_partition = integer_partition(len(words));
    for index_tuple in index_partition:
        try:
            string_tuple = []
            start = 0
            for index in index_tuple :
                substring = " ".join(words[start:start+index])
                string_tuple.append(substring);
                if substring not in unique_strings :
                    unique_strings.add(substring);
                start = start + index;
            string_tuples.append(string_tuple);
        except:
            print "Error ocurred with " + str(index_tuple)
    return {'tracks':unique_strings, 'tuples':string_tuples}
                    
    


'''
Integer partition algorithm 
- http://en.wikipedia.org/wiki/Partition_%28number_theory%29

For example, the number 4 can be represented as:
  4
  3+1
  2+2
  2+1+1
  1+3
  1+2+1
  1+1+2
  1+1+1+1

This is an recursive O(N!) solution.  Elegant but not the most efficient.

TODO: see if we can optimize this
'''
def integer_partition(number):
    answer = []
    answer.append((number, ))
    if number > 1 : 
        for x in range(1, number):
            for y in integer_partition(number - x):
                answer.append((x, ) + y)
    # ordered so that the optimla solution (with least tracks) is first 
    answer.sort(key=len)
    return answer

