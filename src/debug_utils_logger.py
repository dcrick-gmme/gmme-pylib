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
    'test01': False,
    'test02': False,
    'test03': True,
}

o_dbgfile__ = Path(__file__).name
o_dbglogPath__ = os.environ.get("LOGGER_TESTS_PATH", "./logs")


#-------------------------------------------------------------------------------
#-- testCommon_: call each logging helper using logger object and logger module
def testCommon_(a_logger:gmmePylib.Logger.Logger, a_test:str):

    a_logger.Info(a_test + " -- beg:")

    l_tab = "   "

    l_object = l_tab + "object."
    l_module = l_tab + "module."
    l_line = l_tab + "-----------------"

    a_logger.Debug(l_object + "Debug")
    a_logger.Fatal(l_object + "Fatal")
    a_logger.Info(l_object + "Info")
    a_logger.Sql(l_object + "Sql")
    a_logger.Warn(l_object + "Warn")
    a_logger.Warning(l_object + "Warning")

    a_logger.LogInfo(l_line)
    a_logger.LogDebug(l_object + "LogDebug")
    a_logger.LogFatal(l_object + "LogFatal")
    a_logger.LogInfo(l_object + "LogInfo")
    a_logger.LogSql(l_object + "LogSql")
    a_logger.LogWarn(l_object + "LogWarn")
    a_logger.LogWarning(l_object + "LogWarning")

    gmmePylib.Utils.Logger.Info(l_line)
    gmmePylib.Utils.Logger.Debug(l_module + "Debug")
    gmmePylib.Utils.Logger.Fatal(l_module + "Fatal")
    gmmePylib.Utils.Logger.Info(l_module + "Info")
    gmmePylib.Utils.Logger.Sql(l_module + "Sql")
    gmmePylib.Utils.Logger.Warn(l_module + "Warn")
    gmmePylib.Utils.Logger.Warning(l_module + "Warning")

    gmmePylib.Utils.Logger.LogInfo(l_line)
    gmmePylib.Utils.Logger.LogDebug(l_module + "LogDebug")
    gmmePylib.Utils.Logger.LogFatal(l_module + "LogFatal")
    gmmePylib.Utils.Logger.LogInfo(l_module + "LogInfo")
    gmmePylib.Utils.Logger.LogSql(l_module + "LogSql")
    gmmePylib.Utils.Logger.LogWarn(l_module + "LogWarn")
    gmmePylib.Utils.Logger.LogWarning(l_module + "LogWarning")

    a_logger.Info(a_test + " -- end:")


#-------------------------------------------------------------------------------
#-- test01: see how we process command lines with an array and a string
def test01_():
    l_logger = gmmePylib.Utils.Logger.Create(file = sys.argv[0], logpath = o_dbglogPath__, logfile = 'debug_utils_logger-test01.log', append = True)
    l_logger.Open()
    l_logger.LogRaw('test message 1')
    l_logger.LogRaw('test message 2')


#-------------------------------------------------------------------------------
#-- test02: call each logging helper with a fixed log file that appends (both
#--         using the obj and the module)
def test02_():
    l_logger = gmmePylib.Utils.Logger.Create(file = sys.argv[0], logpath = o_dbglogPath__, logfile = 'debug_utils_logger-test02.log', append = True)
    l_logger.Open()
    testCommon_(l_logger, 'test02')


#-------------------------------------------------------------------------------
#-- test03: call each logging helper with a fixed log file that overwrites using
# --        both the obj and the module
def test03_():
    l_logger = gmmePylib.Utils.Logger.Create(file = sys.argv[0], logpath = o_dbglogPath__, logfile = 'debug_utils_logger-test03.log', append = False)
    l_logger.Open()
    testCommon_(l_logger, 'test03')



''' 
def Debug(a_msg) :
    if _g_loggerObj__ is not None : _g_loggerObj__.LogDebug(a_msg, 1)
def Fatal(a_msg) :
    if _g_loggerObj__ is not None : _g_loggerObj__.LogFatal(a_msg, 1)
def Info(a_msg) :
    if _g_loggerObj__ is not None : _g_loggerObj__.LogInfo(a_msg, 1)
def Raw(a_msg) :
    if _g_loggerObj__ is not None : _g_loggerObj__.LogRaw(a_msg, 1)
def Sql(a_msg) :
    if _g_loggerObj__ is not None : _g_loggerObj__.LogSql(a_msg, 1)
def Warn(a_msg) :
    if _g_loggerObj__ is not None : _g_loggerObj__.LogWarning(a_msg, 1)
def Warning(a_msg) :
    if _g_loggerObj__ is not None : _g_loggerObj__.LogWarning(a_msg, 1)

def LogDebug(a_msg) :
    if _g_loggerObj__ is not None : _g_loggerObj__.LogDebug(a_msg, 1)
def LogFatal(a_msg) :
    if _g_loggerObj__ is not None : _g_loggerObj__.LogFatal(a_msg, 1)
def LogInfo(a_msg) :
    if _g_loggerObj__ is not None : _g_loggerObj__.LogInfo(a_msg, 1)
#def LoggerGlobalFunctions():
#    global LogRaw
def LogRaw(a_msg) :
    if _g_loggerObj__ is not None : _g_loggerObj__.LogRaw(a_msg, 1)
def LogSql(a_msg) :
    if _g_loggerObj__ is not None : _g_loggerObj__.LogSql(a_msg, 1)
def LogWarn(a_msg) :
    if _g_loggerObj__ is not None : _g_loggerObj__.LogWarning(a_msg, 1)
def LogWarning(a_msg) :
    if _g_loggerObj__ is not None : _g_loggerObj__.LogWarning(a_msg, 1)
'''
















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
if o_dbgTests__['test03']: test03_()

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
