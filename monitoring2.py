import os, sys

used_space = os.popen("df -h / | grep -v Filesystem | awk '{print $5}'").readline().strip()

if used_space < "85%":
    print "OK - %s of disk space used." % used_space
elif used_space >= "85%":
    print "CRITICAL - %s of disk space used." % used_space
else:
    print "Something went wrong"

used_memory = os.popen("cat /proc/meminfo | awk 'FNR == 2 { print $2 }'").readline().strip()

if used_memory < "30000":
	print "CRITICAL - %s bytes of memory is free." % used_memory
elif used_memory >= "30000":
	print "OK - %s bytes of memory is free." % used_memory
else:
    print "Something went wrong" % used_memory
