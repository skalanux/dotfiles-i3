#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import io
import locale
import os
import sys

import i3

# This is necessary to allow python to print utf8 characters to console
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)


BLOCK_BUTTON = os.environ.get("BLOCK_BUTTON", 0)

if BLOCK_BUTTON.isdigit():
    BLOCK_BUTTON = int(BLOCK_BUTTON)
else:
    BLOCK_BUTTON = 0

# This should be configurable
UNREAD_FILE = "/tmp/unread_notifications"


class Counter(object):
    @classmethod
    def reset_counter_file(cls):
        try:
            fp = io.open(UNREAD_FILE, "w")
            fp.write(u"0")
            fp.close()
        except:
            pass

    @classmethod
    def get_counter_value(cls):
        try:
            fp = io.open(UNREAD_FILE, "r")
            unread_messages = int(fp.readline())
            fp.close()
        except:
            unread_messages = 0

        return unread_messages

    @classmethod
    def increase_counter_file(cls):
        try:
            unread = cls.get_counter_value()
            fp = io.open(UNREAD_FILE, "w")
            fp.write(unicode(unread+1))
            fp.close()
        except:
            pass

if BLOCK_BUTTON > 0:
    Counter.reset_counter_file()
    i3.focus(title="Devecoop Slack")

# Finally spit the desired output
print u"  %s" % Counter.get_counter_value()
