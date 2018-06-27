#!/bin/sh
ls -altr /data
echo "Hello from backup.sh"
python ./send_email.py
sleep 200
exit 0
