#!/bin/bash

image='catalog.png'
./manage.py graph_models -a -g -o $image && echo "File $(readlink -f $image) created."

