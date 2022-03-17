# Date Files Creator
# Create a number of files with valid dates in american format.
# It saves the date in the name and inside the file so we can check the original date after renaming
# The user can choose if they want to .zip the files or not
# Made for the Automate The Boring Stuff with Python book, project at page 240

help_text = """
gendates.py path=<Path to save files> name=<Name of files> num=<Num of files> -> Creates all files

gendates.py defalut -> Creates files in default mode
DEFAULT: gendates (save in current work directory) "us_date_" 100

gendates.py compress path=<Path to save files> name=<Name of Files> num=<Num of files> -> Creates files and compress

gendates.py compress default -> Creates files in default mode and compress
"""

import sys
from pathlib import Path
from random import randint
import zipfile
from zipfile import ZipFile
from os import unlink

#Main function.
#TODO: Organize it in diferent functions
def main(argv):
    #If it has less than 2 args, print the help text
    if len(argv) < 2:
        print(help_text)
        sys.exit(0)

    #The default parameters.
    param_dict = {
    "path": str(Path.cwd()),
    "name": 'us_date_',
    "num": 100}

    #Compress is kept out of param_dict because its just a option.
    #Its a int so it can be used in the index of the args
    compress = 0

    if argv[1].lower() == 'compress':
        compress = 1

    #If it has compress as it first arg, start by the 3th argument
    if argv[1+compress].lower() != 'default':
        for arg in argv[1+compress:]:

            if '=' not in arg: #If it has not = in it, ignore it
                continue
            arg_split = arg.split("=")

            if arg_split[0].lower() not in param_dict: #If the name before = isnt in the list of valid parameters, ignore it
                continue
            else:
                param_dict[arg_split[0].lower()] = arg_split[1] #Save the parameter

    #Checks if path is valid
    if not Path(param_dict['path']).is_dir():
        print("Invalid or non existent path : " + param_dict['path'])
        sys.exit(1)
    else:
        if param_dict['path'] == str(Path.cwd()): #If is using the default path,
            param_dict['path'] = Path(param_dict['path']) / 'dates' #Set the target as 'dates' folder in the work dir
            param_dict['path'].mkdir(exist_ok = True) #And creates the folder if it does not exist
        else:
            param_dict['path'] = Path(param_dict['path'])

    try:
        param_dict['num'] = abs(int(param_dict['num'])) #The abs is for possible negative numbers
        if param_dict['num'] > 3359664: #3359664 is the min number of date combinations (12 * 28 * 9999)
            param_dict['num'] = 3359664 #This is the max number to prevent infinite loop in the date gen function
    except ValueError:
        print('Not valid integer number in num parameter.')
        sys.exit(2)

    list_of_dates = date_generator(param_dict['num']) #Generares a list of valid dates

    for date in list_of_dates: #Write all of them to files
        f = open(param_dict['path'] / (param_dict['name'] + date + '.txt'),'w')
        f.write(date)
        f.close()

    end_msg = "Generated %s files and saved in %s" #Message to print if the process was a sucess
    if compress: #If compress is 1, do the compression and change the sucess message
        compress_dates(param_dict['path'], param_dict['name'],list_of_dates)
        end_msg = "Generated and compressed %s files and saved in %s"

    print(end_msg % (param_dict['num'],param_dict['path']))
    sys.exit(0)

#Check if the year is a leap year or not
def check_leap(y):
    if (y % 400 == 0) or (y % 100 != 0) and (y % 4 == 0):
        return True
    else:
        return False

#Generate a list of valid dates
def date_generator(n):
    #Max months: 12
    #Max days: 30 if m=4,6,9 or 11, 28 or 29 if m=2 and 31 else
    all_dates = {} #Using dict so we dont have repetition between the dates, since keys dont have repetition
    while len(all_dates) < n:
        m = randint(1,12)
        d = 0
        y = randint(1,9999)
        maxDays = 31

        if m == 2: #February
            maxDays = 28 + int(check_leap(y)) #If is a leap year, february can gave 29
        elif m in (4,6,9,11):
            maxDays = 30

        d = randint(1,maxDays)

        #{02d}.format makes the string of the converted numbers have 0s if they are less than 2 digits
        #{04d}.format does the same thing, but with 4 digits
        date = '%s-%s-%s' % ('{:02d}'.format(m),'{:02d}'.format(d),'{:04d}'.format(y))
        all_dates[date] = '' #This is just to save the keys, since we dont need any value

    return list(all_dates) #Return the keys of the dict as a list


# Compact all files created and deletes them from the directory
def compress_dates(p,n,dates): #Path, Name of files and List of Dates
    datesZip = ZipFile(p / 'dates.zip','w')
    for d in dates: #Check a file for every date in the list
        basename = n + d + '.txt' #The name of the archive inside the zip.
        #If we use only the full path,it saves the full path inside the zip.To solve that, we use arcname
        datesZip.write(p / basename, compress_type=zipfile.ZIP_DEFLATED,arcname=basename) #Sends file to .zip archive
        unlink(p / basename) #Deletes the file
    datesZip.close()

if __name__ == "__main__":
    main(sys.argv)
