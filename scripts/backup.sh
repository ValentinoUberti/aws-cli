#!/bin/sh
ls -altr /data
echo "ciao"
python ./send_email.py
echo "email spedita"
sleep 200
exit 0
