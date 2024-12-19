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
#   Debug program for Utils.Other
#===============================================================================

import os
import sys

from gmmePylib import *


#-------------------------------------------------------------------------------
#-- initialize debug settings
o_dbgTests__ = {
    'test01': False,
    'test02': True,
    'test03': False,
}

o_dbgfile__ = os.path.basename(__file__)


#-------------------------------------------------------------------------------
#-- test01: test the IsYesOrNo
def test01_():
    l_dbgfunc = o_dbgfile__ + " :: test01"
    print(l_dbgfunc + " -- beg:")

    #--------------------------------------------------------------------------
    #-- define test cases
    l_tests = [
        {'check': 'yes'},
        {'check': 0, 'true': False},
        {'check': True},
        {'check': False},
        {'check': 'true'},
        {'check': 't', 'true': 'x', 'false': 'y'},
    ]

    #--------------------------------------------------------------------------
    #-- process tests
    for l_test in l_tests:
        #-----------------------------------------------------------------------
        #-- determine calling parameters
        l_check = l_test['check']
        l_true = True
        l_false = False
        l_dbgmsg = "   Utils.Other.IsYesOrNo({}"
        if len(l_test) > 1:
            l_true = l_test['true']
            l_dbgmsg = l_dbgmsg + ", {}"
            if len(l_test) > 2:
                l_false = l_test['false']
                l_dbgmsg = l_dbgmsg + ", {}"
        l_dbgmsg = l_dbgmsg + ")"

        #-----------------------------------------------------------------------
        #-- test and output result
        l_ret = Utils.Other.IsYesOrNo(l_check, l_true, l_false)
        l_dbgmsg = l_dbgmsg + " = {}" 
        print(l_dbgfunc + l_dbgmsg.format(l_check, l_true, l_false, l_ret))

    print(l_dbgfunc + " -- end:")


#-------------------------------------------------------------------------------
#-- test02: test loading json files
def test02_():
    l_dbgfunc = o_dbgfile__ + " :: test02"
    print(l_dbgfunc + " -- beg:")

    l_file = "C:\\Users\\DavidCrickenberger\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 8\\Preferences"

    l_json = Utils.Other.OSLoadJson(l_file)

    print(l_dbgfunc + " -- end:")


# #-------------------------------------------------------------------------------
# #-- osDifferent
# if _o_test__['osDifferent']:
#     print("Testing - OSDifferent - Beg::")
#     l_otherTestPath = l_testsUtilsPath + "/other"
    
#     l_files = gmmePylib.Utils.Other.OSFolderList(l_otherTestPath + "/deletefiles/samplefiles/*")
#     #a_path, a_attrib = 0xffffffff, a_attribAnd = True, a_retAttrib = False):
#     print("Testing - OSDifferent - End::")


# '''
#     #-- OSXXXX
#     l_testsUtilsOtherPath = l_testsUtilsPath + "/other"
#     OSMakeFolder(l_testsUtilsOtherPath + "/makefolder/folder1/folder2")

#     OSDeleteFiles(l_testsUtilsOtherPath + "/deletefiles/testfiles/*.out", FOLDERDELETE_OPTS_INCREADONLY())
#     OSDeleteFiles(l_testsUtilsOtherPath + "/deletefiles/testfiles/*.*", FOLDERDELETE_OPTS_INCREADONLY())
# '''

#     #l_path = 'd:\\maersk\\python\\reportdist\\out\\custperf\\*.*'
#     #l_sep = os.path.sep
#     #l_path1 = os.path.dirname(l_path)
#     #l_path2 = os.path.basename(l_path)
#     #l_list1 = OSFolderList('d:\\maersk\\python\\reportdist\\out\\custperf\\*.*', (win32con.FILE_ATTRIBUTE_ARCHIVE | win32con.FILE_ATTRIBUTE_NORMAL))
#     #l_list2 = OSFolderList('d:\\maersk\\python\\reportdist\\out\\custperf\\*.*', (win32con.FILE_ATTRIBUTE_ARCHIVE | win32con.FILE_ATTRIBUTE_NORMAL), a_retAttrib=True)
#     #if l_list1 is not None :
#     #    print(len(l_list1))
#     #else :
#     #    print('nothing was found')
        
#     #l_ret1, l_ret2 = GetTimeSeconds()
#     #l_time = time.time()
#     #l_ret3, l_ret4 = SplitTimeSeconds(l_time)


# print("the end!")


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-- main processing of debug tests
print(o_dbgfile__ + " - beg:")
print(o_dbgfile__ + " :: python version = " + sys.version)
print(o_dbgfile__ + " :: source = " + __file__)

#-------------------------------------------------------------------------------
#-- get tests workspace folder path
l_testsPath = os.environ.get("_TESTS_WORKSPACEFOLDER", "./tests")
l_testsUtilsPath = l_testsPath + "/utils"

print("testsPath = " + l_testsPath)
print("testsUtilsPath = " + l_testsUtilsPath)

#-------------------------------------------------------------------------------
#-- process tests
if o_dbgTests__['test01']: test01_()
if o_dbgTests__['test02']: test02_()

print(o_dbgfile__ + " - end:")
