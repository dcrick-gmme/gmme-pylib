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
#   Debug program for Utils.CmdLine
#===============================================================================

from pathlib import Path
from gmmePylib import *

import os
import sys


#-------------------------------------------------------------------------------
#-- initialize debug settings
o_dbgTests__ = {
    'test01': True,
    'test02': True,
}

o_dbgfile__ = Path(__file__).name


#-------------------------------------------------------------------------------
#-- test01: see how we process command lines with an array and a string
def test01_():
    l_dbgfunc = o_dbgfile__ + " :: test01"
    print(l_dbgfunc + " -- beg:")

    l_cmdline = Utils.CmdLine.Create(True)
    l_cmdline.AddArgs(sys.argv[1:])
    l_cmdline.AddArgs("-this is -another test -tosee -what")
    l_cmdline.Dump()

    print(l_dbgfunc + " -- end:")


#-------------------------------------------------------------------------------
#-- test02: see how we process command lines starting with env variable
#--         containing opt file and a bad name opt file
def test02_():
    l_dbgfunc = o_dbgfile__ + " :: test02"
    print(l_dbgfunc + " -- beg:")

    #---------------------------------------------------------------------------
    #-- test good filename
    print(l_dbgfunc + " -- good file -- beg:")
    l_optfile = os.environ.get("CMDLINE_TESTS_OPTFILE", "./custperf.opt")
    print("optfile = " + l_optfile)

    l_cmdline = Utils.CmdLine.Create(True)
    l_cmdline.AddArgsFile(l_optfile)
    print(l_dbgfunc + " -- good file -- end:")

    #---------------------------------------------------------------------------
    #-- test bad filename
    print(l_dbgfunc + " -- good bad -- beg:")
    l_optfileBad = os.environ.get("CMDLINE_TESTS_OPTFILE_BAD", "./custperfx.opt")
    l_cmdline = None
    try:
        l_cmdline = Utils.CmdLine.Create(True)
        l_cmdline.AddArgsFile(l_optfileBad)
    except Exception as ex_:
        return None
    print(l_dbgfunc + " -- good bad -- end:")


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-- main processing of debug tests
print(o_dbgfile__ + " - beg:")
print(o_dbgfile__ + " :: python version = " + sys.version)
print(o_dbgfile__ + " :: source = " + __file__)


#-------------------------------------------------------------------------------
#-- process tests
if o_dbgTests__['test01']: test01_()
if o_dbgTests__['test02']: test02_()

print(o_dbgfile__ + " - end:")


#---------------------------------------------------------------------------
#-- test what was loaded from given .opt
"""
l_rc = l_cmdline.IsOpt('-rptExt')
l_rc = l_cmdline.IsOpt('-rptName')
l_rc = l_cmdline.IsOpt('-xrptName')

l_rc1 = l_cmdline.GetPathOpt('-sfxTmp')
l_rc2 = l_cmdline.GetPathOpt('-sfxTmp2')
l_rc3 = l_cmdline.GetOptCombinedValue('-sfxTmpC')        #, a_sep = os.path.sep)
l_rc4 = l_cmdline.GetOptCombinedValue('-sfxTmpC', a_sep = os.path.sep)

l_rc = l_cmdline.GetPathOpt('-sfxTmp3')
l_rc = False
"""

#print("DBG-Utils.CmdLine - end:")
