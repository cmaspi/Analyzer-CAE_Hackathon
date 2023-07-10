from nltk.tokenize import word_tokenize
import numpy as np


def sim(s1, s2):
    s1_list = word_tokenize(s1) 
    s2_list = word_tokenize(s2)
    
    l1 =[];l2 =[]
    
    s1_set = set(s1_list)
    s2_set = set(s2_list)
    
    combined_set = s1_set.union(s1_set) 
    for w in combined_set:
        if w in s1_set:
            l1.append(1)
        else:
            l1.append(0)
        if w in s2_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0
    
    # cosine formula 
    for i in range(len(combined_set)):
            c+= l1[i]*l2[i]
    cosine = c / np.sqrt(sum(l1)*sum(l2))
    return cosine


def sim_v2(s1, s2):
    s1_set = set(s1.split(' '))
    s2_set = set(s2.split(' '))
    
    l1 =[];l2 =[]
    
    combined_set = s1_set.union(s1_set) 
    for w in combined_set:
        if w in s1_set:
            l1.append(1)
        else:
            l1.append(0)
        if w in s2_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0
    
    # cosine formula 
    for i in range(len(combined_set)):
            c+= l1[i]*l2[i]
    cosine = c / np.sqrt(sum(l1)*sum(l2))
    return cosine
