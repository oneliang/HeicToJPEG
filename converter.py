# !/usr/bin/python3
# coding: utf-8
import gc
import os
import subprocess
import sys
import time
import traceback

this = os.path.abspath(os.path.dirname(__file__))
module = os.path.split(this)[0]
sys.path.append(module)

import file
import mei


def get_resource():
    if getattr(sys, 'frozen', False):
        resource = sys._MEIPASS
    else:
        resource = os.path.abspath(".")
    return resource


def convert(fps):
    resource = get_resource()

    cmd1 = r'"%s\core\rundll32.exe"' % resource
    cmd2 = r'"%s\core\Converter.dll", HeicToJPEG' % resource
    cmd3 = r'"%s"'
    cmd_half = cmd1 + " " + cmd2

    for fp in fps:
        new = str(fp).replace(".heic", ".jpg")
        old_name = os.path.basename(fp)
        new_name = os.path.basename(new)

        if os.path.exists(new):
            print(" File conflict:", new_name)
            continue

        print(" %s -> %s" % (old_name, new_name))
        try:
            cmd = cmd_half + ' "' + fp + '" '
            subprocess.Popen(cmd, shell=False)
            time.sleep(1)
        except RuntimeError:
            traceback.print_exc()


if __name__ == '__main__':
    try:
        print("\n         HeicToJPEG")
        cwd = os.getcwd()

        print("\n Search file in this folder:\n ", cwd)
        fps = file.deep_list(cwd, ".heic")
        if len(fps) < 1:
            print("\n No Heic file in this folder")
        else:
            print("\n %s files in this folder" % len(fps))
            convert(fps)

    except:
        traceback.print_exc()
    finally:
        print("\n Wait a minute..")
        time.sleep(5)

        gc.collect()
        mei.remove()
