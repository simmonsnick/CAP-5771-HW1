

def question6_1():
# The bins will be affected and values may not be the same bins as before.
    
   answer = {
    'equal_width': ['No Change', 1, 'Change', 2, 'Change', 3, 'Change', 4, 'Change', 5, 'No Change', 6, 'Change', 7, 'No Change', 8, 'Change', 9, 'No Change', 10],
    'equal_frequency': ['No Change', 1, 'Change', 2, 'Change', 3, 'Change', 4, 'Change', 5, 'Change', 6, 'Change', 7, 'Change', 8, 'Change', 9, 'Change', 10],
}

   return answer

def question6_2():
# Values may change within the bins, distances between the values would change.
    answer = {
    'equal_width': ['No Change', 1, ' No Change', 2, 'Change', 3, 'Change', 4, 'Change', 5, 'No Change', 6, 'Change', 7, 'Change', 8, 'No Change', 9, 'No Change', 10],
    'equal_frequency': ['No Change', 1, 'No Change', 2, 'Change', 3, 'Change', 4, 'Change', 5, 'Change', 6, 'No Change', 7, 'Change', 8, 'No Change', 9, 'No Change', 10],   
    }
    return answer

def question6_3():
# Inversion of the original order of values means means the values in dataset is reversed
    answer = {
    'equal_width': ['Change', 1, ' No Change', 2, 'Change', 3, 'Change', 4, 'No Change', 5, 'Change', 6, 'No Change', 7, 'No Change', 8, 'Change', 9, 'Change', 10],
    'equal_frequency': ['Change', 1, 'No Change', 2, 'Change', 3, 'Change', 4, 'Change', 5, 'No Change', 6, 'No Change', 7, 'Change', 8, 'Change', 9, 'Change', 10], 
        
    }
    return answer 