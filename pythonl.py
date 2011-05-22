#!/usr/bin/env python3
# coding: utf-8

import sys
import os
from platform import system as platform_system
import argparse
import json


data_dir = os.path.dirname(sys.executable)
cfg_file = 'pythonl.py.cfg'

def main():
    py_ver = {}

    # check OS
    if platform_system() != 'Windows':
        print('Error: This script is only used on Windows.')
        sys.exit(1)

    # process sys.argv using argparse
    parser = argparse.ArgumentParser(description='Launch script with the Python version defined in the hashbang.')
    parser.add_argument('-s', '--setup', action='store_true', dest='setup',
                        help='Configure Python install paths')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--idle', action='store_true', dest='idle',
                        help='Launch with IDLE shell')
    group.add_argument('-w', '--pyw', action='store_true', dest='pyw',
                        help='Launch without CMD console')
    parser.add_argument('script', nargs='*',
                        help='Script to launch')
    if len(sys.argv) < 2: args = parser.parse_args(['-h'])
    else: args = parser.parse_args()

    # Get and save new install paths 
    if args.setup or not os.path.exists(os.path.join(data_dir, cfg_file)):
        for ver in (('2.x', '26'), ('3.x', '32')):
            while True:
                install_path = input('Enter path for Python {0} [C:\\Python{1}]: '.format(*ver)).rstrip('\r') #rstrip until bug fixed: http://bugs.python.org/issue11272
                if install_path == 'q': sys.exit(0)
                if install_path == '': install_path = 'C:\\Python{0}'.format(ver[1])
                if os.path.exists(os.path.join(install_path, 'python.exe')):
                    py_ver[ver[0][0]] = install_path
                    print()
                    break
                else: print('Python executable not found in that path. Try again or (q)uit.\n')
        _saveR(cfg_file, py_ver)

    # Load install paths from last time
    if not py_ver:
        py_ver = _loadR(cfg_file)

# Script and additional argument processing
    add_args = args.script
    script = add_args.pop(0)

    # Require script with certain switches
    if not script:
        if args.idle or args.pyw:
            print('Script argument required with this switch. Use -h for help.')

    # Launch script if provided
    else:
        if os.path.exists(script):
            with open(script, mode='r', encoding='utf-8') as f:
                hashbang = f.readline()

            py_num = str(int('python2' not in hashbang) + 2) #translate 2 or 3 version num  
            py_path = py_ver[py_num]

            if args.pyw:
                cmd_line = '''start "" "{}\\pythonw.exe" "{}" {}'''.format(py_path, script, ' '.join(add_args))

            elif args.idle:
                cmd_line = '''start "" "{0}\\pythonw.exe" "{0}\\Lib\\idlelib\\idle.pyw" -e "{1}"'''.format(py_path, script)

            else:
                cmd_line = '''cmd /K ""{}\\python.exe" "{}" {}"'''.format(py_path, script, ' '.join(add_args))

            os.system(cmd_line)

        else: print('Script not found ({0})'.format(script))




def _saveR(file, d):
    if not os.path.exists(data_dir): os.makedirs(data_dir)
    with open(os.path.join(data_dir, file), mode='w', encoding='utf-8') as f:
        json.dump(d, f)


def _loadR(file):
    with open(os.path.join(data_dir, file), mode='r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == '__main__':
    main()
