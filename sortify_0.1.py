import os
import re
import datetime

# specify the directory containing your files to update
directory_path = 'your_path_here'

# prompt user to input directory if the path is unedited
if directory_path == 'your_path_here':
    directory_path = str(input('Enter your directory path:'))

# import subprocess to run exiftool without installing pyexiftool
import subprocess


def update_metadata(file_path):
    """
    Takes the file path as an input and searches it for a date in the forms YYYY-MM-DD HH mm ss,
    YYYY MM DD HH mm ss, YYYY-MM-DD HH:mm:ss and YYYY-MM-DD. It takes this date string and puts it in datetime format then
    applies the new datetime to the file metadata and prints a confirmation output. If a date cannnot be found 
    in the filename it will print an error message and move on. 
    Parameters:
        file_path
    Returns: 
        none
    """
    try:
        # extract date from the file name into date_match
        date_match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2} \d{2} \d{2})|(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})|(\d{4} \d{2} \d{2} \d{2} \d{2} \d{2})', file_path)
        if date_match:
            creation_date_str = date_match.group(1)
            creation_date = datetime.datetime.strptime(creation_date_str, '%Y-%m-%d %H %M %S')

            # update creation date in file metadata using subprocess exiftool
            subprocess.run(['exiftool', '-FileModifyDate=' + creation_date.strftime('%Y:%m:%d %H:%M:%S'), file_path])

            # print confirmation of updated metadata
            print(f"Updated metadata for {filename}")

        else:

            # print error message if date not found in file name
            print(f"\033[91m'Error processing {filename}: Date not found in filename'\033[0m")

    except Exception as e:
        # print error message for exceptions
        print(f"Error processing {filename}: {str(e)}")

# iterate through directory files
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)

    # check each file is a file, not a directory
    if os.path.isfile(file_path):
        update_metadata(file_path)

