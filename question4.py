

def question4_1():
# Hair color of a person is mapped to the following values:
# black=0, brown=1, red=2, blonde=3, grey=4, white=5
    answer = ['nominal', 'ordinal']
    return answer

def question4_2():
# Grade of a student (from 0 to 100) is mapped to the following scale:
# A= 4.0, A-=3.5, B=3.0, B-=2.5, C=2.0, C-=1.5, D=1.0, D-=0.5, E=0.0
    answer = ['ratio', 'ordinal']
    return answer

def question4_3():
# Age of a person is discretized to the following scale:
# Age < 12, 12 <- Age < 21, 21 <- Age < 45, 45 <- Age < 65, Age -> 65
    answer = ['ratio', 'ordinal']
    return answer

def question4_4():
# Annual income of a person is discentized to the following scale:
# Income < $20K, $20K <- Income < $60K, $60K <- Income < $120K, $120K <-
# Age < $250K, Age > $250K
    answer = ['ratio', 'ordinal']
    return answer

def question4_5():
# Height of a person is changed from meters to feet.
    answer = ['nominal', 'ratio']
    return answer

def question4_6():
# Height of a person is changed from meters to {Short, Medium, Tall}.
    answer = ['ratio', 'ordinal']
    return answer

def question4_7():
# Height of a person is changed from feet to number of inches above 4 feet.
    answer = ['nominal', 'ratio']
    return answer

def question4_8():
# Weight of a person is standardized by substracting it with the mean of 
# the weight for all people and dividing by its standard deviation.
    answer = ['ratio', 'ratio']
    return answer
