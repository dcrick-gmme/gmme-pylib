
import os
import gmmePylib.Utils.Other


def test_utils_other():
    #-- get tests workspace folder path
    l_testsPath = os.environ.get("_TESTS_WORKSPACEFOLDER", "./tests")
    l_testsUtilsPath = l_testsPath + "/utils"

    print("testsPath = " + l_testsPath)
    print("testsUtilsPath = " + l_testsUtilsPath)

    assert 1 == 0
'''
    #-- IsYesOrNo
    def testIsYesOrNo(a_val, a_retTrue = True, a_retFalse = False):
        l_ret = IsYesOrNo(a_val, a_retTrue, a_retFalse)
        print("IsYesOrNo(", a_val, ",", a_retTrue, ",", a_retFalse, ") = ", l_ret)

    testIsYesOrNo('yes')
    testIsYesOrNo(0)
    testIsYesOrNo(True)
    testIsYesOrNo(False)
    testIsYesOrNo('true')
    testIsYesOrNo('t', 'x', 'y')

    print("the end!")
'''