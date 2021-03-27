#!/bin/bash

time_when_script_started=$(date +'%y.%m.%d.%k.%M.%S')
python3 systemtime.py
time_when_script_ended=$(date +'%y.%m.%d.%k.%M.%S')
user=$(whoami)

echo "START__________END____________USER"
echo "$time_when_script_started $time_when_script_ended $user"
