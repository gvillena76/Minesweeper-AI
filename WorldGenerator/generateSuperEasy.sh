#!/bin/bash

rm -rf Problems
mkdir Problems

python3 WorldGenerator.py 1000 Easy_world_ 5 5 1  #NOTE: I changed to 10.  Normally should be 1000!

echo Finished generating worlds!
