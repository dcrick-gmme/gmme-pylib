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
import gmmePylib.Utils.Other
#from gmmePylib.Utils import Other


#-------------------------------------------------------------------------------
#-- set what should be tested while debugging
_o_test__ = {
    'isYesOrNo': False,
    'osDifferent': True,
}


#-------------------------------------------------------------------------------
#-- get tests workspace folder path
l_testsPath = os.environ.get("_TESTS_WORKSPACEFOLDER", "./tests")
l_testsUtilsPath = l_testsPath + "/utils"

print("testsPath = " + l_testsPath)
print("testsUtilsPath = " + l_testsUtilsPath)


#-------------------------------------------------------------------------------
#-- IsYesOrNo
if _o_test__['isYesOrNo']:
    def testIsYesOrNo__(a_val, a_retTrue = True, a_retFalse = False):
        l_ret = gmmePylib.Utils.Other.IsYesOrNo(a_val, a_retTrue, a_retFalse)
        print("   IsYesOrNo(", a_val, ",", a_retTrue, ",", a_retFalse, ") = ", l_ret)

    print("Testing - IsYesOrNo - Beg::")
    testIsYesOrNo__('yes')
    testIsYesOrNo__(0)
    testIsYesOrNo__(True)
    testIsYesOrNo__(False)
    testIsYesOrNo__('true')
    testIsYesOrNo__('t', 'x', 'y')
    print("Testing - IsYesOrNo - Beg::")


#-------------------------------------------------------------------------------
#-- IsYesOrNo
if _o_test__['osDifferent']:
    print("Testing - OSDifferent - Beg::")
    l_otherTestPath = l_testsUtilsPath + "/other"
    
    gmmePylib.Utils.Other.OSFolderList(l_otherTestPath + "/deletefiles/samplefiles")
    #a_path, a_attrib = 0xffffffff, a_attribAnd = True, a_retAttrib = False):
    print("Testing - OSDifferent - End::")


'''
    #-- OSXXXX
    l_testsUtilsOtherPath = l_testsUtilsPath + "/other"
    OSMakeFolder(l_testsUtilsOtherPath + "/makefolder/folder1/folder2")

    OSDeleteFiles(l_testsUtilsOtherPath + "/deletefiles/testfiles/*.out", FOLDERDELETE_OPTS_INCREADONLY())
    OSDeleteFiles(l_testsUtilsOtherPath + "/deletefiles/testfiles/*.*", FOLDERDELETE_OPTS_INCREADONLY())
'''

    #l_path = 'd:\\maersk\\python\\reportdist\\out\\custperf\\*.*'
    #l_sep = os.path.sep
    #l_path1 = os.path.dirname(l_path)
    #l_path2 = os.path.basename(l_path)
    #l_list1 = OSFolderList('d:\\maersk\\python\\reportdist\\out\\custperf\\*.*', (win32con.FILE_ATTRIBUTE_ARCHIVE | win32con.FILE_ATTRIBUTE_NORMAL))
    #l_list2 = OSFolderList('d:\\maersk\\python\\reportdist\\out\\custperf\\*.*', (win32con.FILE_ATTRIBUTE_ARCHIVE | win32con.FILE_ATTRIBUTE_NORMAL), a_retAttrib=True)
    #if l_list1 is not None :
    #    print(len(l_list1))
    #else :
    #    print('nothing was found')
        
    #l_ret1, l_ret2 = GetTimeSeconds()
    #l_time = time.time()
    #l_ret3, l_ret4 = SplitTimeSeconds(l_time)


print("the end!")
