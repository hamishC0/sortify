This is my first ever project so expect it to be basic. Yes, it runs slowly I assume (15-ish minutes to edit 9,500 files). No, I don't know how speed optimisation works. I probably wouldn't be using Python if I did. I'm a chemical engineering student and I know some basic python and decided to make somethoing useful for myself. Hopefully someone out there sees this and it helps them too.

The idea is that when backing up your data from Snapchat (native), Instagram (native), Messages (many Github projects for this) you are left with a bunch of image and video files that have a creation date in their metadata corrrespoding to the date and time the backup was done, not the real date of the original file. As they come with dates in the name for the most part (Instagram isnt so friendly...) I made this script to pll the date from the name and update the metadata to reflect the date of the file's creation. 

I guess it isn't limited to these backups and could change the info for any set of files you have with dates in the name but no metadata to match if you wanted to do that. 

If anyone knows how instagram encodes the time and date in their backed up files I would be really interested to hear because I'm quite stuck. I made a couple reddit posts about it noting that I'd seen this post (https://instagram-engineering.com/sharding-ids-at-instagram-1cf5a71e5a5c) about it but had found reversing this process not to work as my ms values were around 2 years off from the correct dates, and not consistently the same distance off.


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
Program runs in Python.

This program also requires 'exiftool' to be installed to function. You can install it using homebrew like this:
  ```sh
  brew install exiftool
  ```
and you can check the installation with 
  ```sh
  exiftool -ver
  ```
### Installation and Use

1. Clone the repo
   ```sh
   git clone https://github.com/HamishC0/Sortify.git
   ```
2. Move to the directory containing the the program and run
   ```sh
   python sortify_0.1.py
   ```
3. Enter the path to the directory with your files when prompted by the terminal
   ```sh
   Enter your directory path: your_path_here
   ```

If the dates in your filenames don't match the formats:  
```YYYY-MM-DD HH mm ss```  
```YYYY MM DD HH mm ss```  
```YYYY-MM-DD HH:mm:ss```   
```YYYY-MM-DD```

you will need to edit the program to add this or put one of those requests in here to change the program on here. The ones I used were just the file name formats I needed to be able to apply it to imessage and snapchat backups.

For those with date and time, edit the first ```date_match``` by adding ```|(\d{4} \d{2} \d{2} \d{2} \d{2} \d{2})``` before ```, file_name)``` and adding the correct punctuation to match your date and time format.  
For thsoe with date only, edit the second ```date_match``` by adding ```|(\d{4} \d{2} \d{2})``` before ```, file_name)``` and adding the correct punctuation to match your date format.
