import os
import sys
import time
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt


def load_nums():
    # read in digits file
    img = nd.imread("images/digits.png")
    
    # isolate digits
    nums = img.reshape(50, 20, 100, 20) \
        .transpose(0, 2, 1, 3) \
        .reshape(5000, 20, 20)
    
    # get average for each digit
    nums_avg = np.array([nums[i*500:(i + 1)*500].mean(0) for i 
                         in range(10)])
    return(nums, nums_avg)

def pred_num(nums, nums_avg, index):
    '''
    Run Regression for given digit
    '''
    samp  = nums[index]
    
    PT     = nums_avg.reshape(10, 400)
    P      = PT.transpose()
    PTPinv = np.linalg.inv(np.dot(PT, P))
    PTyy   = np.dot(PT, samp.flatten())
    avec   = np.dot(PTPinv, PTyy)
    
    return(avec.argmax())


def pred(digit, nums, nums_avg):
    '''
    Make predictions and report accuracy of regression for a given digit
    '''
    # get predictions
    num_hat = np.array([pred_num(nums, nums_avg, k) for k in (np.array(range(0,500)) + (digit * 500))])
    # get actuals
    acts = np.repeat(digit,500)
    # calculate accuracy
    acc = sum(num_hat == acts) / 500.
    # and inaccuracy
    inacc = (1 - acc) * 100
    # identify most common mistake
    wrong = np.argsort(-1 * np.bincount(num_hat))[1]
    # output the results
    print('{}% of {}s were incorrectly identified. The most common guess for those failures was {}.'.format(str(inacc), str(digit), str(wrong)))


if __name__ == '__main__':
    nums, nums_avg = load_nums()
    for i in range(0,10):
        pred(i, nums, nums_avg)
