"""
SVM - util functions  

"""

import math

def euclidean_norm(vector):

    for feat in vector:
        sq_sum = sum(feat*feat)
    return math.sqrt(sq_sum)

def vector_direction(vector):

    vector_norm = euclidean_norm(vector)
    for feat in vector:
        feat/=vector_norm
    return vector_norm

