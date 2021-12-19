#/bin/sh

clear
./snailfish.py test-explode$1
cat test-explode$1-output
