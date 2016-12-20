#!/bin/bash

PID=`ps auxw | grep runserver | grep -v grep | awk '{ print $2 }'`
echo "Stopping server..."
kill -9 ${PID}

if [ $? -eq 0 ]; then
    echo "Server stopped successfully"
else
    echo "Could not stop server!"
fi
