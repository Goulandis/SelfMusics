import os

folder_path = 'D:\Goulandis\SelfMusics\Tmp'  # Replace 'folder_path' with the actual path to the folder containing the .lrc files

# Get a list of all files in the folder
file_list = os.listdir(folder_path)

# Filter the files to only include those with the .lrc extension
lrc_files = [file for file in file_list if file.endswith('.lrc')]

# Create and open the name.txt file for writing
with open('name.txt', 'w') as output_file:
    # Write each filename to a new line in the file
    for lrc_file in lrc_files:
        output_file.write(lrc_file + '\n')

print("Filenames have been stored in name.txt.")
