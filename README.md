# HeicToJPEG

基于 `python3.6` 和 `Windows` 平台

## 打包

`pyinstaller -F -i ico.ico --add-data core;core converter.py`

## 流程

- search .heic files in cwd folder
- convert .heic one by one
- conflict when the xx.jpg is existed

## 支持

[CopyTrans HEIC for Windows](https://www.copytrans.net/copytransheic/)