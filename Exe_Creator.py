import os
import sys
import subprocess

def create_executable(exe_name, destination_folder):
    script_name = sys.argv[0]
    #print(script_name)
    script_path = os.path.abspath(script_name)
    exe_path = os.path.join(destination_folder, exe_name)

    if not os.path.exists(exe_path):
        try:
            subprocess.check_call(['pyinstaller', '--onefile', '--distpath', destination_folder, script_path])
            print(f"Executable created at {exe_path}")
        except subprocess.CalledProcessError:
            print("Failed to create the executable.")
            sys.exit(1)