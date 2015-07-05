#!/usr/bin/env python
import io

import i3

UNREAD_FILE = "/tmp/unread_notifications"

def reset_counter_file():
    try:
        fp = io.open(UNREAD_FILE, "w")
        fp.write(u"0")
        fp.close()
    except:
        pass

if __name__=="__main__":
    reset_counter_file()
    i3.focus(title="Devecoop Slack")
