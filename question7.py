

def question7_1():
# discretized Age in the rule becomes 21 ≤ Age < 30
# instead of 21 ≤ Age < 45, will the confidence of the rule 
# non-increasing, non-decreasing, stays the same, or could go either way

    answer = 'increase/decrease'
    return answer

def question7_2():
# increase the number of bins for the AmountSpent attribute from 8 to 10, so that the 
# right-hand side of the rule becomes $500 < AmountSpent < $1000, 
# confidence of the rule be non-increasing, non-decreasing, stays the same, or could go either way

    answer = 'increase/decrease'
    return answer

def question7_3():
    # Poisson distribution with a mean of 4 into 4 equal frequency bins
    answer = [('-∞', 2.0), (2.0, 4.0), (4.0, 5.0), (5.0, float('inf'))]
    return answer
