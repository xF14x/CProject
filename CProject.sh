#!/bin/bash
# This program was programmed by suliman Almohawis
# Twitter : https://twitter.com/F14Commander
# For clear
clear
# For print
echo "Pleas Enter The Name OF your Project :"
# For ask
read -p ":" name
# For create The Folder
mkdir ~/Documents/$name
# For create The File
touch ~/Documents/$name/$name
# For go to The Folder 
cd ~/Documents/$name
# For open The  Text Editor (vim,code,nano......)
vim $name
# code $name
# nano $name
# gedit $name
exec bash



