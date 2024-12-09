
from time import strftime

import datetime
import os
import sys
import time

#import gmmePylib.Utils.CmdLine
import gmmePylib.Utils.Logger


#-------------------------------------------------------------------------------
#-- get logpath
l_logpath = os.environ.get("LOGGER_TESTS_PATH", "./logs")

print("logpath = " + l_logpath)

l_t1 = time.time()
l_t2 = time.localtime(l_t1)
l_ts = time.strftime('%Y%m%d%H%M%S', l_t2)

l_appname = sys.argv[0]
#l_dirname = os.path.dirname(l_appname)
#l_temp = os.path.splitext(l_appname)
#l_appname = os.path.basename(sys.argv[0])
#l_appname = os.path.splitext(l_appname)[0]

#l_logger = gmmePylib.Utils.Logger.Logger(file=l_appname, logpath=l_logpath, xlogfile='test.log', append=True)
l_logger = gmmePylib.Utils.Logger.CreateLogger(file = l_appname, logpath = l_logpath, logfile = 'debug_utils_logger', append = True)
l_logger.Open()
l_logger.LogRaw('test message 1')
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