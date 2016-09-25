#!/usr/bin/env python3
import os
my_uid = os.getuid()


def pid_pi(status_file):
    with open(status_file) as f:
        for line in f:
            line = line.strip()
            if line.startswith('Uid:'):
                uid = int(line.split()[1])
                return uid == my_uid

processus = [pid for pid in os.listdir('/proc') if pid.isdigit()]

for process in processus:
    cmdline_file = '/proc/{0}/cmdline'.format(process)
    status_file = '/proc/{0}/status'.format(process)
    if os.path.exists(cmdline_file):
        cmdline = open(cmdline_file).readline()
        if cmdline != '':
            cmdline = cmdline.replace('\x00', ' ')
            if pid_pi(status_file):
                print('{0}:{1}'.format(process, cmdline))
