
import os
import gmmePylib.Utils.Other
#from gmmePylib.Utils import Other


o_isYesOrNo = True


#-- get tests workspace folder path
l_testsPath = os.environ.get("_TESTS_WORKSPACEFOLDER", "./tests")
l_testsUtilsPath = l_testsPath + "/utils"

print("testsPath = " + l_testsPath)
print("testsUtilsPath = " + l_testsUtilsPath)

#-------------------------------------------------------------------------------
#-- IsYesOrNo
if o_isYesOrNo:
    def testIsYesOrNo(a_val, a_retTrue = True, a_retFalse = False):
        l_ret = gmmePylib.Utils.Other.IsYesOrNo(a_val, a_retTrue, a_retFalse)
        print("IsYesOrNo(", a_val, ",", a_retTrue, ",", a_retFalse, ") = ", l_ret)

    testIsYesOrNo('yes')
    testIsYesOrNo(0)
    testIsYesOrNo(True)
    testIsYesOrNo(False)
    testIsYesOrNo('true')
    testIsYesOrNo('t', 'x', 'y')


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
