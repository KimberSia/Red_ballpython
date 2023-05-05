import os

# Get list of files in current directory
files = os.listdir()

# Create list of dictionaries
file_list = []
for file in files:
    file_dict = {
        "path": file,
        "size": os.path.getsize(file),
       
       
    }
    file_list.append(file_dict)

# Print list of dictionaries
print(file_list)