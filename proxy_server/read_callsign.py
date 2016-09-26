#!/usr/bin/python
from sys import stdout
import os
import subprocess
import re
import time
import json

timestampFormat = "{0:0>4}-{1:0>2}-{2:0>2} {3:0>2}:{4:0>2}:{5:0>2} {6}"
scanRE = re.compile("([0-9]{4})\.([0-9]{2})\.([0-9]{2})\s([0-9]{2}):([0-9]{2}):([0-9]{2})\s([A-Z]{3})\s(.*)")
while 1:
	searchStatus = False
	cmd = subprocess.Popen("tail -n 10 "+os.path.abspath("ELProxy.log"), shell=True, stdout=subprocess.PIPE)
	for line in reversed(list(cmd.stdout)):
		try:
			if not searchStatus:
				lineData = re.findall(scanRE, line)
				# print "                           =>", lineData[0]
				if("Ready for new client connection." in lineData[0][7]):
					print json.dumps({
						"status":"FREE",
						"timestamp":timestampFormat.format(*lineData[0])
					}, ensure_ascii=False)
					searchStatus = True
				elif("Disconnected." in lineData[0][7]):
					print json.dumps({
						"status":"FREE",
						"timestamp":timestampFormat.format(*lineData[0])
					}, ensure_ascii=False)
					searchStatus = True
				else:
					callsignCheck = re.findall("Client authenticated \(call=(.*)\)", lineData[0][7])
					if (not not callsignCheck) and (not not callsignCheck[0]):
						print json.dumps({
							"status":"USED",
							"callsign":callsignCheck[0],
							"timestamp":timestampFormat.format(*lineData[0])
						}, ensure_ascii=False)
						searchStatus = True
		except IndexError:
			print json.dumps({"error": "Index Out of range"}, ensure_ascii=False)
	if not searchStatus:
		print json.dumps({"status":"UNKNOW"}, ensure_ascii=False)
	stdout.flush()
	time.sleep(5)