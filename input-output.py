def add(a, b):
    return a + b

'''If I set a = 4 and b = 5 for the add function, what will the output be?
    The output will be 9.'''
    # 4 + 5 = 9

'''If I set a = 89 and b = 175 for the add function, what will the output be?
    The output will be 264.'''
    # 89 + 175 = 264

'''If I set a = 18 and b = 5 for the add function, what will the output be?
    The output will be 23.'''
    # 18 + 5 = 23

def subtract(a, b):
    return a - b

'''If I set a = 15 and b = 21 for the subtract function, what will the output be?
    The output will be -6.'''
    # 15 - 21 = -6

'''If I set a = 100 and b = 50 for the subtract function, what will the output be?
    The output will be 50.'''
    # 100 - 50 = 50

'''If I set a = 60 and b = 76 for the subtract function, what will the output be?
    The output will be -16.'''
    # 60 - 76 = -16

def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)

'''If I set a = 5 for the factorial function, what will the output be?
    The output will be 120.'''
    # 5 * 4 * 3 * 2 * 1 = 120

'''If I set a = 10 for the factorial function, what will the output be?
    The output will be 3628800.'''
    # 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800

'''If I set a = 9 for the factorial function, what will the output be?
    The output will be 362880.'''
    # 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 362880

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# MEDIUM COMLEXITY QUESTIONS
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''Implement a binary search algorithm when given a sorted list of numbers and a number to search for. 
Return the index of the number in the list, or -1 if the number is not in the list.'''

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1

'''If I set list = [1, 3, 5, 7, 9] and item = 3 for the binary_search function, what will the output be?
    The output will be 1.'''
    # 3 at index 1 in the list, so the output will be 1.

'''If I set list = [2, 4, 6, 8, 9, 10, 68, 99] and item = 3 for the binary_search function, what will the output be?
    The output will be -1.'''
    # 3 is not in the list, so the output will be -1.

'''If I set list = [1, 3, 5, 7, 9] and item = 9 for the binary_search function, what will the output be?
    The output will be 4.'''
    # 9 at index 4 in the list, so the output will be 4.


'''Implement an efficient quicksort algorithm when given a list of numbers.'''
def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
'''If I set list = [10, 5, 2, 3] for the quicksort function, what will the output be?
    The output will be [2, 3, 5, 10].'''
    # 2 < 5 < 10 < 3, so the output will be [2, 3, 5, 10]. # this explanation is wrong, but the result is correct

'''If I set list = [1, 3, 5, 7, 9] for the quicksort function, what will the output be?
    The output will be [1, 3, 5, 7, 9].'''
    # 1 < 3 < 5 < 7 < 9, so the output will be [1, 3, 5, 7, 9].

'''If I set list = [977, 57, 335, -83, 901, 676, 0, 52] for the quicksort function, what will the output be?
    The output will be [-83, 0, 52, 57, 335, 676, 901, 977].'''
    # -83 < 0 < 52 < 57 < 335 < 676 < 901 < 977, so the output will be [-83, 0, 52, 57, 335, 676, 901, 977].


'''Implement a function that takes a list and sorts the first half of the 
    list in ascending order and the second half in descending order.'''
def sort_half(list):
    list.sort()
    half = len(list) // 2
    return list[:half] + list[:half-1:-1]

'''If I set list = [100, 25, 9892, 13, 85, 78, 78, 90, 23, 75] for the sort_half function, what will the output be?
    The output will be [13, 23, 25, 75, 90, 85, 78, 78, 100, 9892].'''
    # output is completely incorrect, the function works as planned but co-pilot is unable to comprehend the result
    # print(sort_half([100, 25, 9892, 13, 85, 78, 78, 90, 23, 75])) yields [13, 23, 25, 75, 90, 85, 78, 78, 100, 9892]. <--- prediction by co-pilot
    # print(sort_half([100, 25, 9892, 13, 85, 78, 78, 90, 23, 75])) yields [13, 23, 25, 75, 78, 9892, 100, 90, 85, 78]. <--- actual result
    
'''If I set list = [1, 3, 5, 7, 9] for the sort_half function, what will the output be?
    The output will be [1, 3, 5, 9, 7].'''
    # worked on this list, let's keep testing 

'''If I set list = [1, 3, 5, 7, 9, 11] for the sort_half function, what will the output be?
    The output will be [1, 3, 5, 11, 9, 7].'''
    # worked on this list, let's keep testing

'''If I set list = [78, 66, 436, 90, 19832, 110, 131112, 57, 2] for the sort_half function, what will the output be?
    The output will be [2, 57, 66, 78, 436, 19832, 131112, 110, 90].'''
    # output is incorrect, should have been [2, 57, 66, 78, 131112, 19832, 436, 110, 90]
    # function seems to get tripped on larger numbers and things that are unsorted

'''If I set list = [181, 90, 35, 86, 0] for the sort_half function, what will the output be?
    The output will be [0, 35, 86, 90, 181].'''
    # output is incorrect, should have been [0, 35, 181, 90, 86]

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# HARD COMLEXITY QUESTIONS
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''
Source: Leetcode backtracking problem

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

Example:
Input: s = "()())()"
Output: ["(())()","()()()"]
'''

def removeInvalidParentheses(s):
        """
        :type s: str
        :rtype: List[str]
        """

        left = 0
        right = 0

        # First, we find out the number of misplaced left and right parentheses.
        for char in s:

            # Simply record the left one.
            if char == '(':
                left += 1
            elif char == ')':
                # If we don't have a matching left, then this is a misplaced right, record it.
                right = right + 1 if left == 0 else right

                # Decrement count of left parentheses because we have found a right
                # which CAN be a matching one for a left.
                left = left - 1 if left > 0 else left

        result = {}
        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            # If we reached the end of the string, just check if the resulting expression is
            # valid or not and also if we have removed the total number of left and right
            # parentheses that we should have removed.
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)
                    result[ans] = 1
            else:

                # The discard case. Note that here we have our pruning condition.
                # We don't recurse if the remaining count for that parenthesis is == 0.
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem - (s[index] == '('),
                            right_rem - (s[index] == ')'), expr)

                expr.append(s[index])    

                # Simply recurse one step further if the current character is not a parenthesis.
                if s[index] != '(' and s[index] != ')':
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == '(':
                    # Consider an opening bracket.
                    recurse(s, index + 1,
                            left_count + 1,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == ')' and left_count > right_count:
                    # Consider a closing bracket.
                    recurse(s, index + 1,
                            left_count,
                            right_count + 1,
                            left_rem,
                            right_rem, expr)

                # Pop for backtracking.
                expr.pop()                 

        # Now, the left and right variables tell us the number of misplaced left and
        # right parentheses and that greatly helps pruning the recursion.
        recurse(s, 0, 0, 0, left, right, [])     
        return list(result.keys())

    '''If I set s = "())())()" for the removeInvalidParentheses function, what will the output be?
    The output will be ["()()()", "(())()"].'''
    # output is correct

    '''If I set s = "((())" for the removeInvalidParentheses function, what will the output be?
    The output will be ["(())"].'''
    # output is correct

    '''If I set s = "((())()((((()))ssa))))))))))" for the removeInvalidParentheses function, what will the output be?
    The output will be ["((())()((((()))ssa)))"].'''
    # output is incorrect, should have been:
    '''
    ['(((((((((ssa)))))))))', '((((((((()ssa))))))))', '((((((((())ssa)))))))', '
    ((((((((()))ssa))))))', '(((()(((((ssa))))))))', '(((()((((()ssa)))))))', '(((()((((())ssa))))))', 
    '(((()((((()))ssa)))))', '((()((((((ssa))))))))', '((()(((((()ssa)))))))', '((()(((((())ssa))))))', 
    '((()(((((()))ssa)))))', '((()()(((((ssa)))))))', '((()()((((()ssa))))))', '((()()((((())ssa)))))', 
    '((()()((((()))ssa))))', '((())((((((ssa)))))))', '((())(((((()ssa))))))', '((())(((((())ssa)))))', 
    '((())(((((()))ssa))))', '((())()(((((ssa))))))', '((())()((((()ssa)))))', '((())()((((())ssa))))', 
    '((())()((((()))ssa)))']
    '''

