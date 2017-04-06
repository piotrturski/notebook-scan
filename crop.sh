#!/usr/bin/env bash

# 2-sided short edge binding scan

input=${1:-"."}

mkdir $input/result

convert $input/*.png -limit area 1GB -rotate 90 -crop '2x1+100+0@' +repage +adjoin $input/result/%04d.png 
