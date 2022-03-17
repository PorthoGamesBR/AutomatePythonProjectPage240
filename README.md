# Automate the Boring Stuff with Python by Al Sweigart
## Project Page 240: Renaming Files with Dates

- Generate a large number of files with american style dates as their names (mm-dd-yyyy).
- All files have the original date saved in them so you can check if you code worked well after.
- Simple implementation of the date style conversor presented in the book (american to european).

## How to use:
###### Valid American Style Date Generation:
- `gendates.py` -> Prints the help text

- `gendates.py path=Path to save files name=Name of files num=Num of files` -> Creates all files

- `gendates.py defalut` -> Creates files in default mode
DEFAULT: gendates (save in current work directory) "us_date_" 100

- `gendates.py compress path=Path to save files name=Name of Files num=Num of files` -> Creates files and compress

- `gendates.py compress default` -> Creates files in default mode and compress

###### Converting to European Date Style:
- `dateconversor.py (Path to files)` -> Converts every file inside the path that has american style dates

## Functions
### gendates.py
- `check_leap(year)` - Accepts an integer. Checks whenever that number will be a leap year or not, and returns True if yes and False if not.
- `date_generator(n)` - Accepts an integer and returns a list of strings. Generates a list of n size with valid non repeating american style dates.
- `compress_dates(path, name, dates)` - path is a pathlib.Path object, name is a string and dates is a list of strings. In the path, for each date in the list, gets the file with name + date and sends it into a .zip file in the same path.

## Todo's
### gendates.py
- [x] Getting user command line arguments separated by name
- [x] Generating valid american dates with a function
- [x] Compressing all date files in the path to a .zip archive
- [x] Deleting the original files so we dont get duplicates
- [ ] Organizing `main()` in different functions

### dateconversor.py
- [x] Regex to indentify american style dates
- [x] Getting all file names inside the path
- [x] Indentify the files with valid american style dates
- [x] Converting the dates in the filenames to european style
- [ ] try/except in `re.sub()` and `.group()`
- [x] Use `shutil.move()` to change the name of the files
- [ ] Organize code in functions
- [x] Get user inputed path
- [ ] Check if path is valid

## Support
Made based on the book ['Automate the Boring Stuff with Python' by Al Sweigart](https://automatetheboringstuff.com/).

Consider [donating to the writer of the book](https://www.patreon.com/AlSweigart).


And consider following me in my [youtube channel about programming](https://www.youtube.com/channel/UCOzf_llnNj7zoyst26eb_sQ)
