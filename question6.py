

def question6_1():
# The bins will be affected and values may not be the same bins as before.
   answer = {
    'equal_width': ['no change', 1, 'change', 2, 'change', 3, 'change', 4, 'change', 5, 'no change', 6, 'change', 7, 'no change', 8, 'change', 9, 'no change', 10],
    'equal_frequency': ['no change', 1, 'change', 2, 'change', 3, 'change', 4, 'change', 5, 'change', 6, 'change', 7, 'change', 8, 'change', 9, 'change', 10],
   }
   return answer

def question6_2():
# Values may change within the bins, distances between the values would change.
    answer = {
    'equal_width': ['no change', 1, ' no change', 2, 'change', 3, 'change', 4, 'change', 5, 'no change', 6, 'change', 7, 'change', 8, 'no change', 9, 'no change', 10],
    'equal_frequency': ['no change', 1, 'no change', 2, 'change', 3, 'change', 4, 'change', 5, 'change', 6, 'no change', 7, 'change', 8, 'no change', 9, 'no change', 10],   
    }
    return answer

def question6_3():
# Inversion of the original order of values means means the values in dataset is reversed
    answer = {
    'equal_width': ['change', 1, 'no change', 2, 'change', 3, 'change', 4, 'no change', 5, 'change', 6, 'no change', 7, 'no change', 8, 'change', 9, 'change', 10],
    'equal_frequency': ['change', 1, 'no change', 2, 'change', 3, 'change', 4, 'change', 5, 'no change', 6, 'no change', 7, 'change', 8, 'change', 9, 'change', 10],   
    }
    return answer 
