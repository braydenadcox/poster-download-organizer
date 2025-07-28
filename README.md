# Canva Poster Download Organizer
These scripts, based on the language that you want, allow you to be able to organize files based on their suffix where you want!

## Steps For Setup On Your Environment
- Open VS Code or your other IDE with Git installed
- Navigate in your VS Code terminal to the directory you want the repo to be placed in with
```cd path/to/your/directory```

-Once in your directory, clone this repository with this command:
```git clone https://github.com/braydenadcox/poster-download-organizer.git```

## Tailoring and Usage
Edit the target directory "TARGET_DIR" and the directory the files plan to be taken to "DOWNLOADS_DIR" with the paths you have. TARGET_DIR should be renamed to the path of the folder you want your files to go to. This can be done by navigating to the directory in file explorer and copying the path at the top.

Once done with that, edit this code to a suffix that all the files you wish to use have in common. For me, all the posters I want to transfer have the suffix '1620.png' or '1620.jpg' so my line looks like this:
```elif filename.endswith('1620.png') or filename.endswith('1620.jpg'):```

Make sure you press CTRL + S multiple times to ensure your preferences save.

Once done, run the script in the terminal with this command:
```python script.py```

Now, go to Canva, download the files you need, and enjoy!
