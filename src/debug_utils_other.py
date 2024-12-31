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
from pathlib import Path


#-------------------------------------------------------------------------------
#-- initialize debug settings
o_dbgTests__ = {
    'test01': False,
    'test02': True,
    'test03': False,
    'test04': False,
}

o_dbgfile__ = str(Path(__file__).name)


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-- test01: test IsBool
def test01_():
    l_dbgfunc = o_dbgfile__ + " :: test01"
    print(l_dbgfunc + " -- beg:")

    #---------------------------------------------------------------------------
    #-- define test cases
    l_tests = [
        ['str: yes', 'yes'],
        ['int: 0', 0],
        ['int: 5', 5],
        ['str: t', 't'],
        ['str: False', 'False'],
        ['str: x', 'x'],
        ['bool: True', True],
        ['bool: False', False],
        ['list: []', []],
    ]

    #---------------------------------------------------------------------------
    #-- process tests
    for l_test in l_tests:
        print(l_dbgfunc + "   Utils.Other.IsBool(" + l_test[0] + ") = " + str(Utils.Other.IsBool(l_test[1])))

    print(l_dbgfunc + " -- end:")


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-- test02: test the IsYesOrNo/IsTrueOrFalse
def test02_():
    l_dbgfunc = o_dbgfile__ + " :: test02"
    print(l_dbgfunc + " -- beg:")

    #---------------------------------------------------------------------------
    #-- define test cases
    l_tests = [
        {'call': 'oo', 'msg': 'bool: False', 'args': [False]},
        {'call': 'tf', 'msg': 'bool: True', 'args': [True]},
        {'call': 'tf', 'msg': 'str: T, str: istrue', 'args': ['T', 'istrue']},
        {'call': 'tf', 'msg': 'str: T, str: False, str: True', 'args': ['T', 'False', 'True']},
        {'call': 'yn', 'msg': 'bool: True', 'args': [True]},
        {'call': 'yn', 'msg': 'str: Yes', 'args': ['Yes']},
        {'call': 'yn', 'msg': 'str: n', 'args': ['n']},
    ]

    #---------------------------------------------------------------------------
    #-- process tests
    for l_test in l_tests:
        #-----------------------------------------------------------------------
        #-- setup test
        l_check = l_test['args'][0]
        l_true = True
        l_false = False

        if len(l_test['args']) > 1: l_true = l_test['args'][1]
        if len(l_test['args']) > 2: l_false = l_test['args'][2]

        #-----------------------------------------------------------------------
        #-- make call
        l_ret = None
        l_func = ''
        if l_test['call'] == 'oo':
            l_func = 'IsOnOrOff'
            l_ret = Utils.Other.IsOnOrOff(l_check, l_true, l_false)
        if l_test['call'] == 'tf':
            l_func = 'IsTrueOrFalse'
            l_ret = Utils.Other.IsTrueOrFalse(l_check, l_true, l_false)
        elif l_test['call'] == 'yn':
            l_func = 'IsYesOrNo'
            l_ret = Utils.Other.IsYesOrNo(l_check, l_true, l_false)
                
        #-----------------------------------------------------------------------
        #-- print result
        print(l_dbgfunc + "   Utils.Other." + l_func + "(" + l_test['msg'] + ") = " + str(l_ret))

    print(l_dbgfunc + " -- end:")


#-------------------------------------------------------------------------------
#-- test03: test loading json files
def test03_():
    l_dbgfunc = o_dbgfile__ + " :: test03"
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
