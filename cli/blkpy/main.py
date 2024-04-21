import click
from blkpy.util import run_lsblk

@click.command()
@click.option('--verbose','-v', is_flag=True)
@click.argument('device') 
def main(device, verbose):
	print(f"Device: {device}")
	print(f"Verbose: {verbose} ")
	try:
	    print(f"	'{run_lsblk(device)}'")
	except FileNotFoundError as err:
		print(f"error! It is possible that lsblk is not around: {str(err)}")

