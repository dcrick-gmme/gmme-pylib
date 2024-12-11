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

import os
import sys

import gmmePylib.Utils.CmdLine


#-------------------------------------------------------------------------------
#-- get tests opt and output
l_optfile = os.environ.get("CMDLINE_TESTS_OPTFILE", "./custperf.opt")

print("optfile = " + l_optfile)

#---------------------------------------------------------------------------
#-- output python version
print("DBG-Utils.CmdLine - beg:")
print("DBG-Utils.CmdLine - python version = " + sys.version)
                                  
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
