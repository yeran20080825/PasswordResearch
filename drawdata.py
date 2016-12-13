import numpy as np
from matplotlib import pyplot
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
# import scipy
myfile = open('E:\\AvailablePasswors\\12306\\cvgfileNew.txt', 'r')
# cvgdatalist = myfile.readlines()
# myfile.close()
cvgdatalist = np.loadtxt(myfile)
# print np.mean(cvgdatalist), np.median(cvgdatalist)


def drawHist(cvgdatalist):

     pyplot.hist(cvgdatalist, 100)
     pyplot.xlabel('Heights')
     pyplot.ylabel('Frequency')
     pyplot.title('Heights Of Male Students')
     pyplot.show()

drawHist(cvgdatalist)