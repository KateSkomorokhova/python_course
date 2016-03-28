import argparse
import os.path
import shutil
import subprocess

parser = argparse.ArgumentParser(description="неизвестность и непредсказуемость")
parser.add_argument('command',
                    type=str,
                    choices=['store', 'diff'],
                    help='Я вам помогу')
parser.add_argument('path',
                    type=str,
                    help='Путь к файлу или папке')

args=parser.parse_args()
command = args.command
path = args.path

home_dir = '/home/python_course/sad'
if command == 'store':
    if os.path.isfile(path):
        shutil.copy(path, home_dir)
    else:
        shutil.copy(path, home_dir)
if command == 'diff':
    one = path.split('/')[-1]
    two = "diff " + path + " ./sad/" + one
    print(subprocess.call(two, shell=True))