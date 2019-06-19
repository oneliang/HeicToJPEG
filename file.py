# !/usr/bin/python3
# coding: utf-8
import os


def path_join(path, *paths):
    path = path_fmt(path)

    for p in paths:
        p = path_fmt(p)
        path += "/" + p

    path = path_fmt(path)
    return path


def path_fmt(path):
    if path is None:
        return ""

    path = path.strip()

    while path.find("/") >= 0:
        path = path.replace("/", "\\")
    while path.find("\\\\") >= 0:
        path = path.replace("\\\\", "\\")

    return path


def deep_list(path, suffix):
    if not os.path.isdir(path):
        return list()

    try:
        fs = os.listdir(path)
    except PermissionError:
        print("PermissionError:", path)
        return list()

    suffix = str(suffix).lower().strip()

    fps = list()
    for f in fs:
        f = f.lower().strip()
        if not f.endswith(suffix):
            continue

        fp = path_join(path, f)
        if os.path.isfile(fp):
            fps.append(fp)
        elif os.path.isdir(fp):
            fps.extend(deep_list(fp))
    return fps
