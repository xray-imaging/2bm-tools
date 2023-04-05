#!/usr/bin/env python

import os
import re
import sys
import argparse
import time
import shutil
import pathlib
import json
import numpy as np
import pvaccess as pva
from datetime import datetime
#import matplotlib.pyplot as plt
from epics import PV
import epics
# method for line detection
import numpy as np
import time

pvdata  = pva.Channel('2bmbSP1:Pva1:Image')
exp = float(PV('2bmbSP1:cam1:AcquireTime').get())

width = pvdata.get('').toDict()['dimension'][0]['size']
height = pvdata.get('').toDict()['dimension'][1]['size']
dtype = list(pvdata.get('').toDict()['value'][0].keys())[0]

while True:
    try:
      img = pvdata.get('')['value'][0][dtype].reshape([height,width])
      time.sleep(exp*1.01)
      pin = img<np.median(img)*0.5
      # print(np.mean(img))
      rows,cols=np.where(pin>0)
      elements,counts = np.unique(rows,return_counts=True)
      id = np.where(counts>20)[0][0]
      print(elements[id],counts[id])
      time.sleep(1)
    except:
      pass
    # print(cols[np.where(rows==elements[id])])
    # print(elements,counts)
    
    
    # plt.imshow(pin)
    # plt.show()
    
    
    # # Apply edge detection method on the image
    # edges = cv2.Canny(img, 50, 150, apertureSize=3)
    
    # # This returns an array of r and theta values
    # lines = cv2.HoughLines(edges, 1, np.pi/180, 300)
    # print(lines)
    # #The below for loop runs till r and theta values
    # #are in the range of the 2d array
    # for r_theta in lines:
    #     arr = np.array(r_theta[0], dtype=np.float64)
    #     r, theta = arr
    #     # Stores the value of cos(theta) in a
    #     a = np.cos(theta)
    
    #     # Stores the value of sin(theta) in b
    #     b = np.sin(theta)
    
    #     # x0 stores the value rcos(theta)
    #     x0 = a*r
    
    #     # y0 stores the value rsin(theta)
    #     y0 = b*r
    
    #     # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
    #     x1 = int(x0 + 1000*(-b))
    
    #     # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
    #     y1 = int(y0 + 1000*(a))
    
    #     # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
    #     x2 = int(x0 - 1000*(-b))
    
    #     # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
    #     y2 = int(y0 - 1000*(a))
    
    #     # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
    #     # (0,0,255) denotes the colour of the line to be
    #     # drawn. In this case, it is red.
    #     cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
    # # All the changes made in the input image are finally
    # # written on a new image houghlines.jpg

    # cv2.imwrite('linesDetected.jpg', img)
    # exit()
