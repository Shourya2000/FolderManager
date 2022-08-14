import os
import shutil
import time
import random

main_path = "C:/Users/dell/Downloads/"
img_path = 'C:/Users/dell/Downloads/Images/'
vid_path = 'C:/Users/dell/Downloads/Videos/'
tor_path = 'C:/Users/dell/Downloads/Torrent/'
zip_path = 'C:/Users/dell/Downloads/zips/'
audio_path = 'C:/Users/dell/Downloads/AudioFile/'
exe_path = 'C:/Users/dell/Downloads/exeFiles/'
apk_path = 'C:/Users/dell/Downloads/APK/'
html_path = 'C:/Users/dell/Downloads/HTML/'
other_path = 'C:/Users/dell/Downloads/OTHER/'
txt_path = 'C:/Users/dell/Downloads/Text/'
python_path = 'C:/Users/dell/Downloads/PythonFiles/'

def fileName(name):
    name = str(name)
    name_in_list = name.split(".")
    number = str(random.randint(1000,1000000))
    return (name_in_list[0] + number + "." + name_in_list[-1])


def main_global():
   while True:
       all_files = os.listdir(main_path)
       time.sleep(3)
       for each in all_files:
           each2 = each.lower()
           each_after_change = fileName(each2)
           if "." in each2:
               if '.tmp' not in each2  and '.crdownload' not in each:
                   if '.png' in each or '.jpg' in each or '.ico' in each or '.jpeg' in each:
                       shutil.move((main_path+each),(img_path+each_after_change))

                   elif '.mp4' in each2 or '.mkv' in each2 or '.webm' in each2:
                       shutil.move((main_path+each),(vid_path+each_after_change))

                   elif '.torrent' in each2:
                       shutil.move((main_path+each),(tor_path+each_after_change))

                   elif '.win' in each2 or '.rar' in each2 or '.zip' in each2:
                       shutil.move((main_path + each),(zip_path + each_after_change))

                   elif '.mp3' in each2 or '.m4a' in each2 or '.M4A' in each2 or 'WMA' in each2:
                       shutil.move((main_path+each),(audio_path+each_after_change))

                   elif '.exe' in each2:
                       shutil.move((main_path + each),(exe_path + each_after_change))

                   elif '.apk' in each2:
                       shutil.move((main_path + each),(apk_path + each_after_change))

                   elif '.html' in each2:
                       ((main_path + each),(html_path + each_after_change))

                   elif '.txt' in each2:
                       shutil.move((main_path + each),(txt_path + each_after_change))

                   else:
                       shutil.move((main_path + each),(other_path + each_after_change))
               else:
                   print(f"Wrong Format :    {each}")
main_global()

#(main_path+each),(audio_path+each_after_change)