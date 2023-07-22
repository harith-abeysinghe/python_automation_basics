import os
import shutil

# Create a new directory
directory_name = 'my_directory'
try:
    os.mkdir(directory_name)
    print("Directory Created")
except FileExistsError:
    print("Directory Exists")

# List the contents of the current directory
source = "C:\\Users\\USER\\Downloads"
files = os.listdir(source)
destination = os.path.join(os.getcwd(), directory_name)
print(source)
print(destination)



# Print the names of all the files and directories
for file in files:
    #print(file)
    # Create the full source file path
    source_file_path = os.path.join(source, file)

    # Create the full destination file path
    destination_file_path = os.path.join(destination, file)

    try:
        # Copy the file from source to destination
        shutil.copy(source_file_path, destination_file_path)
        print(f"Copied: {file}")
    except PermissionError as e:
        print(f"Permission denied for {file}. Skipping...")


# Rename the directory
#os.rename('my_directory', 'new_name')

# Remove the directory
#os.rmdir('new_name')