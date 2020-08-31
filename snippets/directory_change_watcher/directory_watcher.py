#!/usr/bin/env python

'''
Testing file system watcher using pywin32
'''

import os

import win32file
import win32con

ACTIONS = {
    1: 'created',
    2: 'deleted',
    3: 'updated',
    4: 'renamed from something',
    5: 'renamed to something'
}

path_to_watch = "C:\\Users\\css112720\\Downloads\\misc"
watcher = win32file.CreateFile(
    path_to_watch,
    0x0001, #FILE_LIST_DIRECTORY
    win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
    None,
    win32con.OPEN_EXISTING,
    win32con.FILE_FLAG_BACKUP_SEMANTICS,
    None
)

while True:
    results = win32file.ReadDirectoryChangesW(
        watcher,
        1024,
        True,
        win32con.FILE_NOTIFY_CHANGE_FILE_NAME | 
        win32con.FILE_NOTIFY_CHANGE_DIR_NAME | 
        win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES | 
        win32con.FILE_NOTIFY_CHANGE_SIZE | 
        win32con.FILE_NOTIFY_CHANGE_LAST_WRITE | 
        win32con.FILE_NOTIFY_CHANGE_SECURITY,
        None,
        None
    )
    for action, fname in results:
        full_filename = os.path.join(path_to_watch, fname)
        print(full_filename, ACTIONS.get(action, "Unknown"))

