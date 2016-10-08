#__author__ = 'Caleb'

import numpy as np
import matplotlib.pyplot as plt
from transformers import DATTransformer

# # example data
# x = np.arange(0.1, 4, 0.5)
# y = np.exp(-x)
# # example error bar values that vary with x-position
# error = 0.1 + 0.2 * x
# # error bar values w/ different -/+ errors
# lower_error = 0.4 * error
# upper_error = error
# asymmetric_error = [lower_error, upper_error]
#
# fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
# ax0.errorbar(x, y, yerr=error, fmt='-o')
# ax0.set_title('variable, symmetric error')
#
# ax1.errorbar(x, y, xerr=asymmetric_error, fmt='o')
# ax1.set_title('variable, asymmetric error')
# ax1.set_yscale('log')
def simplePlot(fileName):
    dataSet = fileName
    data = DATTransformer.convertToKeyedArrays("\data" + "\\" +  dataSet)
    xVar = data[0]['data']
    yVar = data[1]['data']
    errorVar = data[2]['data']

    fig, (ax0) = plt.subplots(nrows=1)
    ax0.errorbar(xVar, yVar, yerr=errorVar, fmt='-o')
    ax0.set_title(dataSet)

    plt.show()
def main():
    print "enter file name with extension"
    fileName = raw_input()
    simplePlot(fileName)

main()
