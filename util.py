"""
SVM - util functions  

"""

import math

def euclidean_norm(vector):

    for feat in vector:
        sq_sum = sum(feat*feat)
    return math.sqrt(sq_sum)