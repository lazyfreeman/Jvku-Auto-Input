@echo off
chcp 65001 > nul

echo 请确认您已查看并按照要求修改文件夹中的 config.toml 文件。确认后按 Enter 执行程序。
pause

python main.py
