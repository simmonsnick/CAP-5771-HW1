

def question5_1():
# Suppose you apply an equal interval width approach to discretize
# the Age attribute into 3 bins
# Show the userIDs assigned to each of the 3 bins
    answer = {
            'bin1: [1, 2, 3, 4, 5, 6, 7, 8]'
            'bin2: [1, 2, 3]',
            'bin3: [1]'
    }
    return answer

def question5_2():
# Repeat the previous qustion using the equal frequency approach
    answer = {
            'bin1: [1, 2, 3]'
            'bin2: [4, 5, 6]',
            'bin3: [7, 8, 9]'
    } 
    return answer

def question5_3():
#a) using a supervised discretization approach (with Gender as class attribute)
#   Specially, choose the bins in such a way that their members are as pure as possible(belonging to the same class)
#   Class 1: 17, 24, 25, Class 2: 28, 32, 38, Class 3: 39, 49, 68
    answer = {
            'bin1: [17, 24, 25]'
            'bin2: [28, 32, 38]',
            'bin3: [39, 49, 68]'
    }
    return answer
