#!/bin/sh
ls -altr /data
echo "ciao"
mail -s "hello" "info@valentinouberti.com" <<EOF
hello
world
EOF
sleep 200
exit 0
