1、生成 spec
pyi-makespec -F converter.py

2、编辑 spec
datas=[('core','core')]

3、生成 exe
pyinstaller -F converter.spec