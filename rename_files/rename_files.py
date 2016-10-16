import os

def rename_files():
    # get file names from a folder
    file_list = os.listdir('YOUR DRIVE HERE')

    path = os.getcwd()

    os.chdir('/Users/USERNAME/PATH/TO/YOUR/FILES')

    # for each file, rename filename
    file_num = 0

    for file_name in file_list:
       os.rename(file_name, file_name.translate(None, " "))
       new_filename = "bckground_img_{}.png".format(file_num)
       os.rename(file_name, new_filename)
       print(new_filename)
       file_num += 1

    os.chdir(path)

rename_files()
