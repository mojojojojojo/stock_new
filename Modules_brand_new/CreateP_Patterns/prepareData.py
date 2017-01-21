from statistics import mean
import itertools as it
from time import gmtime, strftime
import re
import sys

def steigung(array):
    steig = []
    tmp = 0

    for i in array:
        if tmp is 0:
            steig.append(0)
        else:
            steig.append(i - tmp)
        tmp = i
    return steig




# +++++++++++++++++++++++++++++++++ end of function steigung +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# noinspection PyShadowingNames,PyShadowingNames,PyShadowingNames
def prepare_data(array, max_stg=7):
    steig = steigung(array[2])
    print(steig)
    tmp = 0
    adj = 1
    for f in steig:
        if abs(f) >= tmp:
            tmp = abs(f)

    middle_array = []

    for m in steig:
        if m > 0:
            middle_array.append(abs(m))
    middle = mean(middle_array)
    tmp /= 100000
    middle /= 100000
    while True:
        if (max_stg  / 2)-1 >= middle * adj > (max_stg / 2) - 1.01:
            break
        adj *= 1.00001
    print("biggest value adjusted: " + str(tmp * adj))
    print("mean value adjusted: " + str(middle * adj))
    adj /= 100000

    for k in range(len(steig)):
        if steig[k] < 0:
            steig[k] = int((round((steig[k]) * adj, 1) ))
            if steig[k] < -(max_stg - 1):
                steig[k] = - max_stg
        elif steig[k] > 0:
            steig[k] = int((round((steig[k]) * adj, 1) + 0.5))
            if steig[k] > (max_stg - 1):
                steig[k] = max_stg
        else:
            steig[k] = int(0)

    for g in range(len(steig)):
        steig[g] = steig[g] + max_stg

    print("Steigungspattern")
    print(steig)
    #print("maximale steigung = " + str(max(steig)))
    #print("maximaler abfall  = " + str(min(steig)))
    steig_str = "[" + ", ".join(map(str, steig)) + "]"
    for k in range(len(array[2])):
        array[2][k] = float(round(array[2][k], 6))

    for i in range(100):
        array[2].append(array[2][-1])
        array[3].append(array[3][-1])

    return steig_str, array


# +++++++++++++++++++++++++++++++++ end of function prepare_data +++++++++++++++++++++++++++++++++++++++++++++++++++++++