#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Log PV in a file
    
'''
from __future__ import print_function

import os
import time
import numpy as np

from epics import PV
from datetime import datetime

import log

variableDict = {
        'AD_Prefix': '2bmbSP1:',         # options: 1. PointGrey: '2bmbPG3:', 2. Gbe '2bmbSP1:' 
        'Station': '2-BM-A'
        }

global_PVs = {}

def init_general_PVs(global_PVs, variableDict):

    # shutter PVs 2bma:D1Dmm_raw.VAL
    global_PVs['Temperature'] = PV('2bma:ET2k:2:Temperature.VAL')
    global_PVs['HDF1_FullFileName_RBV'] = PV(variableDict['AD_Prefix'] + 'HDF1:FullFileName_RBV')

def main():

    # create logger
    home = os.path.expanduser("~")
    logs_home = home + '/logs/'

    # make sure logs directory exists
    if not os.path.exists(logs_home):
        os.makedirs(logs_home)

    lfname = logs_home + 'temperature_' + datetime.strftime(datetime.now(), "%Y-%m-%d_%H:%M:%S") + '.log'
    log.setup_custom_logger(lfname)
   
    init_general_PVs(global_PVs, variableDict)
    try:
        while True:
            h5fname = global_PVs['HDF1_FullFileName_RBV'].get()
            h5fname_str = "".join([chr(item) for item in h5fname])
            temp = global_PVs['Temperature'].get()
            log.info('Temperature: %4.4f °C;  %s' % (temp, h5fname_str))            
            time.sleep(5)   
    except KeyboardInterrupt:
        log.warning('interrupted!')
        log.warning('Log information saved at: %s', lfname)

if __name__ == '__main__':
    main()
