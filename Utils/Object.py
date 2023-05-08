#!/usr/bin/env python
#===============================================================================
# gmme-pylib for Python
# Copyright (c) 2002 - 2023, GMM Enterprises, LLC.
# Licensed under the GMM Software License
# All rights reserved 
#===============================================================================
#	Author:	David Crickenberger
# ------------------------------------------------------------------------------
#	Packages:
#		Utils::CmdLine
#
# 	Description:
#		Command line processor module.
#
#===============================================================================
# $Log: $
#===============================================================================
import Utils.CmdLine
import Utils.Other


#-------------------------------------------------------------------------------
#-- globals
#-------------------------------------------------------------------------------
g_dbgOn = True


#-------------------------------------------------------------------------------
#-- 
#-------------------------------------------------------------------------------




#-------------------------------------------------------------------------------
#-- init: initial object members from dict object
#-------------------------------------------------------------------------------
def Init(a_obj, a_members, a_args) :
    #---------------------------------------------------------------------------
    #-- produce a list of uppercase keys to map parameters back using case
    #-- insenstive values
    l_members = Utils.Other.CreateUpperCaseDictKeys(a_members)
    #l_members = {}
    #for l_key in list(a_members.keys()) :
    #    l_members[l_key.upper()] = l_key


    #---------------------------------------------------------------------------
    #-- process the a_args
    l_found = False
    for l_arg in list(a_args.keys()) :
        if l_arg.upper() in l_members :
            a_obj.__dict__[a_members[l_members[l_arg.upper()]]] = a_args[l_arg]
            l_found = True

    return l_found


#-------------------------------------------------------------------------------
#-- init: initial object members from dict object
#-------------------------------------------------------------------------------
def InitWithCmdLine(a_obj, a_members, a_cmdline, a_args = None) :

    #---------------------------------------------------------------------------
    #-- debug stuff
    #if g_dbgOn :
    #    print('DBG-Utils.Object.initWithCmdLine == args - beg:')
    #    print('DBG-a_obj -- beg:')
    #    print(dump(a_obj))
    #    print('DBG-a_obj -- end:')
    #    #if a_members is not None :
    #    #    print('DBG ===========================================')
    #    #    print('DBG-a_members -- beg:')
    #    #    pprint.pprint(a_members)
    #    #    print('DBG-a_members -- end:')
    #    print('DBG ===========================================')
    #    print('DBG-a_cmdline -- beg:')
    #    print(dump(a_cmdline))
    #    print('DBG-a_cmdline -- end:')
    #    #print('DBG ===========================================')
    #    #print('DBG-a_args -- beg:')
    #    #print(Dumper( @a_args );
    #    #print('DBG-a_args -- end:')
    #    print('DBG-Utils::Object::initWithCmdLine == args - end:')


    #---------------------------------------------------------------------------
    #-- 1st call default init object and see if cmdline was returned
    l_found = False
    l_obj = None

    if a_members is not None : l_found = init(a_obj, a_members, a_args)
    if a_args is not None :
        if isinstance(a_args[0], Utils.CmdLine) :
            l_obj = a_args[0]

    if l_obj is None :
        if '_obj' in a_cmdline : l_obj = a_cmdline['_obj']

    if l_obj is None : return l_found        


    #---------------------------------------------------------------------------
    #-- 2nd determine base and process command line options
    l_base = '-' + a_cmdline['_base']
    for l_key in list(a_cmdline.keys()) :
        #-----------------------------------------------------------------------
        #-- determine key, type and opt values
        if l_key == '_obj' or l_key == '_base' : continue

        l_keyt = a_cmdline[l_key]['t']
        l_keyv = a_cmdline[l_key]['v']

        if 'k' in a_cmdline[l_key] :
            l_opt = l_base + a_cmdline[l_key]['k']
        else :
            l_opt = l_base + l_key
        l_optFound = l_obj.IsOpt(l_opt)
        if l_optFound : l_found = True


        #-----------------------------------------------------------------------
        #-- process based on cmdline key type
        if l_keyt == Utils.CmdLine.ISOPT() :
            a_obj.__dict__[l_keyv] = l_optFound
            continue

        if not l_optFound : continue

        #-- the next set of calls to cmdline use the current objects members
        #-- as default value.  make sure it exists
        l_defValue = None
        if l_keyv in a_obj.__dict__ : l_defValue = a_obj.__dict__[l_keyv]

        if l_keyt == Utils.CmdLine.GETOPTVALUE() or l_keyt == Utils.CmdLine.GETOPTVALUEDEF() :
            if 'd' in a_cmdline[l_key] : l_defValue = a_cmdline[l_key]['d']
            a_obj.__dict__[l_keyv] = l_obj.GetOptValue(l_opt, l_defValue)
            continue

        if l_keyt == Utils.CmdLine.GETPATHOPT() :
            a_obj.__dict__[l_keyv] = l_obj.GetPathOpt(l_opt, l_defValue)
            continue

        #-- process dblogon stuff
        if l_keyt != Utils.CmdLine.GETDBLOGON() : continue

        l_keyvc = a_cmdline[l_key]['vc']
        l_keyvn = a_cmdline[l_key]['vn']
        l_keyvp = a_cmdline[l_key]['vp']
        l_keyvu = a_cmdline[l_key]['vu']
        
        l_dblogon = l_obj.GetDBLogon(l_opt)
        l_tmp = l_dblogon[0].lower()
        if l_tmp in ['ado', 'db2', 'mysql', 'odbc', 'oracle'] :
            if len(l_dblogon) == 2 :
                a_obj.__dict__[l_keyvc] = l_dblogon[1]
            else :
                a_obj.__dict__[l_keyvu] = l_dblogon[1]
                a_obj.__dict__[l_keyvp] = l_dblogon[2]
                a_obj.__dict__[l_keyvc] = l_dblogon[3]
        else :
            #-- old format
            a_obj.__dict__[l_keyvu] = l_dblogon[1]
            a_obj.__dict__[l_keyvp] = l_dblogon[2]
            a_obj.__dict__[l_keyvc] = l_dblogon[3]

    return l_found


#===============================================================================
# Self test of module
#===============================================================================
if __name__ == "__main__" :

    import Utils.CmdLine

    class Test() :

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

        def __init__(self) :
            self.m_cmdline = Utils.CmdLine.Create()
            self.m_cmdline.AddArgsFile('CmdLineTest\\custperf.opt')

            l_members = {}
            l_cmdline = {
                '_obj' : self.m_cmdline,
                '_base' : 'mailrc',
                'txt1' : {'t' : Utils.CmdLine.ISOPT(), 'v' : 'm_isopt', 'k' : 'txt'},
                'smtp' : {'t' : Utils.CmdLine.GETOPTVALUE(), 'v' : 'm_smtp'},
                'from' : {'t' : Utils.CmdLine.GETOPTVALUE(), 'v' : 'm_from'},
                'subj' : {'t' : Utils.CmdLine.GETOPTVALUE(), 'v' : 'm_subj'},
                'subject' : {'t' : Utils.CmdLine.GETOPTVALUE(), 'v' : 'm_subj'},
                'to' : {'t' : Utils.CmdLine.GETOPTVALUE(), 'v' : 'm_to'},
                'cc' : {'t' : Utils.CmdLine.GETOPTVALUE(), 'v' : 'm_cc'},
                'bcc' : {'t' : Utils.CmdLine.GETOPTVALUE(), 'v' : 'm_bcc'},
                'text' : {'t' : Utils.CmdLine.GETOPTVALUE(), 'v' : 'm_text'},
                'textfile' : {'t' : Utils.CmdLine.GETOPTVALUE(), 'v' : 'm_textfile'},
                'txt' : {'t' : Utils.CmdLine.GETOPTVALUE(), 'v' : 'm_text'},
                'txtfile' : {'t' : Utils.CmdLine.GETOPTVALUE(), 'v' : 'm_textfile'},
                'priority' : {'t' : Utils.CmdLine.GETOPTVALUE(), 'v' : 'm_priority'},
                'dbglevel' : {'t' : Utils.CmdLine.GETOPTVALUE(), 'v' : 'm_dbgLevel'}
            }
#            initWithCmdLine(self, l_members, l_cmdline);
            InitWithCmdLine(self, None, l_cmdline);

        def Cmdline(self) : return self.m_cmdline

    l_test = Test()
#    print(dump(l_test))
    
    l_rc = 0

    
    #my %l_members =
    #(
    #);
    #
    #my %l_cmdline =
    #(
    #	_obj			=> $a_app->cmdline( ),
    #	_base			=> $a_base,
    #	smtp			=> { t => Utils::CmdLine::GETOPTVALUE, v => \$self->{m_smtp} },
    #	from			=> { t => Utils::CmdLine::GETOPTVALUE, v => \$self->{m_from} },
    #	subj			=> { t => Utils::CmdLine::GETOPTVALUE, v => \$self->{m_subj} },
    #	subject		=> { t => Utils::CmdLine::GETOPTVALUE, v => \$self->{m_subj} },
    #	to				=> { t => Utils::CmdLine::GETOPTVALUE, v => \$self->{m_to} },
    #	cc				=> { t => Utils::CmdLine::GETOPTVALUE, v => \$self->{m_cc} },
    #	bcc			=> { t => Utils::CmdLine::GETOPTVALUE, v => \$self->{m_bcc} },
    #	text			=> { t => Utils::CmdLine::GETOPTVALUE, v => \$self->{m_text} },
    #	textfile		=> { t => Utils::CmdLine::GETOPTVALUE, v => \$self->{m_textfile} },
    #	txt			=> { t => Utils::CmdLine::GETOPTVALUE, v => \$self->{m_text} },
    #	txtfile		=> { t => Utils::CmdLine::GETOPTVALUE, v => \$self->{m_textfile} },
    #	priority		=> { t => Utils::CmdLine::GETOPTVALUE, v => \$self->{m_priority} },
    #	dbglevel		=> { t => Utils::CmdLine::GETOPTVALUE, v => \$self->{m_dbgLevel} },
    #);
    #Utils::Object::initWithCmdLine( $self, \%l_members, \%l_cmdline, @a_args );
    #   
    
    
    #class Test() :
    #    m_test1 = None
    #    m_test2 = None
    #    m_test3 = None
    #    
    #    def __init__(self, a_args) :
    #        self.m_test1 = 'test1'
    #        self.m_test2 = 'test2'
    #        self.m_test3 = 'test3'
    #        self.PrintAttr('attr1')
    #        l_members = {'SetTest1':'m_test1','SetTest2':'m_test2','SetTest3':'m_test3'}
    #        init(self, l_members, a_args)
    #
    #
    #    def PrintAttr(self, a_str) :
    #        l_keys = list(self.__dict__.keys())
    #        l_keys.sort()
    #        for l_key in l_keys :
    #            print(a_str + ' -- ' + l_key + ' ==> ' + self.__dict__[l_key])
    #        
    #
    ##--------------------------------------
    #l_args = {
    #    'SetTest1': 'ValueTest1',
    #    'setTest2': 'ValueTest2',
    #    'settest3': 'ValueTest3',
    #    'anyitem': None
    #}
    #l_test = Test(l_args)
            

