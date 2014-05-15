#!/usr/bin/env python

import getopt, sys
import os, re

def version():
        print 'check_nimap.py 0.1'
        print 'Eduardo Ramos <eduardo@freedominterface.org>'
        sys.exit(3)

def usage():
        print 'check_nimap.py [-v]'
        sys.exit(3)

def main():
        minimal = 0
        critical = 0
        warning = 0
        cmd = 'doveadm -f flow who'
        count_per_login = 0
        count_total = 0

        try:
                opts, args = getopt.getopt(sys.argv[1:], 'vh')
        except getopt.GetoptError as err:
                print str(err)
                usage()
                sys.exit(3)
                
        for o, a in opts:
                if o == '-v':
                        version()
                else:
                        usage()
                        assert False, 'unhandled option'

        pd = os.popen(cmd, 'r', 10240)
        for line in pd:
                m = re.search(r'#=(\d+)', line, rc.I)
                if m:
                        count_per_login = count_per_login + 1
                        count_total = count_total + int(m.group(1))

        print "# IMAP OK - ({0}/{1}) (users/total)|nusers={0} nimap={1}".format(count_per_login,count_total)
        sys.exit(0)

if __name__ == '__main__':
        main()
