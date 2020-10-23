#!/bin/bash
# This program was programmed by suliman Almohawis
# Twitter : https://twitter.com/F14Commander
# For clear
clear
# For print
echo "Please Enter The Name OF your Project :"
# For ask
read -p ":" name
# To Create a  Folder
mkdir ~/Documents/$name
# To create a File
touch ~/Documents/$name/$name
# To go to The Folder 
cd ~/Documents/$name
# To open The Text Editor (vim,code,nano......)
vim $name
# code $name
# nano $name
# gedit $name
exec bash



