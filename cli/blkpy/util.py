import subprocess
import shlex
import json

def run_command(command):
	cmd = shlex.split(command)
	output = subprocess.check_output(cmd)
	return output

def run_lsblk(device):
	command = f'llsblk -J -o NAME,SIZE,TYPE,MOUNTPOINT'
	output = run_command(command)
	devices = json.loads(output)['blockdevices']

	for parent in devices:
		if parent['name'] == device:
			return parent
		for child in parent.get('children', []):
			if child['name'] == device:
				return child