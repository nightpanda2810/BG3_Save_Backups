
# Baulders Gate 3 Save Files Auto Backup

  

Quick and dirty script to copy save files to desired destination, for Windows only. Noticed the cloud save with Gog dissapear after patch 5, as well as cloud save only backing up the LATEST campaign. Did this to make sure I never lost anything. Overwrites files backed up on the same day, otherwise creates a new folder daily.

You WILL need to clean up old backup folders yourself.

Default save path is c:\users\USERNAME\OneDrive\BG3_Saves\CURRENT_DATE
Runs every quarter hour (12:00, 12:15, etc.)
Simply run the .py and it will run until you close it.
Same goes for the EXE. You will need to compile your own executable for a custom path.
To run the EXE automatically, look up how to schedule a task in Windows, just have it run at login.

I have NO IDEA how to use Git properly, this is my first public script I wrote from scratch. Just started learning Python about a month ago.