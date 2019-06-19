# !/usr/bin/python3
# coding: utf-8
import os
import re

import sys
import traceback


def match(path):
    basename = os.path.basename(path)
    return re.match("^_MEI\d+$", basename) and True or False


def find():
    try:
        return sys._MEIPASS
    except AttributeError:
        traceback.print_exc()

    for index, path in enumerate(sys.path):
        if match(path):
            return path
    return None


def remove():
    try:
        path = find()
        os.remove(path)
    except PermissionError:
        traceback.print_exc()
