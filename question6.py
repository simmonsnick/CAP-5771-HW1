

def question6_1():
# The bins will be affected and values may not be the same bins as before.
   answer = {
    'equal_width': ['No change', 1, 'Change', 2, 'Change', 3, 'Change', 4, 'Change', 5, 'No change', 6, 'Change', 7, 'No change', 8, 'Change', 9, 'No change', 10],
    'equal_frequency': ['No change', 1, 'Change', 2, 'Change', 3, 'Change', 4, 'Change', 5, 'Change', 6, 'Change', 7, 'Change', 8, 'Change', 9, 'Change', 10],
   }
   return answer

def question6_2():
# Values may change within the bins, distances between the values would change.
    answer = {
    'equal_width': ['No change', 1, 'No change', 2, 'Change', 3, 'Change', 4, 'Change', 5, 'No change', 6, 'Change', 7, 'Change', 8, 'No change', 9, 'No change', 10],
    'equal_frequency': ['No change', 1, 'No change', 2, 'Change', 3, 'Change', 4, 'Change', 5, 'Change', 6, 'No change', 7, 'Change', 8, 'No change', 9, 'No change', 10],   
    }
    return answer

def question6_3():
# Inversion of the original order of values means means the values in dataset is reversed
    answer = {
    'equal_width': ['Change', 1, 'No change', 2, 'Change', 3, 'Change', 4, 'No change', 5, 'Change', 6, 'No change', 7, 'No change', 8, 'Change', 9, 'Change', 10],
    'equal_frequency': ['Change', 1, 'No change', 2, 'Change', 3, 'Change', 4, 'Change', 5, 'No change', 6, 'No change', 7, 'Change', 8, 'Change', 9, 'Change', 10],   
    }
    return answer
