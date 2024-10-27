import importlib
import subprocess
import sys

def check_and_install(package, mirror='https://pypi.org/simple'):
    try:
        importlib.import_module(package)
        print(f"{package} is already installed.")
    except ImportError:
        print(f"{package} is not installed. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, '-i', mirror])

mirror_url = 'https://pypi.tuna.tsinghua.edu.cn/simple'
check_and_install('selenium', mirror=mirror_url)
check_and_install('toml', mirror=mirror_url)

subprocess.run(['python', 'auto_input.py'])
