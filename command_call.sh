#!/bin/sh
python ./manage.py print_models 2> "$(date +"%d_%m_%y").dat" 
