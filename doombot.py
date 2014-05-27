#!/usr/bin/python3

# This 

import subprocess
import sys
import os
import subprocess
import threading
import config

args = {}

for i in range(len(sys.argv)):
	args[sys.argv[i]] = i

# Options
config.directory = ""    # Optional script directory
config.port      = 5000  # Alternative server port
config.interface = ""    # Alternative server interface
config.script    = ""    # Script to execute
config.cont      = False # Do not restart the process on a SIGABRT+
config.command   = ""


########################################################
#                                                      #
#                   Options validation                 #
#                                                      #
########################################################

if '--help' in args or '-h' in args:
	print("Usage: doombot [options] executable_path [executable_args]\n\
Options:\n\
    --help      (-h)                 : Show options and exit\n\
    --directory (-d) path            : Directory full of scripts to run (optional)\n\
    --script    (-s) path            : Run a single script (optional)\n\
    --port      (-p) port number     : Run the server on a specific port (default:5000)\n\
    --interface (-i) internface_name : Run the server on a specific network interface\n\
    --continue  (  )                 : Continue execution after a SIGABRT (not recommended)\n\
    --version   (-v)                 : Print the version and exit\n")
	exit(0)
elif '--version' in args or '-v' in args:
	print("SFL DoomBot 0.3")
	exit(0)

if '--directory' in args or '-d' in args:
	commandi = 0
	if '--directory' in args:
		commandi = args['--directory']
		del args['--directory']
	else:
		commandi = args['-d']
		del args['-d']
	
	if len(sys.argv) - 1 == commandi:
		print("Missing path")
		exit(1)
	
	directory_tmp = sys.argv[commandi+1]
	
	if not os.path.exists(directory_tmp):
		print("Invalid directory")
		exit(1)
	
	config.directory = directory_tmp
	del args[config.directory]

if  '--script' in args or '-s' in args:
	commandi = 0
	if '--script' in args:
		commandi = args['--script']
		del args['--script']
	else:
		commandi = args['-s']
		del args['-s']
	
	if len(sys.argv) - 1 == commandi:
		print("Missing script path")
		exit(1)
	
	script = sys.argv[commandi+1]
	
	if not os.path.exists(script):
		print("Invalid script path")
		exit(1)
	
	del args[script]

if  '--port' in args or '-p' in args:
	commandi = 0
	if '--port' in args:
		commandi = args['--port']
		del args['--port']
	else:
		commandi = args['-p']
		del args['-p']
	
	if len(sys.argv) - 1 == commandi:
		print("Missing port")
		exit(1)
	
	try:
		port = int(sys.argv[commandi+1])
		if port > 65535:
			raise ValueError('Invalid port number')
	except ValueError:
		print("Invalid port number")
	del args[sys.argv[commandi+1]]

if  '--interface' in args or '-i' in args:
	print("TODO sorry unimplemented yet")
	if '--interface' in args: del args['--interface']
	if '-i' in args: del args['-i']
	exit(1)

if  '--continue' in args:
	del args['--continue']
	cont = True

max_idx = 99999
for arg in args:
	index = args[arg]
	if index != 0 and index < max_idx:
		max_idx = index

if max_idx == 99999:
	print("Missing command")
	exit(1)

sub_range = sys.argv[max_idx:len(sys.argv)]
for i in range(len(sub_range)):
	config.command += " " + sub_range[i]

config.command = config.command.strip()

doombot_path = os.path.dirname(os.path.realpath(__file__)) + "/"

if not os.path.exists(doombot_path+"gdb_wrapper.py"):
	print("Wrapper script not found")
	exit(1)


########################################################
#                                                      #
#                    Start the server                  #
#                                                      #
########################################################

print("Starting the DoomBot server")
print("Executable               : " + config.command              )
print("Port                     : " + str( config.port           ))
print("Continue on Asserts      : " + str( config.cont           ))
print("Using a script directory : " + str( config.directory != ""))
print("Using a script           : " + str( config.script != ""   ))
print()

bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
process = subprocess.Popen(sub_range, stdout=subprocess.PIPE)
output = process.communicate()[0]
#error = process.communicate()[2]

def blabla():
	return "foo"
# Start the server
import server
server.app.run()