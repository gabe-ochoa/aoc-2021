# import subprocess
import os
import sys


python_container_cmd = 'sudo podman run -it --rm -v .:/code python:3.10-slim python /code/{}'.format(
    sys.argv[1])

# Impliment with os.system
os.system(python_container_cmd)

# Impliment with subprocess

# process = subprocess.Popen([python_container_cmd],
#                            stdout=subprocess.PIPE,
#                            stderr=subprocess.PIPE)

# stdout, stderr = process.communicate()
# stdout, stderr
