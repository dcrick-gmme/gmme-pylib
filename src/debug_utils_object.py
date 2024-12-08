
import os
import sys

import gmmePylib.Utils.CmdLine
import gmmePylib.Utils.Object


g_dbgOn = True

o_init = False
o_initWithCmdLine = True


##-- get tests workspace folder path
#l_testsPath = os.environ.get("_TESTS_WORKSPACEFOLDER", "./tests")
#l_testsUtilsPath = l_testsPath + "/utils"
#
#print("testsPath = " + l_testsPath)
#print("testsUtilsPath = " + l_testsUtilsPath)


#-------------------------------------------------------------------------------
#-- InitWithCmdLine()
#-------------------------------------------------------------------------------
if o_initWithCmdLine:
    #---------------------------------------------------------------------------
    class TClass():

        m_cmdline = None

        m_isopt = False
        m_smtp = None
        m_from = None
        m_subj = None
        m_to = None
        m_cc = None
        m_bcc = None
        m_text = None
        m_textfile = None
        m_priority = None
        m_dbgLevel = None


        def __init__(self):
            l_optfile = os.environ.get("OBJECT_TESTS_OPTFILE", "./custperf.opt")

            self.m_cmdline = gmmePylib.Utils.CmdLine.Create(g_dbgOn)
            self.m_cmdline.AddArgsFile(l_optfile)

            l_members = {}
            l_cmdline = {
                '_obj': self.m_cmdline,
                '_base': 'mailrc',
                'txt1': {'t': gmmePylib.Utils.CmdLine.ISOPT(), 'v': 'm_isopt', 'k': 'txt'},
                'smtp': {'t': gmmePylib.Utils.CmdLine.GETOPTVALUE(), 'v': 'm_smtp'},
                'from': {'t': gmmePylib.Utils.CmdLine.GETOPTVALUE(), 'v': 'm_from'},
                'subj': {'t': gmmePylib.Utils.CmdLine.GETOPTVALUE(), 'v': 'm_subj'},
                'subject': {'t': gmmePylib.Utils.CmdLine.GETOPTVALUE(), 'v': 'm_subj'},
                'to': {'t': gmmePylib.Utils.CmdLine.GETOPTVALUE(), 'v': 'm_to'},
                'cc': {'t': gmmePylib.Utils.CmdLine.GETOPTVALUE(), 'v': 'm_cc'},
                'bcc': {'t': gmmePylib.Utils.CmdLine.GETOPTVALUE(), 'v': 'm_bcc'},
                'text': {'t': gmmePylib.Utils.CmdLine.GETOPTVALUE(), 'v': 'm_text'},
                'textfile': {'t': gmmePylib.Utils.CmdLine.GETOPTVALUE(), 'v': 'm_textfile'},
                'txt': {'t': gmmePylib.Utils.CmdLine.GETOPTVALUE(), 'v': 'm_text'},
                'txtfile': {'t': gmmePylib.Utils.CmdLine.GETOPTVALUE(), 'v': 'm_textfile'},
                'priority': {'t': gmmePylib.Utils.CmdLine.GETOPTVALUE(), 'v': 'm_priority'},
                'dbglevel': {'t': gmmePylib.Utils.CmdLine.GETOPTVALUE(), 'v': 'm_dbgLevel'}
            }
            gmmePylib.Utils.Object.InitWithCmdLine(self, l_members, l_cmdline);

        def Cmdline(self) : return self.m_cmdline


    #-- processing
    l_test = TClass()
    print("we are here")



#-------------------------------------------------------------------------------
#-- Init()
#-------------------------------------------------------------------------------
if o_init:
    #---------------------------------------------------------------------------
    class TClass():
        m_test1 = None
        m_test2 = None
        m_test3 = None

        def __init__(self, a_args):
            self.m_test1 = 'test1'
            self.m_test2 = 'test2'
            self.m_test3 = 'test3'
            self.DumpAttributes('TClass.__init__:')
            l_members = {'SetTest1':'m_test1','SetTest2':'m_test2','SetTest3':'m_test3'}
            gmmePylib.Utils.Object.Init(self, l_members, a_args)

        def DumpAttributes(self, a_str):
            l_keys = list(self.__dict__.keys())
            l_keys.sort()

            print(a_str)
            for l_key in l_keys :
                print('   ' + l_key + ' ==> ' + self.__dict__[l_key])


    #---------------------------------------------------------------------------
    l_args = {
        'SetTest1': 'ValueTest1',
        'setTest2': 'ValueTest2',
        'settest3': 'ValueTest3',
        'anyitem': None
    }
    l_ctest = TClass(l_args)
    l_ctest.DumpAttributes('TClass after creation:')
