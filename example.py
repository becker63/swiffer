import subprocess

a = subprocess.check_output('cat /home/becker/code/spikdev2/spikedev/README.md', shell=True)

print(a)