import psutil

listProcesses = psutil.pids()

print "There are " + str(len(listProcesses)) + " processes running on this server"
print "Processes taking > 0% CPU or Memory:"
print "---------"

for e in listProcesses:
	p = psutil.Process(e)
	if p.cpu_percent(interval=1.0) != 0.0 and p.memory_percent() != 0.0:
		print p.name() + ': ' + 'CPU: ' + str(p.cpu_percent(interval=1.0)) + ' Memory: ' + str(p.memory_percent())

