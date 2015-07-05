#!/usr/bin/env python

import os
from subprocess import Popen, PIPE, STDOUT

# dmenu constants
DMENU_CACHE = os.path.expanduser('~/.dmenu_cache')
DMENU_COMMAND = [
            'dmenu',
            '-p', 'command:',
            '-sb', '#DD4814',
            '-l', '10',
            '-fn', 'Ubuntu-10'
        ]

## our custom commands
#commands = {
#        'nodesktop': 'nautilus --no-desktop'
#    }
commands = {}

# check if local cache exists
if not os.path.exists(DMENU_CACHE):
    os.system('dmenu_path > /dev/null')

# load command cache and combine with our commands
with open(DMENU_CACHE, 'r') as raw_file:
    system_commands = raw_file.read()

output = commands.keys()
output.sort()

# create a process
process = Popen(DMENU_COMMAND, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
selection = process.communicate(input='{0}\n{1}'.format('\n'.join(output), system_commands))[0]

# get command based on selection and execute it
if selection.strip() != '':
    command = commands[selection] if commands.has_key(selection) else selection
    os.system(command)
