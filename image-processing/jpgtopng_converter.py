import sys
import os
from PIL import Image

# task is to convert jpg into png through command
# for ex filename.py  /image_folder/ /whereTo store/

# hints

# Grab the 2 arguments from the command
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# print(image_folder, output_folder)

# check whether where to store folder exists or not , if not create one
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Loop through image folder and convert all the jpg image into png
for file_name in os.listdir(image_folder):
    print(file_name, 'file_name')
    current_path = os.getcwd()
    img = Image.open(f'{current_path}/{image_folder}/{file_name}')
    #  If we didn't did clean_name that time output file was stored in kdp.jpg.png format
    # we want to remove .jpg from the file name so if we do os.path.splitText() it will
    # return the result in tuple format like this (file_name, '.jpg)
    clean_name = os.path.splitext(file_name)[0]
    print(clean_name, 'clean_name')
    img.save(f'{current_path}/{output_folder}/{clean_name}.png', 'png')
    print('All done')
