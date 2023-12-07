import os
import shutil
import schedule
import time
import datetime

USER_HOME_PATH = os.path.expanduser("~")
USER_PATH = USER_HOME_PATH.replace("\\", "/")

BACKUP_TIMES = [":00", ":15", ":30", ":45"]  # Runs every quarter hour.
SOURCE_DIR = USER_PATH + "/AppData/Local/Larian Studios/Baldur's Gate 3/PlayerProfiles"
DEST_DIR = USER_PATH + "/OneDrive/BG3_Saves"


def copy_folder_to_directory(source, dest):
    current_time = datetime.datetime.now().date()
    dest_dir = os.path.join(dest, str(current_time))

    def custom_copytree(src, dst):  # Custom in order to overwrite files in destination.
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                custom_copytree(s, d)
            else:
                shutil.copy2(s, d)

    custom_copytree(source, dest_dir)
    print(f"Folder copied to: {dest_dir}")


for time_slot in BACKUP_TIMES:
    schedule.every().hour.at(time_slot).do(
        lambda: copy_folder_to_directory(SOURCE_DIR, DEST_DIR)
    )

while True:
    schedule.run_pending()
    time.sleep(60)
