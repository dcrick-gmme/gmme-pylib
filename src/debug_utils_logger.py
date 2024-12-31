#!/usr/bin/env python
#===============================================================================
# gmme-pylib for Python
# Copyright (c) 2002 - 2024, GMM Enterprises, LLC.
# Licensed under the GMM Software License
# All rights reserved 
#===============================================================================
# Author: David Crickenberger
# ------------------------------------------------------------------------------
# Description:
#   Debug program for Utils.Logger
#===============================================================================

from pathlib import Path
from time import strftime

import datetime
import os
import sys
import time

#import gmmePylib.Utils.CmdLine
import gmmePylib.Utils.Logger


#-------------------------------------------------------------------------------
#-- initialize debug settings
o_dbgTests__ = {
    'test01': True,
    'test02': True,
}

o_dbgfile__ = Path(__file__).name
o_dbglogPath__ = os.environ.get("LOGGER_TESTS_PATH", "./logs")


#-------------------------------------------------------------------------------
#-- test01: see how we process command lines with an array and a string
def test01_():
    l_logger = gmmePylib.Utils.Logger.Create(file = sys.argv[0], logpath = o_dbglogPath__, logfile = 'debug_utils_logger-test01.log', append = True)
    l_logger.Open()
    l_logger.LogRaw('test message 1')
    l_logger.LogRaw('test message 2')
    return


#-------------------------------------------------------------------------------
#-- test02: see how we process command lines with an array and a string
def test02_():
    return


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-- main processing of debug tests
print(o_dbgfile__ + " - beg:")
print(o_dbgfile__ + " :: python version = " + sys.version)
print(o_dbgfile__ + " :: source = " + __file__)
print(o_dbgfile__ + " :: logpath = " + str(o_dbglogPath__))


#-------------------------------------------------------------------------------
#-- process tests
if o_dbgTests__['test01']: test01_()
if o_dbgTests__['test02']: test02_()

print(o_dbgfile__ + " - end:")


#-------------------------------------------------------------------------------
#-- get logpath

l_t1 = time.time()
l_t2 = time.localtime(l_t1)
l_ts = time.strftime('%Y%m%d%H%M%S', l_t2)

l_appname = sys.argv[0]
#l_dirname = os.path.dirname(l_appname)
#l_temp = os.path.splitext(l_appname)
#l_appname = os.path.basename(sys.argv[0])
#l_appname = os.path.splitext(l_appname)[0]

#l_logger = gmmePylib.Utils.Logger.Logger(file=l_appname, logpath=l_logpath, xlogfile='test.log', append=True)
#l_logger = gmmePylib.Utils.Logger.Create(file = l_appname, logpath = l_logpath, logfile = 'debug_utils_logger', append = True)
#l_logger.Open()
#l_logger.LogRaw('test message 1')
#    LogRaw('test message 2')
l_rc = 0



'''
#---------------------------------------------------------------------------
#-- initialize CmdLine Object and pull info from command line for a fixed
#-- file
l_cwd = os.getcwd()

l_cmdline = gmmePylib.Utils.CmdLine.Create(True)
if len(sys.argv) == 1:
    #-- pass .opt file to process from env or default
    l_cmdline.AddArgsFile(l_optfile)
else:
    #-- pass in what is ever on the command line
    l_cmdline.AddArgsArray(sys.argv[1:])

#---------------------------------------------------------------------------
#-- test what was loaded from given .opt
l_rc = l_cmdline.IsOpt('-rptExt')
l_rc = l_cmdline.IsOpt('-rptName')
l_rc = l_cmdline.IsOpt('-xrptName')

l_rc1 = l_cmdline.GetPathOpt('-sfxTmp')
l_rc2 = l_cmdline.GetPathOpt('-sfxTmp2')
l_rc3 = l_cmdline.GetOptCombinedValue('-sfxTmpC')        #, a_sep = os.path.sep)
l_rc4 = l_cmdline.GetOptCombinedValue('-sfxTmpC', a_sep = os.path.sep)

l_rc = l_cmdline.GetPathOpt('-sfxTmp3')
l_rc = False

print("DBG-Utils.CmdLine - end:")
'''