import subprocess

# completed = subprocess.run(["ls","-l"],
#                            capture_output=True,
#                            text=True,
#                            check=True)

try:
    completed = subprocess.run(["false"],
                            capture_output=True,
                            text=True,
                            check=True)
    print(type(completed))
    print(completed.args)
    print(completed.stdout)
    print(completed.stderr)
    print(completed.returncode)
except subprocess.CalledProcessError as err:
    print("Error")
